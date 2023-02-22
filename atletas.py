from Atleta import Atleta
from csv import reader
import random

def cargar_atletas(archivo):
    atletas = {}
    with open(archivo, "r", encoding="utf-8") as a:
        csv_reader = reader(a)
        for linea in csv_reader:
            nombre = linea[0]
            edad = int(linea[1])
            atleta = Atleta(nombre, edad)
            atletas[nombre] = atleta
    return atletas

def carrera(atletas:dict,valores:list):
    for nombre,atleta in atletas.items():
        t = random.choice(valores)
        atleta.agregar_tiempo(t)
        
def ganador(atletas:dict):
    top = 19.2
    key = ""
    for nombre, atleta in atletas.items():
        if atleta.top3()[0] < top:
            top = atleta.top3()[0]
            key = nombre
        print(f"{nombre} - Tiempo: {atleta.top(3)[0]}")
    print(f" Gana: {key} con {top} segundos")

def main():
    atletas = cargar_atletas("atletas.csv")
    #print(atletas)
    valores = [x for x in range(9.6,19.2,.1)]
    


if __name__ == "__main__":
    main()