class Grafo():
    N = 5
    Matriz: list
    
    def __init__(self):
        self.Matriz = [[None for i in range(self.N)] for j in range(self.N)]

##  Nombre: CaminoEntreVertices
##  Encabezado: CaminoEntreVertices(self,u,v)
##  funcion: verifica si existe un camino entre u y v
##  Entrada: u,v
##  Salida: retorna True si existe , False en caso contrario.

    def CaminoEntreVertices(self,u,v):
        x = self.bea(u)
        if x[v] != 999:
            return True
        else:
            return False
## hecho para recordar xd
    def bea(self,origen):
        d= [999] * self.N
        d[origen] = 0
        cola = Cola(self.N)
        cola.insertar(origen)
        while not cola.Vacia():
            eliminado = cola.suprimir()
            adyacentes = self.adyacentes(eliminado)
            for i in adyacentes:
                if d[i] == 999:
                    d[i] = d[eliminado] +1
                    cola.insertar(i)
        return d
    
                    
    def bea(self, origen):
        d= [999]* self.N
        cola = Cola(self.N)
        d[origen] = 0
        while not cola.vacia():
            eliminado = cola.suprimir()
            adyacentes = self.adyacentes(eliminado)    
            for i in adyacentes:
                if d[i] == 999:
                    d[i] = d[eliminado]+1
                    cola.insertar(i)
        return d
    
        
        
        