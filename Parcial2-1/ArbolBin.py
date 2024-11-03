class Nodo():
    dato: int
    izquierda: object
    derecha: object
    def __init__(self, dato=None):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
    def __str__(self):
        return f"{self.dato}"

class ArbolBinario:
    raiz: object
    
    def __init__(self, raiz):
        self.raiz = raiz

## METODO INSERTAR    
    def insertar(self,dato,raiz):
        nuevo = Nodo(dato)
        if raiz == None:
            raiz = nuevo
        
        if raiz and dato < raiz.dato:
            if raiz.izquierda == None:
                raiz.izquierda = nuevo
            else:
                self.insertar(dato, raiz.izquierda)
        elif raiz and dato > raiz.dato:
            if raiz.derecha == None:
                raiz.derecha = nuevo
            else:
                self.insertar(dato, raiz.derecha)
                
## ESTE METODO COMBINA EL METODO "buscarNodo()" Y EL METODO "descendientes()" PARA HALLAR LOS DESCENDIENTES DE UN NODO INGRESADO.
    def cantDesc(self,Vnodo,raiz):                                              
        cant = 0 # t(o) =1
        x = self.buscarNodo(Vnodo,raiz) # t(o) = 2n
        
        if x is None: # t(o) =1
            return cant # t(o) =1
        
        desc = self.descendientes(x, cant) # t(o) = 2n
        return desc # t(o) =1                            ##### COMPLEJIDAD 4n + 4

## ESTE METODO BUSCA UN NODO EN EL ARBOL PRINCIPAL 
    def buscarNodo(self,Nodo,raiz):
        if Nodo == raiz.dato:
            return raiz
        self.buscarNodo(Nodo, raiz.izquierda)
        self.buscarNodo(Nodo, raiz.derecha)
        return None

## ESTE METODO BUSCA LOS DESCENDIENTES DE UN NODO DADO. (QUE PRIMERO DEBE SER ENCONTRADO EN EL ARBOL PRINCIPAL)    
    def descendientes(self, nodo, cant):
        
        if nodo == None:
            return 0
        
        return 1 + self.descendientes(nodo.izquierda, cant) + self.descendientes(nodo.derecha, cant)
    
            
if __name__ == "__main__":
    arbol = ArbolBinario(Nodo(5))
    arbol.insertar(3, arbol.raiz)
    arbol.insertar(7, arbol.raiz)
    arbol.insertar(2, arbol.raiz)
    arbol.insertar(4, arbol.raiz)
    arbol.insertar(6, arbol.raiz)
    arbol.insertar(8, arbol.raiz)
    a = arbol.cantDesc(5, arbol.raiz)
    print(f"El nodo 5 tiene: {a} descendientes.")
            
            
        
        