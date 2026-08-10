# PF-0953 Programación en R, 2026-II

Curso del Programa de Posgrado en Geografía (SEP-UCR). Profesor: Manuel Vargas Del Valle.

## Datos del curso

- Grupo 001, jueves 17:00-19:50 (J 17-18-19), aula 213, 3 créditos.
- Horario de atención: J 14-15-16 (14:00 a 16:50).
- II ciclo 2026: lecciones del 10 de agosto al 28 de noviembre; exámenes finales del 30 de noviembre al 5 de diciembre (Circular VD-43-2026). Ningún jueves se pierde por feriados: 16 sesiones (13 de agosto al 26 de noviembre).
- Evaluación 25/40/35: 5 exámenes cortos (5 % c/u, semanas 3, 6, 9, 13 y 16), 3 tareas (10 + 15 + 15 %, semanas 4, 10 y 14, aproximaciones incrementales al proyecto), proyecto final (aplicación shiny 20 % + presentación oral 5 % en semana 16 + documento computacional Quarto estilo artículo 10 % en semana de exámenes). Tema elegido individualmente o en parejas.
- Sitio web (pendiente de desarrollar, en Quarto): https://pf0953-programacionr.github.io/2026-ii/

## Estructura del repositorio

- `programa/programa.md`: fuente de la verdad del programa del curso.
- `programa/generar.sh`: genera DOCX y PDF (`pf0953-programacionr-g001-2026-ii.*`, versionados).
- `privado/`: NO versionado (.gitignore). Contiene `calificaciones/` y `documentos-recibidos/` (nombramiento, circulares, listas de clase, programas de referencia de otros cursos).

## Generación del programa

```bash
bash programa/generar.sh
```

Flujo: `programa.md` → pandoc (gfm→html→docx, por los `<br>` en las celdas de las tablas) → `postprocesar.py` → LibreOffice PDF. Dependencias: pandoc (`~/miniconda3/bin/pandoc`, configurable con `$PANDOC`), python3 y libreoffice.

`referencia.docx` (no versionado) se regenera automáticamente con `generar-referencia.py` a partir de `privado/documentos-recibidos/pf0953-programacionr-g001-2024-ii.docx` (formato del SEP: logo UCR arriba-izquierda, formas verdes, pies sin texto) + `logo-sep.png` en la esquina superior derecha. Trampas conocidas:

- La base llama "Body Text" al styleId `TextBody`; pandoc usa `BodyText`. `generar-referencia.py` crea alias de estilos para que `FirstParagraph`/`Compact` no pierdan la herencia (sin esto, salen a 10 pt en lugar de 12 pt).
- LibreOffice interpreta los `posOffset` con `relativeFrom="page"` del logo del SEP desde el origen del área de texto (margen izquierdo, margen del encabezado), no desde el borde de la hoja; `generar-referencia.py` compensa restando esos márgenes. El logo de la UCR queda a distinta altura en la primera página (header2) que en las siguientes (header1), por lo que `logo_y()` usa un valor calibrado por encabezado (centros medidos en el PDF a 100 dpi: 53 px y 79 px). El logo del SEP lleva el mismo ancho que el de la UCR (1 819 275 EMU) y se centra verticalmente respecto a él.
- `postprocesar.py` está acoplado al texto del programa: espera exactamente 4 tablas (contenidos + 3 de evaluación) y los marcadores "PROGRAMA DEL CURSO", "6. BIBLIOGRAFÍA", "Profesor:", "II ciclo lectivo 2026", "Fecha de entrega o realización". Revisarlo si cambian secciones o tablas.
- Verificación: convertir el PDF con `pdftoppm -png -r 60` e inspeccionar logos, pies de página, tablas y numeración de listas.

## Convenciones

- Todo cambio se hace en una rama y se integra mediante pull request.
- Mensajes de commit en español, en tercera persona ("Agrega…", "Corrige…").
- Bibliografía en APA 7 en español (apellidos e iniciales, «y» antes del último autor, "Recuperado el … de" solo en fuentes sin edición/versión). Excepción: en la tabla del cronograma las citas llevan nombres completos ("Garret Grolemund (2014, capítulos 1 al 8)").

## Estado y fases pendientes

- PR #1 (rama `programa-curso`): primera versión del programa, pendiente de revisión de Manuel. Puntos abiertos: adscripción (¿mencionar la Maestría en GIRH como en 2024?), confirmar 3 créditos, confirmar año/edición de *Geocomputation with R* (2.ª ed., 2025), tabla de exámenes cortos partida entre páginas 7-8.
- Sitio web del curso en Quarto (mismo repo, GitHub Actions → GitHub Pages), con logo del curso por crear y vinculación visual con la UCR y el SEP. Contenidos incrementales (lección por lección). Software de estudiantes: instalación directa de R/RStudio, Posit Cloud como respaldo.
- Entorno virtual en Mediación Virtual (Moodle 4.5): encabezado según VD-12784-2023 (sigla, nombre, grupo, modalidad, ciclo, docente, grado de virtualidad "presencial", descripción, horario de consulta, medios de contacto), subir el PDF del programa, enlaces a las páginas del sitio, entregas y libro de calificaciones. Investigar automatización; consultas solo por soporte.metics@ucr.ac.cr (3 días hábiles de gestión).
