# Félidos de Costa Rica: aplicación shiny de ejemplo del capítulo 18
# del curso PF-0953 Programación en R (2026-II)

# Paquetes ---------------------------------------------------------------
library(shiny)
library(bslib)
library(tidyverse)
library(sf)
library(DT)
library(plotly)
library(leaflet)

# Datos (se ejecuta una sola vez, al iniciar la aplicación) --------------
datos <- "https://raw.githubusercontent.com/pf0953-programacionr/2026-ii/main/datos/"

cantones <- st_read(paste0(datos, "cantones.gpkg"), quiet = TRUE)

# Registros de félidos como puntos, con el cantón y la provincia
# en que cae cada uno (medir en CRTM05, dibujar en WGS84)
felidos <- read_csv(paste0(datos, "felidos.csv"), show_col_types = FALSE) |>
  st_as_sf(coords = c("decimalLongitude", "decimalLatitude"), crs = 4326) |>
  st_transform(8908) |>
  st_join(cantones, join = st_within) |>
  st_transform(4326)

cantones <- st_transform(cantones, 4326)

# Listas de opciones de los controles y paleta de colores de las especies
especies <- sort(unique(felidos$species))
provincias <- sort(unique(cantones$provincia))
paleta_especies <- colorFactor(palette = "Dark2", domain = especies)

# Interfaz de usuario ----------------------------------------------------
ui <- page_sidebar(
  title = "Félidos de Costa Rica",
  sidebar = sidebar(
    selectInput(
      inputId = "especie",
      label = "Especie",
      choices = c("Todas", especies)
    ),
    selectInput(
      inputId = "provincia",
      label = "Provincia",
      choices = c("Todas", provincias)
    ),
    helpText("Fuentes: GBIF (2026) e IGN (s. f.)")
  ),
  layout_columns(
    value_box(title = "Registros de presencia", value = textOutput("registros")),
    value_box(title = "Especies", value = textOutput("especies")),
    value_box(title = "Cantones con registros", value = textOutput("cantones")),
    fill = FALSE
  ),
  layout_columns(
    card(
      card_header("Registros de presencia"),
      leafletOutput("mapa"),
      full_screen = TRUE
    ),
    card(
      card_header("Cantones con más registros"),
      plotlyOutput("grafico"),
      full_screen = TRUE
    ),
    col_widths = c(7, 5)
  ),
  card(
    card_header("Lista de registros"),
    DTOutput("tabla"),
    full_screen = TRUE
  ),
  fillable = FALSE
)

# Servidor ---------------------------------------------------------------
server <- function(input, output, session) {
  # Expresión reactiva: los registros que cumplen los filtros
  felidos_filtrados <- reactive({
    filtrados <- felidos

    if (input$especie != "Todas") {
      filtrados <- filter(filtrados, species == input$especie)
    }

    if (input$provincia != "Todas") {
      filtrados <- filter(filtrados, provincia == input$provincia)
    }

    filtrados
  })

  # Cajas de valor
  output$registros <- renderText({
    nrow(felidos_filtrados())
  })

  output$especies <- renderText({
    n_distinct(felidos_filtrados()$species)
  })

  output$cantones <- renderText({
    n_distinct(felidos_filtrados()$canton, na.rm = TRUE)
  })

  # Mapa
  output$mapa <- renderLeaflet({
    validate(need(nrow(felidos_filtrados()) > 0, "No hay registros con estos filtros."))

    leaflet() |>
      addProviderTiles(providers$Esri.WorldGrayCanvas, group = "Fondo gris (Esri)") |>
      addTiles(group = "OpenStreetMap") |>
      addPolygons(
        data = cantones,
        color = "#666666",
        weight = 0.5,
        fillOpacity = 0,
        label = ~canton
      ) |>
      addCircleMarkers(
        data = felidos_filtrados(),
        radius = 4,
        color = ~paleta_especies(species),
        fillOpacity = 0.7,
        stroke = FALSE,
        label = ~species,
        popup = ~paste0("<b>", species, "</b><br>", eventDate, "<br>", locality)
      ) |>
      addLegend(position = "bottomright", pal = paleta_especies, values = especies, title = "Especie") |>
      addLayersControl(baseGroups = c("Fondo gris (Esri)", "OpenStreetMap")) |>
      setView(lng = -84.2, lat = 9.9, zoom = 7) |>
      addScaleBar(position = "bottomleft")
  })

  # Gráfico
  output$grafico <- renderPlotly({
    validate(need(nrow(felidos_filtrados()) > 0, "No hay registros con estos filtros."))

    registros_canton <- felidos_filtrados() |>
      st_drop_geometry() |>
      filter(!is.na(canton)) |>
      count(canton, name = "registros", sort = TRUE) |>
      head(10)

    grafico <- registros_canton |>
      ggplot(aes(
        x = registros,
        y = fct_reorder(canton, registros),
        text = paste0(canton, ": ", registros, " registros")
      )) +
      geom_col(fill = "#005da4") +
      labs(x = "Registros", y = NULL) +
      theme_minimal()

    ggplotly(grafico, tooltip = "text") |>
      config(locale = "es", displaylogo = FALSE)
  })

  # Tabla
  output$tabla <- renderDT({
    felidos_filtrados() |>
      st_drop_geometry() |>
      select(species, eventDate, provincia, canton, locality) |>
      datatable(
        rownames = FALSE,
        colnames = c("Especie", "Fecha", "Provincia", "Cantón", "Localidad"),
        options = list(
          pageLength = 5,
          language = list(url = "https://cdn.datatables.net/plug-ins/2.3.2/i18n/es-ES.json")
        )
      )
  })
}

# Aplicación -------------------------------------------------------------
shinyApp(ui = ui, server = server)
