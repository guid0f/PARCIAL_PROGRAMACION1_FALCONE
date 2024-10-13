import random  
#A
def solicitar_numero():  
    """  
    Solicita al usuario que ingrese un número entero en un rango específico.  
   
    Este procedimiento repetirá la solicitud hasta que el usuario ingrese un número válido que esté  
    entre 3 y 15. Si la entrada no es un número entero válido, se mostrará un mensaje de error.  
   
    Devuelve:  
        int: Un número entero entre 3 y 15, ingresado por el usuario.  
    """  
    while True:  
        numero_input = input("Ingrese un número entero entre 3 y 15: ")  
        
        if numero_input == "":                  
            print("Entrada vacía. Por favor, ingrese un número entero.")  
            continue  
   
        es_entero = True  
     
        for i in numero_input:  
            ascii_val = ord(i)  
            if not (48 <= ascii_val <= 57):   
                es_entero = False  
                break        
     
        if es_entero:  
            numero = int(numero_input)  
            if 3 <= numero <= 15:  
                return numero  
            else:  
                print("El número debe estar entre 3 y 15. Intente de nuevo.")  
        else:  
            print("Entrada no válida. Por favor, ingrese un número entero.")          
      



#B
def generar_lista_letras(longitud:int) -> list:  
    """  
    Genera una lista de letras aleatorias en mayúsculas.  
   
    La longitud de la lista es especificada por el usuario y cada letra es seleccionada aleatoriamente  
    entre 'A' (65) y 'Z' (90) del código ASCII.  
   
    Parámetros:  
        longitud (int): La longitud de la lista que se generará.  
   
    Devuelve:  
        list: Una lista de letras aleatorias en mayúsculas.  
    """  
    lista = [""] * longitud                     
    for i in range(longitud):  
        letra = chr(random.randint(65, 90))     
        lista[i] = letra                        
    return lista  

#C
def mostrar_lista(lista:list):  
    """  
    Muestra los elementos de una lista en la consola.  
   
    Si la lista está vacía, se mostrará un mensaje indicando que no se ha generado ninguna lista.  
   
    Parámetros:  
        lista (list): La lista de letras que se desea mostrar.  
    """  
    if len(lista) > 0:  
        print("Lista generada:", end=" ")  
        for letra in lista[:-1]:  
            print(letra, end=", ")  
        print(lista[-1])  
    else:  
        print("No se ha generado ninguna lista.")  

#D
def buscar_letra_en_lista(letra: str, lista: list) -> list:  
    """  
    Busca todas las posiciones de una letra específica en la lista.  
   
    Devuelve una lista de índices donde se encuentra la letra.  
   
    Parámetros:  
        letra (str): La letra que se desea buscar en la lista.  
        lista (list): La lista en la que se busca la letra.  
   
    Devuelve:  
        list: Una lista de índices donde la letra se encuentra en la lista.  
    """  
    indices = []  
    
    for i in range(len(lista)):  
        if lista[i] == letra:  
            indices = indices + [i] 
    return indices

#E
def ordenar_lista(lista: list) -> list:  
    """  
    Ordena una lista de letras en orden ascendente o descendente utilizando ordenamiento por burbuja.  
   
    Parámetros:  
        lista (list): Lista de letras a ordenar.  
   
    Devuelve:  
        list: Nueva lista ordenada según el criterio ingresado por el usuario.  
    """  
    # Hacer una copia de la lista original  
    lista_ordenada = [letra for letra in lista]  # Copiamos cada letra a una nueva lista  
    
    # Solicitar criterio al usuario  
    criterio = input("Ingrese 'ASC' para ordenar de forma ascendente o 'DESC' para descendente: ")
    
    while criterio not in ["ASC", "DESC"]:  
        print("Criterio no válido. Debe ingresar 'ASC' o 'DESC'.")  
        criterio = input("Ingrese 'ASC' para ordenar de forma ascendente o 'DESC' para descendente: ")

    n = len(lista_ordenada)  
    
    # Implementación del Bubble Sort  
    for i in range(n):  
        for j in range(0, n-i-1):  
            if criterio == "ASC":  
                if lista_ordenada[j] > lista_ordenada[j + 1]:  # Ordenar de forma ascendente  
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]  
            elif criterio == "DESC":  
                if lista_ordenada[j] < lista_ordenada[j + 1]:  # Ordenar de forma descendente  
                    lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]  

    return lista_ordenada