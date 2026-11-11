# Félidos de Costa Rica: paso 2 de la aplicación shiny del capítulo 18
# (dos filtros, una expresión reactiva y una tabla interactiva)

# Paquetes ---------------------------------------------------------------
library(shiny)
library(bslib)
library(tidyverse)
library(sf)
library(DT)

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

# Listas de opciones de los controles
especies <- sort(unique(felidos$species))
provincias <- sort(unique(cantones$provincia))

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
    )
  ),
  textOutput("conteo"),
  card(
    card_header("Lista de registros"),
    DTOutput("tabla")
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

  # Texto con la cantidad de registros filtrados
  output$conteo <- renderText({
    paste(nrow(felidos_filtrados()), "registros de presencia")
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
