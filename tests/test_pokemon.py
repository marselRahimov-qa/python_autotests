import requests
import pytest

token = '9722fcf37f427c64c0eb35763dd3b39c'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params= {'trainer_id': '3628'})
    assert response.json()['trainer_name'] == 'True Barsik'