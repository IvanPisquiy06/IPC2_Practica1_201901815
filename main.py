import xml.etree.ElementTree as ET

# Función para obtener el código de un elemento Plataforma o Juego
def get_code(element):
    return element.find('codigo').text

# Función para ordenar una lista de elementos
def sort_elements(elements):
    return sorted(elements, key=get_code)

# Función para ordenar la lista de Plataformas y la lista de Juegos
def sort_lists(xml):
    lista_plataformas = xml.find('ListaPlataformas')
    lista_juegos = xml.find('ListadoJuegos')

    # Ordenar lista de Plataformas
    lista_plataformas[:] = sort_elements(lista_plataformas)

    # Ordenar lista de Juegos
    for juego in lista_juegos:
        plataformas = juego.find('Plataformas')
        plataformas[:] = sort_elements(plataformas)

    lista_juegos[:] = sort_elements(lista_juegos)

# Función para leer el archivo XML y devolver el XML ordenado
def sort_xml_file(file_path):
    tree = ET.parse(file_path)
    xml = tree.getroot()
    sort_lists(xml)
    tree.write("ejemplo_ordenado.xml", encoding="UTF-8", xml_declaration=True)
    return ET.tostring(xml)

file_path = input("Escriba el archivo que desea leer:")

sort_xml_file(file_path)