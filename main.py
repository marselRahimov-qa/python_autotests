import requests
token = '9722fcf37f427c64c0eb35763dd3b39c' # токен тренера
host = 'https://api.pokemonbattle.me:9104' # хост для покемонов

response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {    # тренер уже создан
    "trainer_token": token,
    "email": "marselo725@yandex.ru",
    "password": "1q2w3e4R"
}, headers = {'Content-Type' : 'application/json'})

print(response.text)
print (response.status_code)

response_activation = requests.post(f'{host}/trainers/confirm_email', json = {     #активация прошла
    "trainer_token": token
}, headers = {'Content-Type' : 'application/json'})

print(response_activation.text)
print (response.status_code)

'''if response.status_code == 200:
    print('OK!')
else:
    print('Not OK!')'''

response_change_trainer = requests.put(f'{host}/trainers', json =  {
    "name": "True Barsik",
    "city": "Штормград"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token': token})

print(response_change_trainer.text)

response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Покемоншка",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)

response_change_pokemon = requests.put(f'{host}/pokemons', json =  {
    "pokemon_id": "27727",
    "name": "Геракл",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_change_pokemon.text)

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "28053"
}, headers = {'Content-Type' : 'application/json', 'trainer_token': token})

print(response_add_pokemon.text)

'''if response.status_code ==200:
    print('OK!')
else:
    print('Not OK!')'''