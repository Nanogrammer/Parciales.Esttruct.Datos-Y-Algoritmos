
class Digrafo:
    N = 10
    Matriz: list
    
    
    def __init__(self):
        self.Matriz = [[None for i in range(self.N)] for j in range(self.N)]
    
## nombre: fuentes
## Encabezado: fuentes(self)
## Funcion: encontrar todas las fuentes del arbol
## entrada: self
## Salida: imprime todos los nodos fuentes

    def fuentes(self):
        for i in range(len(self.Matriz)):##  2n +2 
            if self.cantEntradas(i) is None and self.cantSalidas(i) > 0: ## 2n
                print(i)                                                  ## 1n
                
                
                ## T(N(o)) = 2n² + 1n + 2 (cuadratica)
                
        