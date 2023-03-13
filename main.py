import xml.etree.ElementTree as ET

def read_xml_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Hacer lo que sea necesario con el archivo XML aquí
    # Por ejemplo, imprimir los elementos en la consola
    for child in root:
        print(child.tag, child.attrib)
        for subchild in child:
            print(subchild.tag, subchild.attrib, subchild.text)

file_path = input("Escriba el archivo que desea leer:")

read_xml_file(file_path)