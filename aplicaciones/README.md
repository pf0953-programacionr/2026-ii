# Aplicaciones shiny

Código de la aplicación de ejemplo del capítulo 18 del sitio del curso,
[«shiny: aplicaciones web interactivas»](https://pf0953-programacionr.github.io/2026-ii/contenidos/v-tableros-aplicaciones-interactivas/18-shiny.html):
registros de presencia de félidos de Costa Rica (GBIF), filtrados por especie
y por provincia, en cajas de valor, un mapa, un gráfico y una tabla.

- `felidos/app.R`: la aplicación terminada (paso 5 del capítulo).
- `pasos/paso-1/app.R` a `pasos/paso-4/app.R`: las versiones intermedias que
  el capítulo construye (estructura mínima; expresión reactiva y tabla;
  gráfico; mapa).

El capítulo incluye estos archivos tal como están (opción `file` de los
bloques de código), de modo que lo que se muestra en el sitio es lo que se
probó. Como el sitio usa `freeze: auto`, después de modificar un `app.R` hay
que volver a renderizar el capítulo borrando su carpeta en `_freeze/`.

Para ejecutar una aplicación, en R, desde la raíz del repositorio:

```r
shiny::runApp("aplicaciones/felidos")
```

Requiere los paquetes shiny, bslib, tidyverse, sf, DT, plotly y leaflet, y
conexión a Internet: los datos se leen del directorio `datos/` de este
repositorio por su URL.
