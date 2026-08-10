"""Genera referencia.docx: el programa del curso 2024-II (formato del SEP)
con los estilos que pandoc necesita inyectados en styles.xml y con el logo
del SEP agregado a los encabezados.

El programa 2024-II se usa como base porque conserva la identidad visual
del Sistema de Estudios de Posgrado (SEP): logo de la UCR en la esquina
superior izquierda, formas verdes decorativas en los márgenes y pies de
página sin texto. pandoc toma de este documento los estilos, los márgenes
y los encabezados y pies de página; el contenido se descarta.

Este script:
  1. Extrae los estilos del documento de referencia por defecto de pandoc.
  2. Inyecta en la base los que falten (por styleId).
  3. Ajusta los estilos de encabezados (color negro, fuente heredada).
  4. Ajusta el estilo de tabla para que tenga bordes completos.
  5. Agrega el logo del SEP (logo-sep.png, descargado de
     https://www.sep.ucr.ac.cr/) en la esquina superior derecha de los
     encabezados de la primera página (header2.xml) y de las páginas
     siguientes (header1.xml).

Uso: python3 generar-referencia.py
"""

import os
import re
import subprocess
import zipfile

PANDOC = os.environ.get("PANDOC", os.path.expanduser("~/miniconda3/bin/pandoc"))
BASE = "../privado/documentos-recibidos/pf0953-programacionr-g001-2024-ii.docx"
LOGO_SEP = "logo-sep.png"
SALIDA = "referencia.docx"
REF_PANDOC = "/tmp/pandoc-default-reference.docx"

BORDES_TABLA = (
    '<w:tblBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:left w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:right w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="000000" />'
    '</w:tblBorders>'
)

# Dimensiones y posición del logo del SEP, en EMU (1 cm = 360 000 EMU).
# El logo original mide 792 x 127 px; se escala a 4.5 cm de ancho.
# Página carta (21.59 cm) - margen derecho (2 cm) - ancho del logo.
LOGO_CX = 1620000
LOGO_CY = round(LOGO_CX * 127 / 792)
LOGO_X = 7772400 - 720000 - LOGO_CX
LOGO_Y = 400000  # centrado verticalmente respecto al logo de la UCR

REL_LOGO = (
    '<Relationship Id="rIdLogoSEP" '
    'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" '
    'Target="media/logo-sep.png"/>'
)


def drawing_logo(doc_id):
    """Dibujo anclado del logo del SEP, para insertar en un párrafo del encabezado."""
    return (
        '<w:r><w:drawing>'
        '<wp:anchor behindDoc="0" distT="0" distB="0" distL="0" distR="0" '
        'simplePos="0" locked="0" layoutInCell="0" allowOverlap="1" '
        f'relativeHeight="{200 + doc_id}">'
        '<wp:simplePos x="0" y="0"/>'
        f'<wp:positionH relativeFrom="page"><wp:posOffset>{LOGO_X}</wp:posOffset></wp:positionH>'
        f'<wp:positionV relativeFrom="page"><wp:posOffset>{LOGO_Y}</wp:posOffset></wp:positionV>'
        f'<wp:extent cx="{LOGO_CX}" cy="{LOGO_CY}"/>'
        '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:wrapNone/>'
        f'<wp:docPr id="{900 + doc_id}" name="LogoSEP{doc_id}"/>'
        '<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">'
        '<a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:nvPicPr>'
        f'<pic:cNvPr id="{900 + doc_id}" name="LogoSEP{doc_id}"/>'
        '<pic:cNvPicPr/>'
        '</pic:nvPicPr>'
        '<pic:blipFill>'
        '<a:blip r:embed="rIdLogoSEP"/>'
        '<a:stretch><a:fillRect/></a:stretch>'
        '</pic:blipFill>'
        '<pic:spPr>'
        '<a:xfrm><a:off x="0" y="0"/>'
        f'<a:ext cx="{LOGO_CX}" cy="{LOGO_CY}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
        '</pic:spPr>'
        '</pic:pic>'
        '</a:graphicData>'
        '</a:graphic>'
        '</wp:anchor>'
        '</w:drawing></w:r>'
    )


def leer_styles(path):
    return zipfile.ZipFile(path).read("word/styles.xml").decode()


def main():
    subprocess.run(
        [PANDOC, "-o", REF_PANDOC, "--print-default-data-file", "reference.docx"],
        check=True,
    )

    base_xml = leer_styles(BASE)
    pandoc_xml = leer_styles(REF_PANDOC)

    ids_base = set(re.findall(r'w:styleId="([^"]+)"', base_xml))
    # Word y LibreOffice identifican los estilos por nombre, no por styleId:
    # inyectar un estilo cuyo nombre ya existe en la base (ej. Heading2 de
    # pandoc vs. Ttulo2 de la base, ambos "heading 2") crea un duplicado que
    # anula al de la base (los títulos pierden la negrita).
    # Mapa nombre (en minúsculas) -> styleId de la base, para crear alias.
    id_por_nombre = {}
    for m in re.finditer(r"<w:style [^>]*>.*?</w:style>", base_xml, re.S):
        s = m.group(0)
        n = re.search(r'<w:name w:val="([^"]+)"', s)
        if n:
            id_por_nombre[n.group(1).lower()] = re.search(
                r'w:styleId="([^"]+)"', s
            ).group(1)
    nombres_base = set(id_por_nombre)
    inyectados = []
    for estilo in re.findall(r"<w:style [^>]*>.*?</w:style>", pandoc_xml, re.S):
        sid = re.search(r'w:styleId="([^"]+)"', estilo).group(1)
        if sid in ids_base:
            continue
        nombre = re.search(r'<w:name w:val="([^"]+)"', estilo)
        if nombre and nombre.group(1).lower() in nombres_base:
            # El estilo existe en la base con otro styleId (ej. "Body Text"
            # es TextBody en la base y BodyText en pandoc). Se crea un alias
            # con el styleId de pandoc, basado en el estilo de la base, para
            # que las referencias de pandoc (pStyle, basedOn) no queden rotas
            # y hereden el formato de la base.
            tipo = re.search(r'w:type="([^"]+)"', estilo).group(1)
            base_id = id_por_nombre[nombre.group(1).lower()]
            alias = (
                f'<w:style w:type="{tipo}" w:styleId="{sid}">'
                f'<w:name w:val="{nombre.group(1)} (pandoc)" />'
                f'<w:basedOn w:val="{base_id}" />'
                '</w:style>'
            )
            inyectados.append((sid, alias))
            continue
        if sid.startswith("Heading"):
            # Heredar fuente y color de la base (negro, no azul).
            estilo = re.sub(r"<w:color [^/]*/>", "", estilo)
            estilo = re.sub(r"<w:rFonts [^/]*/>", "", estilo)
        if sid == "Table":
            # El estilo por defecto de pandoc no define bordes; se insertan.
            estilo = re.sub(r"<w:tblBorders>.*?</w:tblBorders>", "", estilo, flags=re.S)
            estilo = estilo.replace("<w:tblPr>", "<w:tblPr>" + BORDES_TABLA, 1)
        inyectados.append((sid, estilo))

    nuevo_xml = base_xml.replace(
        "</w:styles>", "".join(e for _, e in inyectados) + "</w:styles>"
    )

    with open(LOGO_SEP, "rb") as f:
        logo = f.read()

    zin = zipfile.ZipFile(BASE)
    with zipfile.ZipFile(SALIDA, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            if item == "word/styles.xml":
                data = nuevo_xml.encode()
            elif item in ("word/header1.xml", "word/header2.xml"):
                # El dibujo anclado se inserta en el primer párrafo; su
                # posición es absoluta respecto a la página.
                n = 1 if item.endswith("1.xml") else 2
                xml = data.decode()
                xml = xml.replace("</w:p>", drawing_logo(n) + "</w:p>", 1)
                data = xml.encode()
            elif item in (
                "word/_rels/header1.xml.rels",
                "word/_rels/header2.xml.rels",
            ):
                data = data.decode().replace(
                    "</Relationships>", REL_LOGO + "</Relationships>"
                ).encode()
            zout.writestr(item, data)
        zout.writestr("word/media/logo-sep.png", logo)

    print(f"{SALIDA} creado ({len(inyectados)} estilos inyectados, logo del SEP agregado)")


if __name__ == "__main__":
    main()
