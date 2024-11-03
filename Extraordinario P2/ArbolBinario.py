class Nodo:
    dato: int
    izquierda: object
    derecha: object
    
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    raiz: object
    
    def __init__(self,raiz):
        self.raiz = raiz
## Nombre: hojas
## Encabezado: hojas(self,raiz)
## Funcion: busca todas las hojas dentro del arbol
## entrada: self, raiz
## Salida: imprime todas las hojas del arbol sino, retorna 0 en caso contrario
    def hojas(self,raiz): ##( n = veces que recursa)
        if raiz == None:  ## 1n
            return 0      ## 1
        
        if raiz.izquierda is None and raiz.derecha is None: ## 2n  (2 comparaciones)
            print(raiz.dato)                                ## n / 2 (aproximadamente la mitad son hojas)
            
        self.Arreglohojas(raiz.izquierda)                   ## n / 2 (la mitad del arbol)
        self.Arreglohojas(raiz.derecha)                     ## n / 2 (la otra mitad del arbol)
        ## entre las 2 llamadas seria lineal osea n ---> seria n + 1n + 2n + (n/2) + 1  = 4.5n +1
    
## CON EL METODO HOJA
    def Hojas(self,raiz):
        if raiz == None:
            return 0
        
        if raiz and self.hoja(raiz) is True:
            print(raiz.dato)
            
        self.Hojas(raiz.izquierda)
        self.Hojas(raiz.derecha)
        