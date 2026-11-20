import requests 


respuesta = requests.get(
    "https://pokeapi.co/api/v2/pokemon",
    timeout=(3,5)
)

print("estado http: ", respuesta.status_code)

if (respuesta.status_code == 200):
    result = respuesta.json()
    pokemon_buscar = input("buscar pokemon: ") # "bulbasaur"
    pokemones = result.get("results")
    resultado_busqueda = None
    for pk in pokemones:
        if (pk.get("name") == pokemon_buscar):
            resultado_busqueda = pk
            break

    if(resultado_busqueda):
        print(f"Pokemon encontrado : {resultado_busqueda.get("name")}")
        print(f"Url :{resultado_busqueda.get("url")}")
        url = resultado_busqueda.get("url")

        respuesta_pokemon = requests.get(
            url,
            timeout=(3,5)
        )
        json_rp = respuesta_pokemon.json()

        print(f"""
            "name": {json_rp.get('name')},
            "base_experience": {json_rp.get('base_experience')},
            "height": {json_rp.get('height')},
            "is_default": {json_rp.get('is_default')},
            "order": {json_rp.get('order')},
            "weight": {json_rp.get('weight')},
        """)

            







   