from funciones import *  


respuesta = "N"  
menu = '''  
    A) INGRESAR NUMERO   
    B) GENERAR LISTA  
    C) MOSTRAR LISTA  
    D) BUSCAR LETRA  
    E) ORDENAR LISTA  
    I) SALIR  

Ingrese una opcion: 
'''  

lista_letras = []  
numero = None  

while respuesta == "N":  
    opcion_seleccionada = input(menu)  

    match opcion_seleccionada:  
        case "A":    
            numero = solicitar_numero()  
            print(f"Número ingresado: {numero}")  
        
        case "B":  
            if numero is None: 
                print("No se ha ingresado un número. Por favor, ingrese un número primero en la opción A.")  
            else:  
                lista_letras = generar_lista_letras(numero)  
                print("Lista generada!")  

        case "C":   
                mostrar_lista(lista_letras)  
        
        case "D":  
            if not lista_letras:  
                print("No se ha generado ninguna lista. Por favor, genere una lista primero usando la opción B.")  
            else:  
                letra = input("Ingrese una letra mayúscula entre 'A' y 'Z': ")  
                indices = buscar_letra_en_lista(letra, lista_letras)  
                if indices:  
                    mostrar_lista(lista_letras)
                    print(f"La letra '{letra}' se encuentra en la posición:", end=" ") 
                    for indice in indices:  
                        print(indice +1, end=" ")  
                else:  
                    print(f"La letra '{letra}' no se encuentra en la lista.") 
                 
        
        case "E":  
            if lista_letras:  
                lista_letras = ordenar_lista(lista_letras)   
                mostrar_lista(lista_letras)  
            else:  
                print("No se puede ordenar, la lista está vacía.")  
        case "I":  
            print("¿Deseas SALIR? (S/N)")  

            while True:  
                respuesta = input("Ingresa S para sí o N para no: ")  

                if respuesta == 'S':  
                    break  
                elif respuesta == 'N':  
                    print("Volviendo a mostrar las opciones...")  
                    break
                else:  
                    print("Respuesta no válida. Por favor ingresa S o N.")

        case _:  
            print("La opción ingresada no es correcta.")  

print("Programa finalizado.")