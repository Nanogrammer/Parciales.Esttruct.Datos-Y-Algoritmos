class Nodo():
    dato: int
    izquierda: object
    derecha: object
    
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        

class Arbol:
    raiz: object
    
    def __init__(self,raiz):
        self.raiz = Nodo(raiz)
        
    def insertar(self,dato,raiz):
        nuevo = Nodo(dato)
        if raiz == None:
            raiz = nuevo
        
        if raiz and raiz and dato < raiz.dato:
            if raiz.izquierda == None:
                raiz.izquierda = nuevo
            else:
                self.insertar(dato, raiz.izquierda)
        elif raiz and raiz and dato > raiz.dato:
            if raiz.derecha == None:
                raiz.derecha = nuevo
            else:
                self.insertar(dato, raiz.derecha)
                    
    def inorden(self,raiz):
        
        if raiz == None:
            return 
        self.inorden(raiz.izquierda)
        print(raiz.dato)
        self.inorden(raiz.derecha)
        
        
        
## Nombre: calcularGrado
## Encabezado: calcularGrado(self, nodo, raiz)
## FUncion: atravez de un nodo ingresado por teclado, hallar el grado de ese nodo
## entrada: self, nodo, raiz
## salida: retorna el grado del nodo, 0 si no existe el nodo
    def calcularGrado(self,nodo,raiz):
        if raiz == None:
            return 0
        
        if nodo == raiz.dato:
            grado = 0
            if raiz.izquierda:
                grado+=1
            if raiz.derecha:
                grado+=1
            return grado
        else:
            if nodo < raiz.dato:
                return self.calcularGrado(nodo, raiz.izquierda)
            else:
                return self.calcularGrado(nodo, raiz.derecha)
            

## Nombre: altura (del arbol)
## Encabezado: altura(self, raiz)
## FUncion: encontrar la altura total del arbol
## entrada: self, raiz
## salida: retorna el numero de arcos de la rama maxima

    def altura(self,raiz):
        if raiz == None:
            return 0
        
        if self.altura(raiz.izquierda) > self.altura(raiz.derecha):
            return 1 + self.altura(raiz.izquierda)
        
        else:
            return 1 + self.altura(raiz.derecha)
        
        
if __name__ == "__main__":
    arbol = Arbol(40)
    arbol.insertar(50, arbol.raiz)
    arbol.insertar(30, arbol.raiz)
    arbol.insertar(20, arbol.raiz)
    arbol.insertar(70, arbol.raiz)
    arbol.insertar(60, arbol.raiz)
    arbol.insertar(80, arbol.raiz)
    arbol.inorden(arbol.raiz)
    a = arbol.calcularGrado(40, arbol.raiz)
    print(f"El grado del nodo 40 es: {a}")
    altura = arbol.altura(arbol.raiz)
    print(f"Altura: {altura}")
    