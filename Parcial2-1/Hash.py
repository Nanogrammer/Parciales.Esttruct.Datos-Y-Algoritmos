class Hash:
    N = 7500
    M = 9000
    Arreglo: list
    
    def __init__(self):
        self.Arreglo = [None] * self.N
    
    def hashModulo(self):
        return self.M % self.N
    
    
## Nombre: buscarClave
## Encabezado: buscarClave(self,clave)
## Funcion: atravez de una clave ingresada, encontrar si existe
## entrada: self, clave
## Salida: True si se encuentra la clave, False en caso contrario

    def buscarClave(self,clave):
        claveRes = self.hashModulo(clave)
        indice = claveRes % self.M
    
        for i in range(self.M):
            posicion = (indice +i) 
            if self.Arreglo[posicion] == clave:
                return True
            if self.Arreglo[posicion] == None:
                break
        return False

        
    
            
    
            
            
            
            
        