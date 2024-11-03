import random 

class Nodo():
    dato: int
    siguiente : object
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        
class Hash:
    Arreglo: list
    N = 30
    M = 40
    
    
    def __init__(self):
        self.Arreglo = [None for i in range(self.M)]
    
    def HashModulo(self,clave):
        return int(clave%self.N)
    
    
## Nombre: InsertarClave
## Encabezado: InsertarClave(self,clave)
## Funcion: insertar clave, en la politica de direccionamiento abierto
## Entrada: self,clave
## Salida: se agrega la clave al arreglo y retorna True, False en caso contrario
    def InsertarClave(self,clave):
        
        claveRes = int(self.HashModulo(clave))  ## 1
        for i in range(self.M): ## 2n + 2
            pos = (claveRes +i) % self.M ## 3n
            if self.Arreglo[pos] == None: ## 1n
                self.Arreglo[pos] = clave  ## 1n
                return True                 ## 1n
        return False    ## 1
    ## CALCULO: 8n +4
    
    
    
    def insertarClave(self,clave):
        claveRes = self.HashModulo(clave)
        
        for i in range(self.M):
            pos = (claveRes +i) % self.N
            if self.Arreglo[pos] == None:
                self.Arreglo[pos] = clave
                return True
            
        return False
    
    def InsertarEncadenado(self,clave):
        nuevo = Nodo(clave)
        claveRes = self.HashModulo(clave)
        
        for i in range(self.M):
            pos = (claveRes+i) % self.M
            if self.Arreglo[pos] == None:
                self.Arreglo[pos] = nuevo
                return True
            else:
                aux = self.Arreglo[pos]
                while aux.siguiente != None:
                    aux = aux.siguiente
                aux.siguiente  = nuevo
        
if __name__ == "__main__":
    a = Hash()
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    a.InsertarClave(random.randint(1, 100))
    print(a.Arreglo)
    
    