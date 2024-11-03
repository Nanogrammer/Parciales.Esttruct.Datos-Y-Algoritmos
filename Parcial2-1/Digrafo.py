class Nodo():
    dato: int
    siguiente: object
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        

class Digrafo:
    N= 5
    matriz: list  ## USO MATRICIAL PARA VERIFICAR LA FILA Y COLUMNA SELECCIONADA Y NO REVISAR TODOS LOS NODOS
    
    def __init__(self):
        self.matriz = [[None for i in range(self.N)]for j in range(self.N)]
    
    def VerticesFuentes(self,raiz):
        ArregloFuentes = [] # T(o) = 1
        for i in range(len(self.matriz)): # T(o) = 2n + 2
            if self.gradoEntrada(i) is not None and self.gradoSalida(i) > 0:#T(o)= 2n ## cada llamada es n en el peor de los casos
                ArregloFuentes.append(i) # T(o) = 1n                         ## es decir es practicamente otro bucle dentro del for
        return ArregloFuentes # T(o) = 1
    ##### CALCULO FINAL = 2n² + n + 2
                    
            

    