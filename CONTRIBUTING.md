# Convenciones del repositorio

Este documento describe las convenciones de Git y de contenido usadas en
este repositorio. Además de mantener el orden del proyecto, sirve como
material de referencia para el curso.

## Mensajes de commit

- El título se redacta en **tercera persona del presente de indicativo**: el
  mensaje describe lo que el commit hace al aplicarse ("[este commit]
  corrige…").

  ```text
  Corrige la posición del logo del SEP en el encabezado
  Agrega los contenidos de la semana 2
  Actualiza la bibliografía del programa
  ```

- Título de unos 50 caracteres (máximo 72), sin punto final y específico
  sobre el cambio ("Actualiza las fechas de las tareas", no "Cambios").
- Cuerpo opcional, separado del título por una línea en blanco, que explica
  el **porqué** del cambio cuando no es obvio. El *qué* ya lo muestra el
  diff; el contexto y la motivación son lo que se pierde si no se escribe.
- Un cambio lógico por commit. Si el mensaje necesita la palabra "y" para
  describir dos cambios sin relación, probablemente son dos commits.
- Cuando un commit se elabora con asistencia de una herramienta de
  inteligencia artificial, se declara con un trailer al final del cuerpo,
  por ejemplo:

  ```text
  Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
  ```

## Flujo de trabajo

- La rama principal es `main` y siempre debe quedar en estado publicable:
  GitHub Pages publica el sitio web directamente desde el directorio
  `docs/` de esta rama.
- Todo cambio se hace en una rama propia y se integra mediante *pull
  request*. El nombre de la rama es corto y descriptivo, en minúsculas y
  con guiones: `contenidos-semana-2`, `dockerfile-version-fija`.

## Renderizado del sitio web

El sitio se genera con [Quarto](https://quarto.org/) dentro de la imagen
Docker del curso (ver `Dockerfile` y las instrucciones de `CLAUDE.md`):

```bash
docker run --rm -u $(id -u):$(id -g) -e HOME=/tmp -v "$PWD":/work -w /work pf0953-2026-ii quarto render
```

- `execute: freeze: auto`: el código R se ejecuta una sola vez y los
  resultados se congelan en `_freeze/`, que se versiona; los render
  posteriores no requieren ejecutar R (ni acceso a las API que consultan
  algunas lecciones).
- El HTML generado en `docs/` se versiona junto con las fuentes, en el
  mismo commit.
- **Atención**: `quarto render` elimina `docs/.nojekyll`; hay que
  restaurarlo (`touch docs/.nojekyll`) antes de confirmar, pues sin él
  GitHub Pages procesa el sitio con Jekyll.
- Las salidas interactivas de R (plotly, leaflet, DT) son *htmlwidgets*
  que Quarto incorpora en el HTML sin tratamiento especial.

## Estructura de los capítulos del sitio web

Todos los capítulos (lecciones `.qmd` en `contenidos/`) siguen la misma
estructura de secciones, en este orden:

1. Título del capítulo en el encabezado YAML (`title:`), no como `#` en el
   cuerpo.
2. `## Trabajo previo` — con subsecciones `### Lecturas` y, si aplica,
   `### Tutoriales`, `### Videos` u otros recursos que deben revisarse
   antes de la clase.
3. `## Introducción` — presentación breve del tema y su motivación.
4. Secciones de contenido (`##`) propias del tema.
5. `## Resumen` — síntesis breve, típicamente en viñetas, de las ideas
   principales del capítulo.
6. `## Ejercicios` — con numeración continua y, cuando el capítulo lo
   amerite, subdividida en subsecciones espejo de las secciones de
   contenido (`### Datos`, `### Sintaxis`, …), con un identificador
   `{#ejercicios-x}` en cada una. Cada sección de contenido cierra
   entonces con una línea `*Ejercicios de esta sección: [...](#ejercicios-x).*`,
   lo que permite intercalar teoría y práctica durante las clases sin
   alterar la estructura del capítulo.
7. `## Referencias bibliográficas` — al final, según la sección
   [Referencias bibliográficas](#referencias-bibliográficas).

Las secciones 2, 5, 6 y 7 pueden omitirse solo cuando no aplican (ej. un
documento de ejemplo sin trabajo previo). Cada capítulo nuevo se agrega a
la barra lateral en `_quarto.yml`, en la sección del cronograma que le
corresponde.

Las guías de la sección Software (`contenidos/software/`) son un género
distinto: instrucciones de instalación, configuración y acceso, con pasos
numerados cuando corresponda, sin la estructura completa de capítulos;
las lecciones remiten a ellas en lugar de repetir instrucciones.

Los enunciados de las evaluaciones (`contenidos/evaluaciones/`, sección
Evaluaciones de la barra lateral) siguen la estructura de los de GF-0657:
párrafo inicial (carácter individual o grupal, valor y propósito), «Fecha
y hora límite de entrega», «Objetivos», «Entregables», «Consideraciones
adicionales», «Desarrollo», «Calificación» (porcentajes por aspecto) y
«Recursos» (enlaces a las lecciones que cubren lo evaluado).

### Estilo

- Los nombres de los paquetes de R se escriben en minúsculas en la prosa
  (tidyverse, plotly, leaflet), como en el programa del curso; los títulos
  de las obras citadas conservan su forma original.
- Las **negritas** destacan cada concepto del capítulo en su primera
  aparición y los términos clave del resumen; no se usan para énfasis.
- Los **hipervínculos** amplían información en la primera mención:
  Wikipedia en español para conceptos auxiliares que el capítulo menciona
  pero no desarrolla, y el sitio oficial para herramientas, organizaciones
  y estándares; los conceptos que el propio capítulo desarrolla no se
  enlazan.
- Los diagramas se escriben como bloques `{mermaid}` dentro del propio
  documento, en el lenguaje de [Mermaid](https://mermaid.js.org/), que
  Quarto renderiza al generar el sitio.
- Las tablas y figuras se numeran consecutivamente dentro de cada capítulo
  (`Tabla 1`, `Figura 1`, …) y llevan leyenda con la fuente. Las tablas en
  HTML se envuelven en `<figure>` con la leyenda en `<figcaption>` antes
  del `<table>`; las celdas con valores numéricos llevan
  `class="align-right"`, definida en la hoja de estilos del sitio
  (`estilos.scss`):

  ```html
  <figure style="text-align: center; margin: 20px 0;">
      <figcaption><strong>Tabla N</strong>. Descripción. Fuente: ...</figcaption>
      <table class="table table-bordered table-striped" style="margin: 0 auto;">
      ...
      </table>
  </figure>
  ```

## Referencias bibliográficas

Todo el material del curso — capítulos del sitio web, pautas de tareas y
del proyecto, evaluaciones — usa el formato **APA 7** con el aparato en
español:

- Apellidos e iniciales de los autores ("Wickham, H."), no nombres
  completos.
- Conjunción «y» antes del último autor, no «&», y sin coma antes de la
  conjunción.
- «En» para capítulos o secciones de una obra mayor.
- Títulos con mayúscula solo en la primera palabra (y en nombres propios),
  en el idioma original de la obra.
- Ediciones en español: «(2.ª ed.)».
- Rangos de páginas con semiraya: «452–454», no «452-454».
- «Recuperado el [fecha]» únicamente en fuentes diseñadas para cambiar y
  sin edición ni versión (ej. sitios de documentación como los citados en
  el programa); las obras con edición, versión o fecha de publicación no
  llevan fecha de recuperación.
- Citas en el texto: «(Autor, año)» o «Autor (año)»; en las leyendas de
  tablas y figuras se usa la forma narrativa («Fuente: Autor (año)»).
- Las URL se escriben entre corchetes angulares (`<https://...>`), con lo
  que Quarto las convierte en enlaces.

Este mismo formato es el que se pide a los estudiantes en las tareas y en
el documento del proyecto final. La única excepción es el **programa del
curso**, cuyo cronograma cita con nombres completos ("Garret Grolemund
(2014, capítulos 1 al 8)") por requerimiento de la plantilla oficial del
SEP.

## Qué no se versiona

- El directorio `privado/` (calificaciones, documentos administrativos
  recibidos) está excluido mediante `.gitignore` y nunca debe publicarse.
- `programa/referencia.docx` se deriva de una plantilla del SEP y se
  regenera localmente; tampoco se versiona.
- Antes de agregar archivos nuevos, verificar que no contengan datos
  personales de estudiantes ni documentos internos del posgrado.
