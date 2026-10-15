"""Prepara las capas de Natural Earth que usa el curso.

Descarga los archivos originales (ZIP con Shapefile) del CDN de Natural Earth
y escribe, en EPSG:4326 y con nombres de columnas en español:

- paises.gpkg: países a escala 1:110 M (177 polígonos).
- centroamerica.gpkg: los 7 países de Centroamérica (de Guatemala a Panamá)
  a escala 1:10 M, para mapas a escala regional. Se excluyen México y la
  Isla Clipperton, que Natural Earth incluye en la subregión.
- ciudades.csv: ciudades principales a escala 1:110 M (243), como tabla con
  longitud y latitud.
- aeropuertos.gpkg: aeropuertos a escala 1:10 M (893 puntos).
- rios.gpkg y lagos.gpkg: ríos (líneas) y lagos (polígonos) a 1:110 M.

Uso: python3 preparar-datos.py (requiere geopandas; ejecutar en datos/natural-earth/).
"""

import io
import urllib.request

import geopandas as gpd

CDN = "https://naciscdn.org/naturalearth"

CONTINENTES = {
    "Africa": "África", "Asia": "Asia", "Europe": "Europa", "North America": "América del Norte",
    "South America": "América del Sur", "Oceania": "Oceanía", "Antarctica": "Antártida",
    "Seven seas (open ocean)": "Siete mares (océano abierto)"
}

# Subregiones según el esquema geográfico de la ONU (M49), en español
SUBREGIONES = {
    "Antarctica": "Antártida", "Australia and New Zealand": "Australia y Nueva Zelanda",
    "Caribbean": "Caribe", "Central America": "América Central", "Central Asia": "Asia central",
    "Eastern Africa": "África oriental", "Eastern Asia": "Asia oriental", "Eastern Europe": "Europa oriental",
    "Melanesia": "Melanesia", "Micronesia": "Micronesia", "Polynesia": "Polinesia", "Middle Africa": "África central", "Northern Africa": "África septentrional",
    "Northern America": "América septentrional", "Northern Europe": "Europa septentrional",
    "Seven seas (open ocean)": "Siete mares (océano abierto)", "South America": "América del Sur",
    "South-Eastern Asia": "Asia sudoriental", "Southern Africa": "África austral",
    "Southern Asia": "Asia meridional", "Southern Europe": "Europa meridional",
    "Western Africa": "África occidental", "Western Asia": "Asia occidental", "Western Europe": "Europa occidental"
}

GRUPOS_INGRESO = {
    "1. High income: OECD": "1. Ingreso alto: OCDE", "2. High income: nonOECD": "2. Ingreso alto: no OCDE",
    "3. Upper middle income": "3. Ingreso mediano alto", "4. Lower middle income": "4. Ingreso mediano bajo",
    "5. Low income": "5. Ingreso bajo", "-99": None  # sin dato en Natural Earth
}


def leer(ruta):
    """Lee una capa de Natural Earth a partir de su ruta en el CDN (sin .zip)."""
    with urllib.request.urlopen(f"{CDN}/{ruta}.zip") as respuesta:
        return gpd.read_file(io.BytesIO(respuesta.read()))


def paises_es(capa):
    capa = capa.rename(columns={
        "ADM0_A3": "codigo", "ISO_A3": "iso3", "NAME_ES": "nombre", "NAME": "nombre_en",
        "CONTINENT": "continente", "SUBREGION": "subregion", "POP_EST": "poblacion_estimada",
        "GDP_MD": "pib_millones", "INCOME_GRP": "grupo_ingreso"
    })
    capa["continente"] = capa["continente"].map(CONTINENTES)
    capa["subregion"] = capa["subregion"].map(SUBREGIONES)
    capa["grupo_ingreso"] = capa["grupo_ingreso"].map(GRUPOS_INGRESO)
    assert capa[["continente", "subregion"]].notna().all().all(), "valor sin traducción"
    capa["poblacion_estimada"] = capa["poblacion_estimada"].round().astype("int64")
    return capa[["codigo", "iso3", "nombre", "nombre_en", "continente", "subregion",
                 "poblacion_estimada", "pib_millones", "grupo_ingreso", "geometry"]]


# Países 1:110 M
paises = paises_es(leer("110m/cultural/ne_110m_admin_0_countries"))
paises.to_file("paises.gpkg", driver="GPKG")
print("paises.gpkg:", paises.shape)

# Centroamérica 1:10 M
paises_10m = paises_es(leer("10m/cultural/ne_10m_admin_0_countries"))
# Natural Earth sigue el esquema M49 de la ONU, que incluye a México en América Central; el curso usa
# la acepción de Centroamérica como los siete países entre Guatemala y Panamá.
centroamerica = paises_10m[(paises_10m["subregion"] == "América Central") & ~paises_10m["nombre"].isin(["México", "Isla Clipperton"])]
assert len(centroamerica) == 7, sorted(centroamerica["nombre"])
centroamerica.to_file("centroamerica.gpkg", driver="GPKG")
print("centroamerica.gpkg:", centroamerica.shape, sorted(centroamerica["nombre"]))

# Ciudades 1:110 M, como tabla con coordenadas
ciudades = leer("110m/cultural/ne_110m_populated_places_simple")
ciudades = ciudades.rename(columns={
    "name": "nombre", "adm0name": "pais", "adm0_a3": "codigo_pais", "adm0cap": "capital",
    "pop_max": "poblacion", "longitude": "longitud", "latitude": "latitud"
})
ciudades["capital"] = ciudades["capital"] == 1
ciudades = ciudades[["nombre", "pais", "codigo_pais", "capital", "poblacion", "longitud", "latitud"]]
ciudades.to_csv("ciudades.csv", index=False)
print("ciudades.csv:", ciudades.shape)

# Aeropuertos 1:10 M
aeropuertos = leer("10m/cultural/ne_10m_airports")
aeropuertos = aeropuertos.rename(columns={"name": "nombre", "type": "tipo", "iata_code": "iata"})
aeropuertos = aeropuertos[["nombre", "tipo", "iata", "geometry"]]
aeropuertos.to_file("aeropuertos.gpkg", driver="GPKG")
print("aeropuertos.gpkg:", aeropuertos.shape)

# Ríos y lagos 1:110 M
rios = leer("110m/physical/ne_110m_rivers_lake_centerlines").rename(columns={"name": "nombre"})
rios[["nombre", "geometry"]].to_file("rios.gpkg", driver="GPKG")
lagos = leer("110m/physical/ne_110m_lakes").rename(columns={"name": "nombre"})
lagos[["nombre", "geometry"]].to_file("lagos.gpkg", driver="GPKG")
print("rios.gpkg:", rios.shape, "lagos.gpkg:", lagos.shape)
