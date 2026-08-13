# Imagen de rocker/geospatial que se utiliza como base.
# Incluye R, RStudio Server, Quarto, tidyverse, sf, terra y leaflet.
# Se usa la versión más actualizada, tanto de la imagen como de los paquetes.
FROM rocker/geospatial:latest

# Clave para ingresar a RStudio Server
ENV PASSWORD=pf0953

# Puerto de RStudio Server
EXPOSE 8787

# Instalación de paquetes adicionales de R, en sus versiones más recientes
RUN R -e "install.packages(c('here', 'plotly', 'DT', 'rgbif', 'leaflet.extras'), repos = 'https://cloud.r-project.org')"
