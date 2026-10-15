# Datos de Natural Earth

> Estos archivos son copias de los preparados para el curso GF-0657 2026-II (<https://github.com/gf0657-programacionsig/2026-ii/tree/main/datos/natural-earth>), con el mismo programa `preparar-datos.py` (requiere Python con geopandas o pandas; no hace falta ejecutarlo para usar los datos).

Fuente: [Natural Earth](https://www.naturalearthdata.com/), un conjunto de
datos cartográficos de dominio público a escalas 1:10 M, 1:50 M y
1:110 M, mantenido por la North American Cartographic Information Society
(NACIS). Los archivos originales (Shapefile comprimidos) se descargan del
CDN de Natural Earth (https://naciscdn.org/naturalearth/) con el programa
`preparar-datos.py` (requiere geopandas), que escribe las capas de este
directorio en WGS84 (EPSG:4326) y con nombres de columnas en español.

## Archivos

- `paises.gpkg` (177 polígonos, escala 1:110 M): `codigo` (código de tres
  letras de Natural Earth, `ADM0_A3`), `iso3` (código ISO 3166-1 alfa-3,
  `ISO_A3`; es `-99` en Francia, Noruega, Kosovo, Somalilandia y el norte
  de Chipre), `nombre` (en español), `nombre_en`, `continente` (en
  español), `subregion` (según el esquema geográfico de la ONU, en español),
  `poblacion_estimada`
  (estimación de Natural Earth, 2019), `pib_millones` (PIB en millones de
  dólares, 2019) y `grupo_ingreso` (cinco grupos, en español). Los nombres de
  las columnas y los valores de continente, subregión y grupo de ingreso se
  traducen en el script; los nombres de los países vienen en español de la
  propia fuente (`NAME_ES`).
- `centroamerica.gpkg` (7 polígonos, escala 1:10 M): los países de
  Centroamérica (Guatemala, Belice, Honduras, El Salvador, Nicaragua,
  Costa Rica y Panamá), con las mismas columnas, para mapas a escala
  regional en los que la escala 1:110 M es demasiado gruesa. Natural Earth
  incluye a México en la subregión "América Central", según el esquema
  geográfico de la ONU; aquí se excluye.
- `ciudades.csv` (243 filas, escala 1:110 M): ciudades principales del
  mundo, casi todas capitales, como tabla con `nombre`, `pais`,
  `codigo_pais`, `capital` (verdadero o falso), `poblacion` y las
  coordenadas `longitud` y `latitud` en WGS84.
- `aeropuertos.gpkg` (893 puntos, escala 1:10 M): `nombre`, `tipo` y
  código `iata`.
- `rios.gpkg` (13 líneas) y `lagos.gpkg` (24 polígonos), escala 1:110 M:
  `nombre`.

## Advertencias

- Los códigos de país de Natural Earth (`codigo`) coinciden casi siempre
  con los del Banco Mundial en `../banco-mundial/`, con tres excepciones:
  Kosovo (`KOS` en Natural Earth, `XKX` en el Banco Mundial), Palestina
  (`PSX` / `PSE`) y Sudán del Sur (`SDS` / `SSD`). Otros siete territorios
  de Natural Earth no existen en el Banco Mundial (Antártida, Tierras
  Australes Francesas, Islas Malvinas, norte de Chipre, Sahara Occidental,
  Somalilandia y Taiwán) y 50 países o territorios del Banco Mundial no
  tienen polígono a 1:110 M (en su mayoría islas pequeñas, como Singapur,
  Hong Kong, Bahréin o Mauricio).
- La escala 1:110 M es adecuada para mapas del mundo o de un continente;
  los países pequeños están muy simplificados o ausentes. Para mapas de
  un país o una región se usa `centroamerica.gpkg` (1:10 M) o se descarga
  la capa correspondiente de Natural Earth.
