import json

def cargar() -> list[dict]:
    lista_elementos = []
    try:
        with open('assets/documents/elementos_ordenados_dif.json','r',encoding='utf-8-sig') as a:
            archivo: dict = json.load(a)
            if archivo:
                for k,v in archivo.items():
                    lista_elementos.extend(v)
        return lista_elementos            
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        return lista_elementos