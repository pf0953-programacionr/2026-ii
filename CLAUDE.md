# PF-0953 Programación en R, 2026-II

Curso del Programa de Posgrado en Geografía (SEP-UCR). Profesor: Manuel Vargas Del Valle.

## Datos del curso

- Grupo 001, jueves 17:00-19:50 (J 17-18-19), 3 créditos. Curso completamente virtual (indicación de la coordinación de la maestría, agosto de 2026): sesiones sincrónicas por videoconferencia en el horario del curso (sin mencionar una aplicación específica en el programa), enlaces en Mediación Virtual.
- Horario de atención: J 14-15-16 (14:00 a 16:50).
- II ciclo 2026: lecciones del 10 de agosto al 28 de noviembre; exámenes finales del 30 de noviembre al 5 de diciembre (Circular VD-43-2026). Ningún jueves se pierde por feriados: 16 sesiones (13 de agosto al 26 de noviembre).
- Evaluación 50/50 (sin exámenes cortos, por la virtualidad total): 3 tareas (15 + 15 + 20 %, semanas 5, 10 y 14, aproximaciones incrementales al proyecto), proyecto final (aplicación shiny 25 % + presentación oral sincrónica 10 % en semana 16 + documento computacional Quarto estilo artículo 15 % en semana de exámenes). El programa habla de tema elegido por cada estudiante, sin mencionar trabajo en parejas (Manuel decidirá después si lo permite).
- Sitio web (pendiente de desarrollar, en Quarto): https://pf0953-programacionr.github.io/2026-ii/

## Estructura del repositorio

- `programa/programa.md`: fuente de la verdad del programa del curso. También se renderiza como página del sitio web (`programa/_metadata.yml` fija su `pagetitle`; el archivo no lleva encabezado YAML porque es la fuente del DOCX/PDF), enlazada como primer elemento de la barra lateral («Programa del curso»).
- `programa/generar.sh`: genera DOCX y PDF (`pf0953-programacionr-g001-2026-ii.*`, versionados).
- `_quarto.yml`, `index.qmd`, `contenidos/`, `estilos.scss`: sitio web del curso en Quarto (ver sección "Sitio web").
- `datos/`: conjuntos de datos de las lecciones y ejercicios, con README y scripts de generación. `cantones.csv` (84 cantones: provincia, población 2022 y área, derivado del XLSX del INEC por `generar-cantones.py`, que reclasifica Monteverde y Puerto Jiménez, aún distritos en el archivo del INEC). Las lecciones lo leen por URL cruda de GitHub (`raw.githubusercontent.com/.../main/datos/cantones.csv`), por lo que un dato nuevo debe fusionarse a `main` antes de renderizar la lección que lo usa.
- `Dockerfile`: entorno de autoría/render del profesor (rocker/geospatial y paquetes adicionales con versiones fijas —decisión de Manuel: actualizarlas es un commit explícito—, RStudio Server en el puerto 8787, clave `pf0953`). No es para estudiantes (ellos instalan R/RStudio directamente).
- `privado/`: NO versionado (.gitignore). Contiene `calificaciones/`, `documentos-recibidos/` (nombramiento, circulares, listas de clase, programas de referencia de otros cursos) y `guias/` (guías operativas del profesor, p. ej. la de la VM de Windows para la demo).

## Sitio web

Sitio Quarto tipo *website* publicado en GitHub Pages **desde `docs/` en `main`** (sin GitHub Actions, como en GF-0604 2026-I). `execute: freeze: auto`: el código R se ejecuta una vez localmente y `_freeze/` se versiona.

```bash
# Construir la imagen (una vez, o al cambiar el Dockerfile)
docker build --pull -t pf0953-2026-ii .

# Renderizar el sitio (ejecuta el código R; requiere red para la API de GBIF)
docker run --rm -u $(id -u):$(id -g) -e HOME=/tmp -v "$PWD":/work -w /work pf0953-2026-ii quarto render

# RStudio Server para autoría interactiva
docker run -d --name pf0953-2026-ii -p 8787:8787 -v "$PWD":/home/rstudio pf0953-2026-ii
```

- Contenidos en `contenidos/<sección>/<nn>-<tema>.qmd`, una sección por parte del cronograma (I a V), adaptados de GF-0657 2026-II (repo `gf0657-programacionsig/2026-ii`, MyST, licencia CC BY-SA 4.0; hay que convertir directivas MyST y traducir el código de Python a R) — Manuel prefiere esos contenidos sobre los de GF-0604 2026-I.
- El ejemplo de la semana 1 (`02-ejemplo-procesos-ciencia-datos.qmd`) consulta la API de GBIF al renderizar; el "clic y ejecutá" del estudiantado es el proyecto de Posit Cloud https://posit.cloud/content/12735309 (proyecto "2026-ii" en la cuenta de Manuel —login con Google—, clonado del repo, con rgbif/tidyverse/plotly/leaflet instalados, acceso "All Posit Cloud Users": cada estudiante abre una copia temporal y la guarda en su cuenta gratuita). El enlace se comparte por Mediación Virtual, no está en el sitio. Para actualizar el proyecto con contenidos nuevos: git pull desde el propio proyecto.
- No mencionar una aplicación específica de videoconferencia (decisión de Manuel).
- Identidad visual en `estilos.scss` (azul UCR `#005da4`, verde SEP `#4f7d3a`). Marca del curso en `marca/` (misma familia que la brújula-serpiente de GF-0657): brújula con anillo verde SEP y N, y una R monolínea en azul UCR cuya pata es la aguja con punta roja. `logo-general.svg/png` (independiente de la edición, para la organización en GitHub), `logo-2026-ii.svg/png` (con la pastilla de la edición) y `marca-favicon.svg` (solo la R-aguja). `logo.svg` y `logo-oscuro.svg` en la raíz son las versiones horizontales para la cabecera del sitio (temas claro y oscuro). Estructura del sitio como la de GF-0657: barra superior (`navbar`) con el logo a la izquierda y el buscador y el conmutador claro/oscuro a la derecha (botón circular sol/luna restilizado en `estilos.scss` con la fuente de Bootstrap Icons; Quarto los genera en otro orden y `estilos.scss` los reordena con `order`), y barra lateral con los contenidos debajo. Tema claro (predeterminado) y oscuro: `estilos-oscuro.scss` solo redefine la paleta (variables `!default` de `estilos.scss` y de Bootstrap); para probar el modo oscuro sin navegador interactivo, fijar `localStorage["quarto-color-scheme"] = "alternate"` antes de cargar la página.

## Generación del programa

```bash
bash programa/generar.sh
```

Flujo: `programa.md` → pandoc (gfm→html→docx, por los `<br>` en las celdas de las tablas) → `postprocesar.py` → LibreOffice PDF. Dependencias: pandoc (`~/miniconda3/bin/pandoc`, configurable con `$PANDOC`), python3 y libreoffice.

`referencia.docx` (no versionado) se regenera automáticamente con `generar-referencia.py` a partir de `privado/documentos-recibidos/pf0953-programacionr-g001-2024-ii.docx` (formato del SEP: logo UCR arriba-izquierda, formas verdes, pies sin texto) + `logo-sep.png` en la esquina superior derecha. Trampas conocidas:

- La base llama "Body Text" al styleId `TextBody`; pandoc usa `BodyText`. `generar-referencia.py` crea alias de estilos para que `FirstParagraph`/`Compact` no pierdan la herencia (sin esto, salen a 10 pt en lugar de 12 pt).
- LibreOffice interpreta los `posOffset` con `relativeFrom="page"` del logo del SEP desde el origen del área de texto (margen izquierdo, margen del encabezado), no desde el borde de la hoja; `generar-referencia.py` compensa restando esos márgenes. El logo de la UCR queda a distinta altura en la primera página (header2) que en las siguientes (header1), por lo que `logo_y()` usa un valor calibrado por encabezado (centros medidos en el PDF a 100 dpi: 53 px y 79 px). El logo del SEP lleva el mismo ancho que el de la UCR (1 819 275 EMU) y se centra verticalmente respecto a él.
- `postprocesar.py` está acoplado al texto del programa: espera exactamente 3 tablas (contenidos + 2 de evaluación) y los marcadores "PROGRAMA DEL CURSO", "6. BIBLIOGRAFÍA", "Profesor:", "II ciclo lectivo 2026", "Fecha de entrega o realización". Revisarlo si cambian secciones o tablas.
- Verificación: convertir el PDF con `pdftoppm -png -r 60` e inspeccionar logos, pies de página, tablas y numeración de listas.

## Convenciones

Las convenciones del repositorio (mensajes de commit, flujo de ramas y pull requests, estructura y estilo de los capítulos, formato APA 7) están documentadas en `CONTRIBUTING.md`, que además sirve como material de referencia para el curso. En resumen:

- Todo cambio se hace en una rama y se integra mediante pull request.
- Mensajes de commit en español, en tercera persona ("Agrega…", "Corrige…"), con título de máximo 72 caracteres.
- Bibliografía en APA 7 en español (apellidos e iniciales, «y» antes del último autor, "Recuperado el … de" solo en fuentes sin edición/versión). Excepción: en la tabla del cronograma las citas llevan nombres completos ("Garret Grolemund (2014, capítulos 1 al 8)").

## Estado y fases pendientes

- Programa del curso: primera versión mergeada a `main` (PR #1, agosto de 2026), adaptada a la modalidad completamente virtual. Decisiones cerradas: la adscripción menciona el Posgrado en Geografía y la Maestría en GIRH, 3 créditos confirmados por Manuel, *Geocomputation with R* citado como 2.ª ed. (2025, verificado con CRC Press). Trabajo en parejas: pendiente de decisión (por ahora el programa no lo menciona).
- Sitio web del curso en Quarto: publicado en https://pf0953-programacionr.github.io/2026-ii/ (GitHub Pages desde `docs/` en `main`). Semanas 1 y 2 completas (PRs #3 y #6): lecciones adaptadas de GF-0657 2026-II más la sección Software con la guía de R y RStudio (`software/r-rstudio.qmd`; renombrada desde `rstudio.qmd` el 26 de agosto de 2026: el enlace de la semana 2 en Mediación Virtual debe apuntar a `contenidos/software/r-rstudio.html`). Marca integrada (favicon, logo, logos institucionales, modo oscuro; PRs #14 y #15). Sección II (R): capítulos 06 «Introducción a R» (lectura previa: en clase solo «Ejecución de R en el curso» y el ejercicio del proyecto `pf0953`) y 07 «Fundamentos de R I» (semana 3) en `contenidos/ii-lenguaje-programacion-r/`, con el hilo conductor de `datos/cantones.csv`; y 08 «Fundamentos de R II» (semana 4: condicionales, ciclos, factores y listas, funciones). El 07 se aligeró el 27 de agosto de 2026: factores y listas pasaron al 08, «Tipos de datos» quedó como subsección de «Vectores», la clínica de errores es una tabla (mensaje → causa → solución; los errores se provocan en vivo en clase) y los ejercicios bajaron de 12 a 7. Diseño de la sección: dos sesiones cortas, ejercicios breves por sección (sin celdas de verificación), «prediga antes de ejecutar» con `<details>`, clínica de errores; soluciones en `privado/soluciones-ejercicios/`. Falta: semana 5 en adelante (Quarto, tidyverse…), adaptando GF-0657 2026-II y GF-0604 2026-I. Software de estudiantes: instalación directa de R/RStudio, Posit Cloud como respaldo.
- Entorno virtual en Mediación Virtual (Moodle 4.5, curso id 16311): armado en agosto de 2026 con el encabezado según VD-12784-2023, el PDF del programa, el enlace de Zoom y, por semana, los enlaces a las lecciones del sitio, el video de la clase, el proyecto de Posit Cloud (semana 1) y la guía de R y RStudio (semana 2). Falta: entregas (la tarea 1 es en la semana 5) y libro de calificaciones. Consultas solo por soporte.metics@ucr.ac.cr (3 días hábiles de gestión).
- Demo de instalación de R/RStudio en Windows para el estudiantado (que usa Windows; la máquina del profesor es Linux): lista y ensayada (20 de agosto de 2026). Windows 11 en Docker con [dockur/windows](https://github.com/dockur/windows): contenedor `windows` (en inglés, sin activar, 8 GB RAM y 4 núcleos, volumen `windows-data`), visor en el navegador en http://localhost:8006. El disco recién instalado (sin R) está respaldado en el volumen `windows-data-clean`; para restaurar el estado limpio antes o después de una demo: `docker stop windows && docker run --rm -v windows-data-clean:/src -v windows-data:/dst debian:stable-slim bash -c 'rm -rf /dst/* && cp -a --sparse=always /src/. /dst/' && docker start windows` (arranca en ~20 s). La VM tiene el teclado US-International como predeterminado (más el US normal), igual que el Linux de Manuel (27 de agosto de 2026); el respaldo limpio no lo incluye, así que tras restaurar hay que reaplicarlo (comandos en `privado/guias/guia-vm-windows.md`). El ensayo validó el flujo de la guía del sitio: R 4.6.1 desde CRAN y RStudio Desktop 2026.08.1 desde Posit, sin trabas de UAC ni SmartScreen en la VM (en máquinas reales de estudiantes pueden aparecer); reveló además que `posit.co/download/rstudio-desktop` ya no detecta el sistema operativo y redirige a la guía de usuario en docs.posit.co (corregido en la guía, PR #9).
