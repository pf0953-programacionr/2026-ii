"""Descarga indicadores del Banco Mundial (base Indicadores del desarrollo
mundial) mediante su API y escribe:

- indicadores-2024.csv: una fila por país (sin agregados regionales) con los
  indicadores de la tabla INDICADORES para el año ANIO (la superficie
  terrestre, que el Banco Mundial publica con rezago, es la de ANIO_AREA).
- poblacion-1960-2025.csv: población total por país y año, en formato largo.

Uso: python3 preparar-datos.py (requiere pandas; ejecutar en datos/banco-mundial/).
"""

import json
import urllib.request

import pandas as pd

API = "https://api.worldbank.org/v2"
ANIO = 2024
ANIO_AREA = 2023  # último año publicado de AG.LND.TOTL.K2
ANIO_FINAL_SERIE = 2025

INDICADORES = {
    "SP.POP.TOTL": "poblacion",
    "SP.POP.GROW": "crecimiento_poblacion",
    "AG.LND.TOTL.K2": "area_km2",
    "NY.GDP.PCAP.CD": "pib_per_capita",
    "SP.DYN.LE00.IN": "esperanza_vida",
    "SP.URB.TOTL.IN.ZS": "poblacion_urbana_pct",
    "IT.NET.USER.ZS": "usuarios_internet_pct",
}


def consultar(ruta):
    """Retorna la lista de registros de una consulta a la API (todas las páginas en una)."""
    with urllib.request.urlopen(f"{API}/{ruta}&format=json&per_page=20000", timeout=120) as respuesta:
        encabezado, registros = json.load(respuesta)
    assert encabezado["pages"] == 1, encabezado
    return registros


# Países: se excluyen los agregados (regiones, grupos de ingreso)
paises = pd.DataFrame([
    {"codigo": p["id"], "pais": p["name"].strip(), "region": p["region"]["value"].strip(),
     "grupo_ingreso": p["incomeLevel"]["value"].strip()}
    for p in consultar("es/country?") if p["region"]["value"].strip() != "Agregados"
])
print("países:", len(paises))

# Indicadores del año ANIO
tabla = paises.copy()
for codigo, nombre in INDICADORES.items():
    anio = ANIO_AREA if codigo == "AG.LND.TOTL.K2" else ANIO
    valores = pd.DataFrame(consultar(f"country/all/indicator/{codigo}?date={anio}"))
    valores = valores[["countryiso3code", "value"]].rename(columns={"countryiso3code": "codigo", "value": nombre})
    tabla = tabla.merge(valores, on="codigo", how="left")
tabla["poblacion"] = tabla["poblacion"].astype("Int64")
tabla = tabla.round({"crecimiento_poblacion": 2, "pib_per_capita": 1, "esperanza_vida": 1,
                     "poblacion_urbana_pct": 1, "usuarios_internet_pct": 1, "area_km2": 1})
tabla.to_csv(f"indicadores-{ANIO}.csv", index=False)
print(f"indicadores-{ANIO}.csv:", tabla.shape)

# Serie de población
serie = pd.DataFrame(consultar(f"country/all/indicator/SP.POP.TOTL?date=1960:{ANIO_FINAL_SERIE}"))
serie = serie[serie["countryiso3code"].isin(paises["codigo"])]
serie = serie.rename(columns={"countryiso3code": "codigo", "date": "anio", "value": "poblacion"})
serie = serie[["codigo", "anio", "poblacion"]].dropna().sort_values(["codigo", "anio"])
serie["anio"] = serie["anio"].astype(int)
serie["poblacion"] = serie["poblacion"].astype("int64")
serie.to_csv(f"poblacion-1960-{ANIO_FINAL_SERIE}.csv", index=False)
print(f"poblacion-1960-{ANIO_FINAL_SERIE}.csv:", serie.shape)
