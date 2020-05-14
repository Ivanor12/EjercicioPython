from pathlib import Path
import requests
import os
#direccion API publica que voy a utilizar
#https://docs.thecatapi.com/
try:
    def menu():
        os.system('cls')
        print("\t1 - Referencias API y codigos de ejemplo")
        print("\t2 - Foto de un gato al azar")
        opcion=int(input("Selecciona una opcion : "))
        return (opcion)


        api_address="https://www.etnassoft.com/api/v1/get/?keyword=python&count_items=true&decode=true"
        resp = requests.get(api_address)
        if resp.status_code==200:
            json_data=json.loads(resp.content)
            print(type(json_data))
            print("Referencias API y codigos de ejemplo : %s"%json_data.get('texto'))
        def gatos_categoria():
            categoria=input ("Introduce la categoria de gatos sobre la cual quieres hacer la consulta : ")
            api_address="https://www.etnassoft.com/api/v1/get/?category=%s&criteria=most_viewed&decode=true"%categoria
        resp = requests.get(api_address)
        if resp.status_code==200:
            json_data=json.loads(resp.content)
            contador=1
        def fotos_gato_al_azar():
            api_address="https://www.etnassoft.com/api/v1/get/?keyword=python&lang=spanish&last_year&decode=true"
        resp = requests.get(api_address)
        if resp.status_code==200:#todo correcto
            json_data=json.loads(resp.content)
            print(json_data)
    while True:
            opcion=menu()
            if opcion==1:
                categoria_gatos()
            elif opcion==2:
                fotos_gatos_al_azar()
            elif opcion==3:
                break

    input("Pulse una tecla para terminar...")

except:
    print("Ha ocurrido algun error")