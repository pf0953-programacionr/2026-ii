# Genera datos/felidos.csv: registros de presencia de félidos (familia
# Felidae) en Costa Rica, descargados de la API de GBIF con el paquete rgbif.
#
# Se recuperan los registros con coordenadas y sin problemas geoespaciales
# detectados por GBIF, iterando por «páginas» de 300 como en el ejemplo de la
# semana 1 del curso. Se excluyen las observaciones automáticas
# (basisOfRecord == "MACHINE_OBSERVATION"): son miles de fotografías de
# cámaras trampa, casi todas de jaguar y concentradas en unos pocos sitios,
# que ocultarían el patrón del resto de los registros en los mapas de las
# lecciones. Se excluye también el gato doméstico (Felis catus), que no es un
# félido silvestre. Se conservan solo las columnas que usan las lecciones.
#
# Como GBIF recibe registros nuevos continuamente, el resultado varía según
# la fecha de la consulta; la versión versionada en el repositorio es la que
# usan las lecciones.
#
# Uso (desde la raíz del repositorio, en el contenedor del curso):
#   Rscript datos/generar-felidos.R

suppressPackageStartupMessages({
  library(rgbif)
  library(dplyr)
  library(readr)
})

limite <- 300
inicio <- 0
registros_acumulados <- list()

repeat {
  res <- occ_search(
    familyKey = 9703, # Felidae
    country = "CR",
    hasCoordinate = TRUE,
    hasGeospatialIssue = FALSE,
    limit = limite,
    start = inicio
  )
  registros <- res$data
  if (is.null(registros) || nrow(registros) == 0) break
  registros_acumulados[[length(registros_acumulados) + 1]] <- registros
  inicio <- inicio + limite
}

felidos <- bind_rows(registros_acumulados) |>
  filter(
    basisOfRecord != "MACHINE_OBSERVATION",
    !is.na(species),
    species != "Felis catus"
  ) |>
  mutate(eventDate = substr(eventDate, 1, 10)) |>
  select(
    gbifID, species, basisOfRecord, eventDate, year,
    stateProvince, locality, decimalLongitude, decimalLatitude
  ) |>
  arrange(species, eventDate, gbifID)

write_csv(felidos, "datos/felidos.csv", na = "")

cat("Registros escritos:", nrow(felidos), "\n")
print(count(felidos, species, sort = TRUE))
print(count(felidos, basisOfRecord, sort = TRUE))
