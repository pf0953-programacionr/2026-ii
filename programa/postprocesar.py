"""Posprocesa el DOCX generado por pandoc.

- Ajusta los anchos de columna de las tablas: la tabla de contenidos queda
  20/50/30 % del ancho de la página y las tablas de evaluación usan los
  anchos del programa de GF-0657 2026-II (revisados por la comisión de
  docencia de la Escuela de Geografía en agosto 2026).
- Centra la fila de encabezado de la tabla de componentes de la evaluación.
- Justifica los párrafos del cuerpo del documento — desde "PROGRAMA DEL
  CURSO" hasta la bibliografía, sin tocar títulos, tablas ni imágenes.
- Deja una línea en blanco antes y después de las tablas de la sección de
  evaluación.
- Centra los párrafos que contienen imágenes (código QR).
- Centra el bloque de encabezado (del nombre del curso hasta el título
  "PROGRAMA DEL CURSO"), como en la plantilla oficial.
- En la tabla de contenidos, fusiona en una sola celda centrada las filas de
  título de sección (las que inician con numeración romana, ej. "I. …").
- Impide que las filas de las tablas se partan entre páginas y mantiene las
  filas de título de sección junto a la fila que les sigue.
- Aplica espaciado sencillo (sin espacio entre párrafos) a las líneas desde
  "Profesor:" hasta "II ciclo lectivo 2026" y deja una línea en blanco antes
  de "PROGRAMA DEL CURSO".

Uso: python3 postprocesar.py <archivo.docx>
"""

import re
import sys
import zipfile

# Ancho útil de la página: 21.59 cm - 4 cm de márgenes ≈ 9970 twips.
# Los anchos de las tablas de evaluación provienen del programa de
# GF-0657 2026-II (revisado por la comisión de docencia en agosto 2026).
ANCHOS_TABLAS = [
    [1994, 4985, 2991],  # contenidos: 20 %, 50 %, 30 %
    [2375, 2109, 4361],  # evaluación: quices (tabla al 89 % del ancho)
    [1235, 6647, 2080],  # evaluación: tareas
    [1572, 6562, 1828],  # evaluación: componentes de la calificación
]
ENCABEZADO_COMPONENTES = "Fecha de entrega o realización"
INICIO_JUSTIFICADO = "PROGRAMA DEL CURSO"
FIN_JUSTIFICADO = "6. BIBLIOGRAFÍA"
FIN_ENCABEZADO = "PROGRAMA DEL CURSO"
INICIO_COMPACTO = "Profesor:"
FIN_COMPACTO = "II ciclo lectivo 2026"
ESPACIADO_SENCILLO = '<w:spacing w:after="0" w:line="240" w:lineRule="auto" />'


def agregar_a_ppr(parrafo, xml):
    if "<w:pPr>" in parrafo:
        return parrafo.replace("</w:pPr>", xml + "</w:pPr>", 1)
    return parrafo.replace("<w:p>", "<w:p><w:pPr>" + xml + "</w:pPr>", 1)


def centrar_parrafo(parrafo):
    if "<w:jc " in parrafo:
        return parrafo
    return agregar_a_ppr(parrafo, '<w:jc w:val="center" />')


def procesar_encabezado(doc):
    """Centra y compacta los párrafos del bloque de encabezado del programa."""
    resultado = []
    pos = 0
    compacto = False
    for m in re.finditer(r"<w:p>.*?</w:p>", doc, re.S):
        resultado.append(doc[pos : m.start()])
        parrafo = m.group(0)
        pos = m.end()
        texto = re.sub(r"<[^>]+>", "", parrafo)
        if FIN_ENCABEZADO in texto:
            resultado.append("<w:p />")  # línea en blanco de separación
            resultado.append(centrar_parrafo(parrafo))
            break
        if INICIO_COMPACTO in texto:
            compacto = True
        if compacto:
            parrafo = agregar_a_ppr(parrafo, ESPACIADO_SENCILLO)
        if FIN_COMPACTO in texto:
            compacto = False
        resultado.append(centrar_parrafo(parrafo))
    resultado.append(doc[pos:])
    return "".join(resultado)


def fusionar_filas_seccion(doc):
    """Fusiona las filas de título de sección de la tabla de contenidos."""
    ini = doc.index("<w:tbl>")
    fin = doc.index("</w:tbl>", ini) + len("</w:tbl>")
    tabla = doc[ini:fin]

    def fusionar(m):
        fila = m.group(0)
        celdas = re.findall(r"<w:tc>.*?</w:tc>", fila, re.S)
        if len(celdas) != 3:
            return fila
        texto = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", celdas[0]))
        if not re.match(r"[IVX]+\.\s", texto):
            return fila
        if any(re.search(r"<w:t[^>]*>[^<]", c) for c in celdas[1:]):
            return fila
        celda = celdas[0].replace(
            "<w:tcPr />", '<w:tcPr><w:gridSpan w:val="3" /></w:tcPr>', 1
        )
        celda = centrar_parrafo(celda)
        # "Mantener con el siguiente" para que la fila de sección no quede
        # sola al final de una página.
        celda = agregar_a_ppr(celda, "<w:keepNext />")
        # Línea en blanco antes y después del título de sección.
        celda = celda.replace("</w:tcPr>", "</w:tcPr><w:p />", 1)
        celda = celda.replace("</w:tc>", "<w:p /></w:tc>")
        celda = celda.replace(
            "<w:p />", "<w:p><w:pPr><w:keepNext /></w:pPr></w:p>"
        )
        return "<w:tr>" + celda + "</w:tr>"

    tabla = re.sub(r"<w:tr>.*?</w:tr>", fusionar, tabla, flags=re.S)
    return doc[:ini] + tabla + doc[fin:]


def justificar_parrafo(parrafo):
    if "<w:jc " in parrafo:
        return parrafo
    return agregar_a_ppr(parrafo, '<w:jc w:val="both" />')


def justificar_cuerpo(doc):
    """Justifica los párrafos del cuerpo (fuera de tablas, sin títulos ni imágenes)."""
    resultado = []
    pos = 0
    activo = False
    for m in re.finditer(
        r"<w:tbl>.*?</w:tbl>|<w:p\b[^>]*?/>|<w:p\b.*?</w:p>", doc, re.S
    ):
        resultado.append(doc[pos : m.start()])
        pos = m.end()
        bloque = m.group(0)
        if bloque.startswith("<w:tbl>") or bloque.endswith("/>"):
            resultado.append(bloque)
            continue
        texto = re.sub(r"<[^>]+>", "", bloque)
        es_titulo = re.search(r'w:pStyle w:val="(Ttulo|Heading)', bloque)
        if not activo and INICIO_JUSTIFICADO in texto:
            activo = True
        elif activo and es_titulo and FIN_JUSTIFICADO in texto:
            activo = False
        elif activo and not es_titulo and "<w:drawing>" not in bloque:
            bloque = justificar_parrafo(bloque)
        resultado.append(bloque)
    resultado.append(doc[pos:])
    return "".join(resultado)


def centrar_encabezado_componentes(doc):
    """Centra la fila de encabezado de la tabla de componentes de la evaluación."""
    resultado = []
    pos = 0
    for m in re.finditer(r"<w:tbl>.*?</w:tbl>", doc, re.S):
        tabla = m.group(0)
        if ENCABEZADO_COMPONENTES in re.sub(r"<[^>]+>", "", tabla):
            fila = re.search(r"<w:tr\b.*?</w:tr>", tabla, re.S)
            nueva = re.sub(
                r"<w:p>.*?</w:p>",
                lambda p: centrar_parrafo(p.group(0)),
                fila.group(0),
                flags=re.S,
            )
            tabla = tabla[: fila.start()] + nueva + tabla[fila.end() :]
        resultado.append(doc[pos : m.start()] + tabla)
        pos = m.end()
    resultado.append(doc[pos:])
    return "".join(resultado)


def espaciar_tablas_evaluacion(doc):
    """Deja una línea en blanco antes y después de las tablas de evaluación."""
    resultado = []
    pos = 0
    n = 0
    for m in re.finditer(r"<w:tbl>.*?</w:tbl>", doc, re.S):
        n += 1
        resultado.append(doc[pos : m.start()])
        pos = m.end()
        if n >= 2:  # la tabla 1 es la de contenidos
            resultado.append("<w:p />" + m.group(0) + "<w:p />")
        else:
            resultado.append(m.group(0))
    resultado.append(doc[pos:])
    return "".join(resultado)


def evitar_particion_filas(doc):
    """Impide que las filas de las tablas se partan entre páginas."""
    doc = re.sub(r"<w:tr><w:trPr>", "<w:tr><w:trPr><w:cantSplit />", doc)
    doc = re.sub(
        r"<w:tr>(?!<w:trPr>)", "<w:tr><w:trPr><w:cantSplit /></w:trPr>", doc
    )
    return doc


def main(path):
    zin = zipfile.ZipFile(path)
    doc = zin.read("word/document.xml").decode()

    tabla_n = [0]

    def anchos_tabla(m):
        tabla_n[0] += 1
        anchos = ANCHOS_TABLAS[min(tabla_n[0], len(ANCHOS_TABLAS)) - 1]
        grid = "".join(f'<w:gridCol w:w="{w}" />' for w in anchos)
        return f"<w:tblGrid>{grid}</w:tblGrid>"

    doc = re.sub(r"<w:tblGrid>.*?</w:tblGrid>", anchos_tabla, doc, flags=re.S)

    # Centra los párrafos que contienen imágenes (código QR).
    doc = re.sub(
        r"<w:p>(?:(?!</w:p>).)*?<w:drawing>.*?</w:p>",
        lambda m: centrar_parrafo(m.group(0)),
        doc,
        flags=re.S,
    )

    doc = procesar_encabezado(doc)
    doc = fusionar_filas_seccion(doc)
    doc = justificar_cuerpo(doc)
    doc = centrar_encabezado_componentes(doc)
    doc = espaciar_tablas_evaluacion(doc)
    doc = evitar_particion_filas(doc)

    datos = {item: zin.read(item) for item in zin.namelist()}
    datos["word/document.xml"] = doc.encode()
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, data in datos.items():
            zout.writestr(item, data)
    print(f"{path} posprocesado")


if __name__ == "__main__":
    main(sys.argv[1])
