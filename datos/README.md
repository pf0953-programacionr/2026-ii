# Datos del curso

Conjuntos de datos que se usan en las lecciones y en los ejercicios del curso.

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
