# PF-0953 Programación en R

**Profesor: Manuel Vargas Del Valle**

Grupo 001, horario J 17-18-19 (17:00 a 19:50), modalidad virtual, Créditos: 3

Horas totales semanales: 3 horas (laboratorio 3).

Horario de atención al estudiantado: J 14-15-16 (14:00 a 16:50).

Correo electrónico institucional: manuel.vargas_d@ucr.ac.cr

II ciclo lectivo 2026

## PROGRAMA DEL CURSO

### 1. DESCRIPCIÓN

Este curso es una introducción a la programación de computadoras y al procesamiento de datos geoespaciales mediante el lenguaje de programación R. Se estudian los fundamentos del lenguaje, sus paquetes para ciencia de datos y para datos geoespaciales, y las herramientas que facilitan la reproducibilidad de los procedimientos y la comunicación de las soluciones a través de Internet, tanto en documentos computacionales como en aplicaciones interactivas. Además, se incorpora de manera paulatina y crítica el uso de herramientas de inteligencia artificial (IA) como apoyo en los procesos de programación y de análisis de datos. El curso se imparte en el Programa de Posgrado en Geografía del Sistema de Estudios de Posgrado (SEP) de la Universidad de Costa Rica.

El enfoque del curso es teórico-práctico, con lecciones teóricas combinadas con sesiones prácticas de programación en las cuales el estudiantado aplica, en diversos escenarios de procesamiento de datos, los conocimientos aprendidos y las habilidades desarrolladas. A lo largo del curso, cada estudiante desarrolla un tema de su elección mediante tareas que funcionan como aproximaciones incrementales al proyecto final. No se requiere experiencia previa en programación de computadoras; es recomendable contar con conocimientos básicos de datos geoespaciales y de sistemas de información geográfica.

El curso es completamente virtual: las lecciones se imparten de manera sincrónica por videoconferencia, en el horario del curso. Los contenidos del curso y los recursos relacionados se comparten en el sitio web [https://pf0953-programacionr.github.io/2026-ii/](https://pf0953-programacionr.github.io/2026-ii/), así como en la plataforma Mediación Virtual de la Universidad de Costa Rica.

### 2. OBJETIVOS

Al finalizar el curso, el estudiantado será capaz de:

1. Desarrollar programas en el lenguaje de programación R orientados al procesamiento de datos geoespaciales.
2. Aplicar un enfoque de ciencia de datos en los procesos de importación, transformación, visualización, análisis y comunicación de datos.
3. Desarrollar soluciones reproducibles a problemas computacionales mediante R.
4. Integrar visualizaciones tabulares, gráficas y geoespaciales de datos en documentos computacionales y aplicaciones interactivas desarrolladas en R.
5. Emplear de manera crítica, responsable y transparente herramientas de inteligencia artificial como apoyo en el desarrollo de programas y en el análisis de datos.

### 3. CONTENIDO DEL CURSO

| SEMANA | CONTENIDO | LECTURA OBLIGATORIA |
|---|---|---|
| **I. INTRODUCCIÓN A LA CIENCIA DE DATOS Y A LA PROGRAMACIÓN DE COMPUTADORAS** |  |  |
| 1 (10 al 14 de agosto) | Entrega y discusión del programa del curso.<br><br>Introducción a la ciencia de datos.<br><br>Reproducibilidad en los procesos de análisis de datos. | Mine Çetinkaya-Rundel y Johanna Hardin (2024, capítulo 1)<br><br>Hadley Wickham, Mine Çetinkaya-Rundel y Garret Grolemund (2023, Introducción) |
| 2 (17 al 21 de agosto) | El lenguaje de marcado Markdown.<br><br>Git, GitHub y GitHub Pages.<br><br>Asistentes de programación basados en inteligencia artificial: panorama y lineamientos de uso en el curso. | *Markdown Tutorial* (s. f.)<br><br>Ihechikara Vincent Abba (2021)<br><br>GitHub (s. f.)<br><br>Stanford University (2025) |
| **II. EL LENGUAJE DE PROGRAMACIÓN R** |  |  |
| 3 (24 al 28 de agosto) | El lenguaje R:<br>• Historia y características.<br>• RStudio: ambiente de desarrollo integrado.<br>• Objetos, tipos de datos, funciones y paquetes.<br>• Operaciones básicas con la notación de [] y $: selección, ordenamiento, filtrado, agrupación, sumarización. | The R Foundation (s. f.)<br><br>Garret Grolemund (2014, capítulos 1 al 8) |
| 4 (31 de agosto al 4 de setiembre) | El lenguaje R (continuación):<br>• Condicionales.<br>• Ciclos.<br>• Funciones definidas por el usuario. | Garret Grolemund (2014, capítulos 9 al 12) |
| 5 (7 al 11 de setiembre) | Quarto: sistema de publicación de documentos técnicos y científicos:<br>• Sintaxis.<br>• Bloques de código en R.<br>• Publicación de documentos en Internet.<br><br>Uso de asistentes de inteligencia artificial para explicar y depurar código.<br><br>**ENTREGA DE TAREA 1** | Quarto (s. f.-b)<br><br>Quarto (s. f.-d) |
| **III. EL CONJUNTO DE PAQUETES TIDYVERSE** |  |  |
| 6 (14 al 18 de setiembre) | tidyverse: conjunto de paquetes de R para ciencia de datos:<br>• Datos *tidy*.<br>• dplyr: transformación de datos (selección, filtrado, agrupación, sumarización, unión de conjuntos de datos). | Hadley Wickham (2014)<br><br>Hadley Wickham, Mine Çetinkaya-Rundel y Garret Grolemund (2023, capítulos 1 al 8) |
| 7 (21 al 25 de setiembre) | ggplot2: paquete para la creación declarativa de gráficos estadísticos:<br>• La gramática de gráficos.<br>• Capas, estéticas y geometrías. | Hadley Wickham (2010)<br><br>Hadley Wickham, Mine Çetinkaya-Rundel y Garret Grolemund (2023, capítulos 9 al 11)<br><br>Winston Chang (2018, capítulo 2) |
| 8 (28 de setiembre al 2 de octubre) | plotly: paquete para graficación interactiva.<br><br>DT: paquete para tablas interactivas.<br><br>Uso de asistentes de inteligencia artificial para generación y verificación de código de análisis de datos. | Plotly (s. f.)<br><br>Posit (s. f.-a) |
| **IV. EL ECOSISTEMA GEOESPACIAL DE R** |  |  |
| 9 (5 al 9 de octubre) | Introducción al manejo de datos geoespaciales: modelos de datos vectorial y raster, sistemas de referencia de coordenadas.<br><br>sf: paquete para manipulación y análisis de datos vectoriales. | Robin Lovelace, Jakub Nowosad y Jannes Münchow (2025, capítulos 1 y 2) |
| 10 (12 al 16 de octubre) | sf (continuación):<br>• Operaciones con datos de atributos.<br>• Operaciones con datos espaciales.<br><br>**ENTREGA DE TAREA 2** | Robin Lovelace, Jakub Nowosad y Jannes Münchow (2025, capítulos 3 y 4) |
| 11 (19 al 23 de octubre) | leaflet: paquete para desarrollo de mapas interactivos. | Posit (s. f.-b) |
| 12 (26 al 30 de octubre) | terra: paquete para manejo de datos raster.<br><br>Ejemplos integrados de análisis de datos vectoriales y raster. | Robert J. Hijmans (s. f.)<br><br>Robin Lovelace, Jakub Nowosad y Jannes Münchow (2025, capítulo 5) |
| **V. TABLEROS DE CONTROL Y APLICACIONES INTERACTIVAS** |  |  |
| 13 (2 al 6 de noviembre) | Quarto *dashboards*: formato de Quarto para el desarrollo de tableros de control. | Quarto (s. f.-c) |
| 14 (9 al 13 de noviembre) | shiny: paquete para el desarrollo de aplicaciones web interactivas:<br>• Estructura de una aplicación: interfaz de usuario y servidor.<br>• Reactividad.<br><br>**ENTREGA DE TAREA 3** | Hadley Wickham (2021, capítulos 1 al 4)<br><br>Posit (s. f.-c) |
| 15 (16 al 20 de noviembre) | shiny (continuación): integración de visualizaciones tabulares, gráficas y geoespaciales. Despliegue de aplicaciones en shinyapps.io.<br><br>Herramientas agénticas de inteligencia artificial para programación: revisión crítica del código generado y documentación de su uso.<br><br>Taller de desarrollo del proyecto final. | Posit (s. f.-d)<br><br>Quarto (s. f.-a)<br><br>Stanford University (2025) |
| 16 (23 al 27 de noviembre) | Taller de cierre del proyecto final.<br><br>**PRESENTACIÓN ORAL Y ENTREGA DE LA APLICACIÓN DEL PROYECTO FINAL** |  |
| SEMANA DE EXÁMENES (30 de noviembre al 5 de diciembre) | Entrega del documento computacional del proyecto final (examen final en modalidad para la casa). |  |

### 4. METODOLOGÍA

El curso se desarrolla mediante clases teórico-prácticas virtuales sincrónicas, impartidas por videoconferencia en el horario del curso. Los conceptos teóricos son explicados por el profesor durante las sesiones de clase y también se abordan mediante lecturas previamente asignadas. Las sesiones prácticas se destinan a la realización de ejercicios de programación en los que el estudiantado aplica los conocimientos aprendidos y las habilidades desarrolladas, tanto en ejercicios cortos como en el desarrollo incremental del tema elegido para las tareas y el proyecto final.

Los recursos didácticos incluyen lecturas, documentación en línea, tutoriales, videos, conjuntos de datos de ejemplo y documentos computacionales con código ejecutable. Los contenidos de las lecciones están disponibles en el sitio web del curso ([https://pf0953-programacionr.github.io/2026-ii/](https://pf0953-programacionr.github.io/2026-ii/)), en el que hay enlaces a la bibliografía y a otros recursos de aprendizaje. Todo el software del curso (R, RStudio, Quarto y los paquetes utilizados) es de código abierto y gratuito, y se instala en las computadoras del estudiantado; como alternativa, también puede ejecutarse en servicios en la nube como Posit Cloud.

**Grado de virtualidad y uso del entorno virtual**: el curso es completamente virtual. Las lecciones se imparten de manera sincrónica por videoconferencia, los jueves de 17:00 a 19:50; los enlaces a las sesiones se publican en el entorno virtual del curso en la plataforma Mediación Virtual. En el entorno virtual también se comparten el programa del curso, los enlaces a los contenidos de las lecciones y a los recursos didácticos; ahí se realizan las entregas de las tareas y del proyecto final, se comunican las calificaciones mediante el libro de calificaciones y se envían mensajes oficiales.

**Uso de herramientas de inteligencia artificial**: el curso incorpora de manera paulatina el uso de asistentes de programación basados en IA (ej. asistentes conversacionales, asistentes integrados en editores de código y herramientas agénticas), como apoyo para explicar, depurar, generar y documentar código. Su uso se orienta con lineamientos de transparencia y pensamiento crítico: el estudiantado debe declarar el uso de estas herramientas en sus trabajos, comprender y ser capaz de explicar todo el código que entregue, y verificar los resultados generados.

La atención de dudas y consultas se realiza en las sesiones sincrónicas, en el horario de atención al estudiantado (J 14-15-16, por videoconferencia), por medio del correo electrónico institucional y mediante el sistema de mensajes de Mediación Virtual.

### 5. EVALUACIÓN

La evaluación incluye dos componentes: tareas programadas y proyecto final.

**a. Tareas programadas (50 %)**. Consisten en ejercicios de programación que deben ser resueltos fuera del tiempo de clase y que aplican los contenidos del curso al tema elegido por cada estudiante. Su propósito es que el estudiantado construya de manera incremental los productos que integrará en el proyecto final. Las semanas estimadas de entrega, los temas a desarrollar y el valor de cada tarea se presentan en la siguiente tabla:

| Semana de entrega | Tema a desarrollar | Porcentaje de la calificación final del curso |
|---|---|---|
| 5 | Elección del tema a desarrollar en las tareas y el proyecto final. Creación de un repositorio en GitHub y de una página web desarrollada en Markdown, con la descripción del tema y de sus fuentes de datos, publicada en Internet. | 15 % |
| 10 | Documento computacional (Quarto) con datos del tema elegido, procesados mediante los paquetes del tidyverse y presentados en tablas y gráficos, publicado en Internet. | 15 % |
| 14 | Documento computacional (Quarto) que incorpora datos geoespaciales del tema elegido, presentados en tablas, gráficos y mapas, publicado en Internet. | 20 % |

**b. Proyecto final (50 %)**. Su objetivo es sintetizar los conocimientos y habilidades aprendidos durante el curso. Consiste en el desarrollo del tema elegido en tres productos: (1) una aplicación web interactiva desarrollada en shiny, o un marco de trabajo similar, con visualizaciones tabulares, gráficas y geoespaciales, publicada en Internet; (2) un documento computacional (Quarto), con estructura de artículo, que documente el proceso de desarrollo, los datos y métodos utilizados y los principales hallazgos; y (3) una presentación oral de la aplicación y de los resultados, realizada de manera sincrónica por videoconferencia. La aplicación se entrega y se presenta oralmente en la semana 16, última semana de clases; el documento computacional se entrega en la semana de exámenes finales, como examen final en modalidad "para la casa". Los componentes y su valor se presentan en la siguiente tabla:

| Fecha de entrega o realización | Componente | Porcentaje de la calificación final del curso |
|---|---|---|
| Semana 16 | Aplicación web interactiva (shiny o un marco de trabajo similar) con visualizaciones tabulares, gráficas y geoespaciales, publicada en Internet. | 25 % |
| Semana 16 | Presentación oral sincrónica del proyecto, por videoconferencia. | 10 % |
| Semana de exámenes | Documento computacional (Quarto) con estructura de artículo, que documenta el proceso de desarrollo, los datos y métodos utilizados y los principales hallazgos. Se entrega como examen final en modalidad "para la casa". | 15 % |

En todas las evaluaciones se permite el uso de herramientas de inteligencia artificial, siempre que este se declare explícitamente y que la persona estudiante comprenda y sea capaz de explicar el trabajo entregado. El uso no declarado de estas herramientas, o la incapacidad de explicar el trabajo propio, se considerará una falta a la honestidad académica, según lo establecido en el Reglamento de Orden y Disciplina de los Estudiantes de la Universidad de Costa Rica.

### 6. BIBLIOGRAFÍA

#### Bibliografía obligatoria

Abba, I. V. (2021). *Git and GitHub tutorial – Version control for beginners*. freeCodeCamp. https://www.freecodecamp.org/news/git-and-github-for-beginners/

Çetinkaya-Rundel, M., y Hardin, J. (2024). *Introduction to modern statistics* (2.ª ed.). OpenIntro. https://openintrostat.github.io/ims/

Chang, W. (2018). *R graphics cookbook: Practical recipes for visualizing data* (2.ª ed.). O'Reilly Media. https://r-graphics.org/

GitHub. (s. f.). *Quickstart for GitHub Pages*. GitHub Docs. Recuperado el 10 de agosto de 2026, de https://docs.github.com/en/pages/quickstart

Grolemund, G. (2014). *Hands-on programming with R: Write your own functions and simulations*. O'Reilly Media. https://rstudio-education.github.io/hopr/

Hijmans, R. J. (s. f.). *Spatial data analysis with R*. Recuperado el 10 de agosto de 2026, de https://rspatial.org/

Lovelace, R., Nowosad, J., y Münchow, J. (2025). *Geocomputation with R* (2.ª ed.). Chapman and Hall/CRC. https://r.geocompx.org/

Markdown Tutorial. (s. f.). Recuperado el 10 de agosto de 2026, de https://www.markdowntutorial.com/

Plotly. (s. f.). *Plotly R open source graphing library*. Recuperado el 10 de agosto de 2026, de https://plotly.com/r/

Posit. (s. f.-a). *DT: An R interface to the DataTables library*. Recuperado el 10 de agosto de 2026, de https://rstudio.github.io/DT/

Posit. (s. f.-b). *Leaflet for R*. Recuperado el 10 de agosto de 2026, de https://rstudio.github.io/leaflet/

Posit. (s. f.-c). *Shiny for R: Get started*. Recuperado el 10 de agosto de 2026, de https://shiny.posit.co/r/getstarted/

Posit. (s. f.-d). *shinyapps.io user guide*. Recuperado el 10 de agosto de 2026, de https://docs.posit.co/shinyapps.io/

Quarto. (s. f.-a). *Dashboards with Shiny for R*. Recuperado el 10 de agosto de 2026, de https://quarto.org/docs/dashboards/interactivity/shiny-r.html

Quarto. (s. f.-b). *Markdown basics*. Recuperado el 10 de agosto de 2026, de https://quarto.org/docs/authoring/markdown-basics.html

Quarto. (s. f.-c). *Quarto dashboards*. Recuperado el 10 de agosto de 2026, de https://quarto.org/docs/dashboards/

Quarto. (s. f.-d). *Tutorial: Hello, Quarto*. Recuperado el 10 de agosto de 2026, de https://quarto.org/docs/get-started/hello/rstudio.html

Stanford University. (2025). *CS146S: The modern software developer*. Recuperado el 10 de agosto de 2026, de https://themodernsoftware.dev/

The R Foundation. (s. f.). *The R project for statistical computing*. Recuperado el 10 de agosto de 2026, de https://www.r-project.org/

Wickham, H. (2010). A layered grammar of graphics. *Journal of Computational and Graphical Statistics, 19*(1), 3-28. https://doi.org/10.1198/jcgs.2009.07098

Wickham, H. (2014). Tidy data. *Journal of Statistical Software, 59*(1), 1-23. https://doi.org/10.18637/jss.v059.i10

Wickham, H. (2021). *Mastering Shiny: Build interactive apps, reports, and dashboards powered by R*. O'Reilly Media. https://mastering-shiny.org/

Wickham, H., Çetinkaya-Rundel, M., y Grolemund, G. (2023). *R for data science: Import, tidy, transform, visualize, and model data* (2.ª ed.). O'Reilly Media. https://r4ds.hadley.nz/

#### Bibliografía complementaria

Fernández-Avilés, G., y Montero, J. M. (2024). *Fundamentos de ciencia de datos con R*. McGraw-Hill. https://cdr-book.github.io/

Irizarry, R. A. (2019). *Introduction to data science: Data wrangling and visualization with R*. Chapman and Hall/CRC. http://rafalab.dfci.harvard.edu/dsbook-part-1/

Moraga, P. (2019). *Geospatial health data: Modeling and visualization with R-INLA and Shiny*. Chapman and Hall/CRC. https://www.paulamoraga.com/book-geospatial/

Pebesma, E., y Bivand, R. (2023). *Spatial data science: With applications in R*. Chapman and Hall/CRC. https://r-spatial.org/book/

Sievert, C. (2020). *Interactive web-based data visualization with R, plotly, and shiny*. Chapman and Hall/CRC. https://plotly-r.com/

Wing, J. M. (2006). Computational thinking. *Communications of the ACM, 49*(3), 33-35. https://doi.org/10.1145/1118178.1118215
