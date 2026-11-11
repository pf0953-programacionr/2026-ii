# Félidos de Costa Rica: paso 1 de la aplicación shiny del capítulo 18
# (estructura mínima: un control de entrada y una salida de texto)

# Paquetes ---------------------------------------------------------------
library(shiny)
library(bslib)
library(tidyverse)

# Datos (se ejecuta una sola vez, al iniciar la aplicación) --------------
datos <- "https://raw.githubusercontent.com/pf0953-programacionr/2026-ii/main/datos/"

felidos <- read_csv(paste0(datos, "felidos.csv"), show_col_types = FALSE)

# Lista de opciones del control de entrada
especies <- sort(unique(felidos$species))

# Interfaz de usuario ----------------------------------------------------
ui <- page_sidebar(
  title = "Félidos de Costa Rica",
  sidebar = sidebar(
    selectInput(
      inputId = "especie",
      label = "Especie",
      choices = especies
    )
  ),
  textOutput("conteo")
)

# Servidor ---------------------------------------------------------------
server <- function(input, output, session) {
  # Texto con la cantidad de registros de la especie elegida
  output$conteo <- renderText({
    registros <- filter(felidos, species == input$especie)

    paste0(input$especie, ": ", nrow(registros), " registros de presencia")
  })
}

# Aplicación -------------------------------------------------------------
shinyApp(ui = ui, server = server)
