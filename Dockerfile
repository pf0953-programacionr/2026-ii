# Imagen de rocker/geospatial que se utiliza como base.
# Incluye R, RStudio Server, Quarto, tidyverse, sf, terra y leaflet.
# La versión de la imagen se fija por reproducibilidad; actualizarla es una
# decisión explícita. Los paquetes adicionales se instalan en sus versiones
# más recientes al momento de construir la imagen.
FROM rocker/geospatial:4.6.1

# Clave para ingresar a RStudio Server
ENV PASSWORD=pf0953

# Puerto de RStudio Server
EXPOSE 8787

# Instalación de paquetes adicionales de R, en sus versiones más recientes
RUN R -e "install.packages(c('here', 'plotly', 'DT', 'rgbif', 'leaflet.extras'), repos = 'https://cloud.r-project.org')"
