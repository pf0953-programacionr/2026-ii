# Datos del curso

Conjuntos de datos que se usan en las lecciones y en los ejercicios del curso. Todos pueden leerse directamente desde GitHub con la URL cruda del archivo (`https://raw.githubusercontent.com/pf0953-programacionr/2026-ii/main/datos/<archivo>`), como hacen las lecciones.

- Datos de Costa Rica, en este directorio: `cantones.csv`, `cantones.gpkg`, `provincias.gpkg` y `felidos.csv` (secciones II a IV).
- [`natural-earth/`](natural-earth/LEEME.md): países, ciudades, aeropuertos, ríos y lagos del mundo, de Natural Earth (dominio público), y [`banco-mundial/`](banco-mundial/LEEME.md): indicadores del desarrollo mundial por país (CC BY 4.0). Se usan en el capítulo de sf para introducir los datos geoespaciales a escala mundial, donde las consecuencias de elegir un sistema de referencia de coordenadas se ven a simple vista. Cada directorio tiene su LEEME.

## `cantones.csv`

Población y extensión territorial de los 84 cantones de Costa Rica.

| Columna | Descripción |
|---|---|
| `provincia` | Nombre de la provincia |
| `canton` | Nombre del cantón |
| `poblacion` | Población total en 2022 (habitantes) |
| `area_km2` | Extensión territorial (km²) |

**Fuente**: Instituto Nacional de Estadística y Censos (INEC). (2023). *Resultados de la Estimación de Población y Vivienda 2022* [archivo XLSX], cuadros 11 (población) y 12 (extensión territorial). <https://admin.inec.cr/sites/default/files/2023-11/reResultadosEstimacionPoblacionVivienda2022_3.xlsx>

**Método**: el archivo se genera con `generar-cantones.py` (`python3 datos/generar-cantones.py`, requiere el paquete openpyxl), que descarga el XLSX del INEC y extrae las filas de cantón de los cuadros 11 y 12. El INEC publica esos cuadros con la división territorial de 2022, de 82 cantones: Monteverde y Puerto Jiménez —creados como cantones en 2021 a partir de los distritos del mismo nombre de Puntarenas y Golfito, con su misma extensión— figuran todavía como distritos. El script los reclasifica como cantones y resta su población y su área a los cantones de origen, con lo que resultan los 84 cantones actuales; los totales nacionales no cambian (5 044 197 habitantes; 51 146,62 km²). Los cantones se listan en el orden del INEC, con los dos nuevos al final de la provincia de Puntarenas.

**Uso**: el archivo puede leerse directamente desde GitHub, por ejemplo en R:

```r
cantones <- read.csv("https://raw.githubusercontent.com/pf0953-programacionr/2026-ii/main/datos/cantones.csv")
```

Se usa en las lecciones sobre el lenguaje R y se retoma en las de tidyverse, ggplot2 y sf.

## `cantones.gpkg` y `provincias.gpkg`

Polígonos de los 84 cantones y de las 7 provincias de Costa Rica, de la división territorial administrativa del Instituto Geográfico Nacional (IGN), en formato [GeoPackage](https://www.geopackage.org/) (una capa por archivo: `cantones` y `provincias`).

| Columna | Descripción |
|---|---|
| `codigo_provincia` | Código de la provincia (1 a 7) |
| `provincia` | Nombre de la provincia |
| `codigo_canton` | Código del cantón (101 a 706; solo en `cantones.gpkg`) |
| `canton` | Nombre del cantón (solo en `cantones.gpkg`) |
| `geom` | Geometría (multipolígono) |

Las dos capas están en el sistema de referencia de coordenadas oficial de Costa Rica, **CR-SIRGAS / CRTM05 (EPSG:8908)**, con coordenadas en metros, y sus geometrías están **simplificadas** con una tolerancia de 100 m para que los archivos sean pequeños y los mapas se dibujen rápido: sirven para mapas a escala nacional y para los ejercicios del curso, no para mediciones precisas ni para mapas a escala local.

**Fuente**: Instituto Geográfico Nacional (IGN). (s. f.). *Límite cantonal 1:5000* y *Límite provincial 1:5000* [capas WFS `IGN_5_CO:limitecantonal_5k` y `IGN_5_CO:limiteprovincial_5k`]. Sistema Nacional de Información Territorial (SNIT). <https://geos.snitcr.go.cr/be/IGN_5_CO/wfs>

**Método**: los archivos son copias de los preparados para el curso GF-0657 2026-II (<https://github.com/gf0657-programacionsig/2026-ii/tree/main/datos/ign>, programa `preparar-datos.py`) a partir de las copias del WFS del SNIT conservadas en el repositorio del curso TPB-708 2026-I: reproyección de CR05 / CRTM05 (EPSG:5367, el sistema en que el SNIT publica las capas) a CR-SIRGAS / CRTM05 (EPSG:8908), selección y renombramiento de columnas y simplificación de las geometrías (100 m, con preservación de la topología). Los 84 cantones incluyen Monteverde (612) y Puerto Jiménez (613).

**Advertencias**:

- Dos cantones tienen nombres distintos en el IGN y en el INEC (`cantones.csv`): «Vázquez de Coronado» (IGN) y «Vásquez de Coronado» (INEC); «León Cortés Castro» (IGN) y «León Cortés» (INEC). Las lecciones corrigen los nombres antes de unir las dos fuentes; es un ejemplo de por qué conviene unir por códigos, cuando existen, y no por nombres.
- El área de los polígonos coincide con la del INEC, con diferencias de hasta 1 km² por la simplificación, salvo en el cantón de Puntarenas: la capa del IGN incluye la Isla del Coco (unos 24 km²) y la cifra del INEC no.

**Uso** en R, con el paquete sf:

```r
cantones <- sf::st_read("https://raw.githubusercontent.com/pf0953-programacionr/2026-ii/main/datos/cantones.gpkg")
```

## `felidos.csv`

Registros de presencia de félidos silvestres (familia Felidae) en Costa Rica, con coordenadas, descargados de la [Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://www.gbif.org/).

| Columna | Descripción |
|---|---|
| `gbifID` | Identificador del registro en GBIF |
| `species` | Nombre científico de la especie |
| `basisOfRecord` | Tipo de registro (`HUMAN_OBSERVATION`, `PRESERVED_SPECIMEN`, …) |
| `eventDate` | Fecha del registro (AAAA-MM-DD; puede faltar) |
| `year` | Año del registro (puede faltar) |
| `stateProvince` | Provincia, tal como la anotó quien publicó el registro (puede faltar o estar escrita de distintas formas) |
| `locality` | Localidad, en texto libre (suele faltar) |
| `decimalLongitude` | Longitud en grados decimales (WGS84) |
| `decimalLatitude` | Latitud en grados decimales (WGS84) |

**Fuente**: GBIF.org. (11 de octubre de 2026). *GBIF occurrence search: Felidae, Costa Rica, with coordinates, without geospatial issues* [consulta a la API]. <https://www.gbif.org/occurrence/search?country=CR&taxon_key=9703&has_coordinate=true&has_geospatial_issue=false>

**Método**: el archivo se genera con `generar-felidos.R` (`Rscript datos/generar-felidos.R`, requiere rgbif, dplyr y readr), que consulta la API de GBIF como en el ejemplo de la semana 1 y conserva los registros con coordenadas y sin problemas geoespaciales. Se excluyen las observaciones automáticas (`MACHINE_OBSERVATION`: miles de fotografías de cámaras trampa, casi todas de jaguar y concentradas en unos pocos sitios) y el gato doméstico (*Felis catus*). La versión del repositorio corresponde a la consulta del 11 de octubre de 2026: 1 041 registros de seis especies (puma, manigordo, jaguar, caucel, león breñero y tigrillo). Como GBIF recibe registros nuevos continuamente, volver a ejecutar el script da un resultado distinto.

**Uso**: las coordenadas están en WGS84 (EPSG:4326); el archivo se convierte en un objeto sf con `st_as_sf(coords = c("decimalLongitude", "decimalLatitude"), crs = 4326)`. Los registros de GBIF tienen licencias Creative Commons (CC0, CC BY o CC BY-NC) según el conjunto de datos de origen; para usarlos fuera del curso, descargue los datos desde GBIF y cite el DOI de la descarga.
