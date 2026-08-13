# Imagen de rocker/geospatial que se utiliza como base.
# Incluye R, RStudio Server, Quarto, tidyverse, sf, terra y leaflet.
# Por reproducibilidad, se fijan las versiones de la imagen y de los
# paquetes adicionales; actualizarlas es una decisión explícita.
FROM rocker/geospatial:4.6.1

# Clave para ingresar a RStudio Server
ENV PASSWORD=pf0953

# Puerto de RStudio Server
EXPOSE 8787

# Gestor de paquetes pak, para instalar versiones específicas
RUN R -e "if (!requireNamespace('pak', quietly = TRUE)) install.packages('pak', repos = 'https://cloud.r-project.org')"

# Instalación de paquetes adicionales de R, con versiones fijas:
# - here 1.0.2: rutas de archivos relativas al proyecto
# - plotly 4.12.1: gráficos estadísticos interactivos
# - DT 0.34.0: tablas interactivas
# - rgbif 3.8.5: acceso a la API de GBIF
# - leaflet.extras 2.0.2: complementos para mapas de leaflet
RUN R -e "pak::pak(c('here@1.0.2', 'plotly@4.12.1', 'DT@0.34.0', 'rgbif@3.8.5', 'leaflet.extras@2.0.2'))"
