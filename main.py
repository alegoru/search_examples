from agenda.contacto import Contacto
from carpeta.archivo import funcion

def buscar_numero_en_lista(lista, n):
    """recibe una lista y un numero y retorna la ubicacion del numero (empieza desde cero)"""
    for ubicacion, numero in enumerate(lista):
        if numero == n:
            return ubicacion


def buscar_diccionario_en_lista(lista, palabra):
    """recibe una lista de diccionarios y retorna el diccionario en el que se encuentra esa palabra
    ejemplo:
    {
        "nombre": "alexis",
        "telefono": "547234532"
    }
    """
    for contacto in lista:
        if contacto.get("nombre") == palabra:
            return contacto


def buscar_diccionario_en_lista_clave_dinamica(lista, clave, palabra):
    """recibe una lista de diccionarios y retorna el diccionario en el que se encuentra esa palabra
    ejemplo:
    {
        "clave": "palabra",
        "otra_clave": "otra palabra"
    }
    """
    for contacto in lista:
        if contacto.get(clave) == palabra:
            return contacto


def buscar_objeto_en_lista(lista, palabra):
    """recibe una lista de objetos y una palabra, luego busca los objetos en la lista que tengan esa palabra y
    retorna el primer objeto encontrado """
    for objeto in lista:
        if objeto.nombre == palabra:
            return objeto


def eliminar_diccionario_de_lista(lista:list, palabra):
    for dicc in lista:
        if dicc.get("nombre") == palabra:
            lista.remove(dicc)
            break

def eliminar_diccionario_de_lista_con_pop(lista:list, palabra):
    for indice, dicc in enumerate(lista):
        if dicc.get("nombre") == palabra:
            lista.pop(indice)
            break


def eliminar_objeto_de_lista(lista, palabra):
    for objeto in lista:
        if objeto.nombre == palabra:
            lista.remove(objeto)
            break


if __name__ == '__main__':
    # buscar numeros en lista
    lista_numeros = [1, 2, 3, 4, 5, 7, 8, 9, 6]
    print(buscar_numero_en_lista(lista_numeros, 3))  # retorna 2
    print(buscar_numero_en_lista(lista_numeros, 6))  # retorna 2


    #buscar diccionarios en lista
    lista_dicc = [
        {
            "nombre": "Santiago",
            "telefono": "12345678"
        },
        {
            "nombre": "alexis",
            "telefono": "234623432"
        }
    ]
    print(buscar_diccionario_en_lista(lista_dicc, "alexis")) # imprime el diccionario de alexis


    # crear diccionario y agregarlo a lista
    # nombre = input("ingrese nombre")
    # telefono = input("ingrese un telefono")
    # nuevo_dic = {
    #     "nombre": nombre,
    #     "telefono": telefono
    # }
    # print(lista_dicc)
    # lista_dicc.append(nuevo_dic)
    # print(lista_dicc)

    # Importar funcion y usarla
    funcion("Hola mundo!")


    # Buscar diccionarios en lista con clave dinamica
    print(buscar_diccionario_en_lista_clave_dinamica(lista_dicc, "telefono", "12345678"))
    print(buscar_diccionario_en_lista_clave_dinamica(lista_dicc, "nombre", "Santiago"))

    # Buscar objetos en lista
    lista_objetos = [
        Contacto("alexis", "3472345234"),
        Contacto("juandiego", "75234534"),
        Contacto("juandavid", "57453324"),
        Contacto("jeronimo", "89567345"),
        Contacto("nikolle", "9653745"),
        Contacto("gabriel", "07564345")
    ]

    print(buscar_objeto_en_lista(lista_objetos, "gabriel"))
    print(buscar_objeto_en_lista(lista_objetos, "nikolle"))
    print(buscar_objeto_en_lista(lista_objetos, "juandiego"))
    print(buscar_objeto_en_lista(lista_objetos, "jeronimo"))
    print(buscar_objeto_en_lista(lista_objetos, "gabriela"))
    # print(buscar_objeto_en_lista(lista_objetos, input("ingrese el nombre a buscar")))

    # Remover diccionario de lista
    print(lista_dicc)
    eliminar_diccionario_de_lista(lista_dicc, "alexis")
    print(lista_dicc)
    eliminar_diccionario_de_lista_con_pop(lista_dicc, "Santiago")
    print(lista_dicc)

    # Remover objeto de lista

    print(lista_objetos)
    eliminar_objeto_de_lista(lista_objetos, "alexis")
    print(lista_objetos)
    eliminar_objeto_de_lista(lista_objetos, "gabriel")
    print(lista_objetos)
    eliminar_objeto_de_lista(lista_objetos, "jeronimo")
    print(lista_objetos)
    eliminar_objeto_de_lista(lista_objetos, "juandiego")
    print(lista_objetos)
    eliminar_objeto_de_lista(lista_objetos, "nikolle")
    print(lista_objetos)



