
import pygame
import json

#NOMBRE DE ARCHICO JSON


def gestionar_json(contador, high_score_file):
    
    try:
        with open(high_score_file, "r") as file:
            high_score_data = json.load(file)
            max_contador = high_score_data.get("max_contador", 0)
    except FileNotFoundError:
        max_contador = 0

    if contador > max_contador:
        max_contador = contador

    high_score_data = {"max_contador": max_contador}

    try:
        with open(high_score_file, "w") as file:
            json.dump(high_score_data, file)
    except FileNotFoundError:
        print("Error al intentar guardar el archivo JSON.")

def obtener_max_puntuacion(high_score_file="nombre_del_archivo.json"):
    try:
        with open(high_score_file, "r") as file:
            high_score_data = json.load(file)
            return high_score_data.get("max_contador", 0)
    except FileNotFoundError:
        return 0


