class Atleta:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.tiempos = []
        
    def __str__(self):
        return f"Atleta {self.nombre} tiene {self.edad} años"
    
    def __repr__(self):
        return f"Atleta({self.nombre},{self.edad})"
    
    def agregar_tiempo(self,tiempo):
        self.tiempos.append(tiempo)
    
    def top3(self):
        return sorted(self.tiempos)[0:3]
    
if __name__ == "__main__":
    a = Atleta("Ana Guevara",26)
    print(a)
    print(repr(a))
    a.agregar_tiempo(10.20)
    a.agregar_tiempo(11.11)
    a.agregar_tiempo(10.03)
    a.agregar_tiempo(12.24)
    print(a.top3())
        