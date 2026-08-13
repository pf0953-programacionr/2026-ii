# PF-0953 Programación en R, 2026-II

Curso del Programa de Posgrado en Geografía (SEP-UCR). Profesor: Manuel Vargas Del Valle.

## Datos del curso

- Grupo 001, jueves 17:00-19:50 (J 17-18-19), 3 créditos. Curso completamente virtual (indicación de la coordinación de la maestría, agosto de 2026): sesiones sincrónicas por videoconferencia en el horario del curso (sin mencionar una aplicación específica en el programa), enlaces en Mediación Virtual.
- Horario de atención: J 14-15-16 (14:00 a 16:50).
- II ciclo 2026: lecciones del 10 de agosto al 28 de noviembre; exámenes finales del 30 de noviembre al 5 de diciembre (Circular VD-43-2026). Ningún jueves se pierde por feriados: 16 sesiones (13 de agosto al 26 de noviembre).
- Evaluación 50/50 (sin exámenes cortos, por la virtualidad total): 3 tareas (15 + 15 + 20 %, semanas 5, 10 y 14, aproximaciones incrementales al proyecto), proyecto final (aplicación shiny 25 % + presentación oral sincrónica 10 % en semana 16 + documento computacional Quarto estilo artículo 15 % en semana de exámenes). El programa habla de tema elegido por cada estudiante, sin mencionar trabajo en parejas (Manuel decidirá después si lo permite).
- Sitio web (pendiente de desarrollar, en Quarto): https://pf0953-programacionr.github.io/2026-ii/

## Estructura del repositorio

- `programa/programa.md`: fuente de la verdad del programa del curso.
- `programa/generar.sh`: genera DOCX y PDF (`pf0953-programacionr-g001-2026-ii.*`, versionados).
- `_quarto.yml`, `index.qmd`, `contenidos/`, `estilos.scss`: sitio web del curso en Quarto (ver sección "Sitio web").
- `Dockerfile`: entorno de autoría/render del profesor (rocker/geospatial y paquetes adicionales con versiones fijas —decisión de Manuel: actualizarlas es un commit explícito—, RStudio Server en el puerto 8787, clave `pf0953`). No es para estudiantes (ellos instalan R/RStudio directamente).
- `privado/`: NO versionado (.gitignore). Contiene `calificaciones/` y `documentos-recibidos/` (nombramiento, circulares, listas de clase, programas de referencia de otros cursos).

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
- El ejemplo de la semana 1 (`02-ejemplo-procesos-ciencia-datos.qmd`) consulta la API de GBIF al renderizar; el "clic y ejecutá" del estudiantado es Posit Cloud (el proyecto lo crea Manuel; el enlace se comparte por Mediación Virtual).
- No mencionar una aplicación específica de videoconferencia (decisión de Manuel).
- Identidad visual en `estilos.scss` (azul UCR `#005da4`, verde SEP `#4f7d3a`). Logo del curso: pendiente de crear.

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

- Todo cambio se hace en una rama y se integra mediante pull request.
- Mensajes de commit en español, en tercera persona ("Agrega…", "Corrige…").
- Bibliografía en APA 7 en español (apellidos e iniciales, «y» antes del último autor, "Recuperado el … de" solo en fuentes sin edición/versión). Excepción: en la tabla del cronograma las citas llevan nombres completos ("Garret Grolemund (2014, capítulos 1 al 8)").

## Estado y fases pendientes

- Programa del curso: primera versión mergeada a `main` (PR #1, agosto de 2026), adaptada a la modalidad completamente virtual. Decisiones cerradas: la adscripción menciona el Posgrado en Geografía y la Maestría en GIRH, 3 créditos confirmados por Manuel, *Geocomputation with R* citado como 2.ª ed. (2025, verificado con CRC Press). Trabajo en parejas: pendiente de decisión (por ahora el programa no lo menciona).
- Sitio web del curso en Quarto: andamiaje y semana 1 en la rama `sitio-web` (PR pendiente). Falta: habilitar GitHub Pages (main, `/docs`), logo del curso, proyecto de Posit Cloud para el ejemplo de la semana 1, y las semanas siguientes (lección por lección, adaptando GF-0657 2026-II). Software de estudiantes: instalación directa de R/RStudio, Posit Cloud como respaldo.
- Entorno virtual en Mediación Virtual (Moodle 4.5): encabezado según VD-12784-2023 (sigla, nombre, grupo, modalidad, ciclo, docente, grado de virtualidad "virtual", descripción, horario de consulta, medios de contacto), subir el PDF del programa, enlaces a las páginas del sitio, entregas y libro de calificaciones. Investigar automatización; consultas solo por soporte.metics@ucr.ac.cr (3 días hábiles de gestión).
