class Nodo():
    dato: int
    siguiente: object
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class Hash:
    Arreglo: list
    FactorCarga = 0.75 
    M = 7000
    N = M * FactorCarga
    def __init__(self):
        self.Arreglo = [None for i in range(self.M)]

    def hashModulo(self,clave):
        return clave % self.N
    
## Nombre: insertarClave
## Encabezado: insertarClave(self, clave)
## Funcion: Insertar una clave mediante la transformacion de la misma mediante hashing en un la representacion encadenada
## entrada: self,clave
## salida: se carga correctamente la clave en un indice, sino en la lista encadenada dentro de ese indice
    def insertarClave(self, clave):
        nuevo = Nodo(clave) ## 1
        claveRes = self.hashModulo(clave) ## 1
        if self.Arreglo[claveRes] is None: ## 1 
            self.Arreglo[claveRes] = nuevo ## 1
        else:
            aux = self.Arreglo[claveRes] ## 1
            while aux.siguiente is not None: ## n   
                aux = aux.siguiente            ## 1n
            aux.siguiente = nuevo       ## 1
    
    ## 2n + 6 (o(n)) Lineal
    
    ## enrealidad tiene a O(1) pero en el peor de los casos tiene a O(n)
    
    
    