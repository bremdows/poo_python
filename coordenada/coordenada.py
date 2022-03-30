# Definiendo un clase coordenada en Python
class Coordenada :
    def __init__ (self, x, y) :
        self.x = x
        self.y = y
    
    def distancia(self, otra_coordenada):
        return ( (self.x - otra_coordenada.x)**2 + (self.y - otra_coordenada.y)**2 )**0.5
    


if __name__ == '__main__' :
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print("Distancia entre la coordenada 1 y 2 es:", coord_1.distancia( coord_2) )
    print( isinstance(coord_1, Coordenada))

## Determinar si un objeto es instancia de una clase