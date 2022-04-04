class CasillaVotacion :
    def __init__(self, identificador, pais) :
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None
    
    @property
    def region(self):
        return self.__region

    @region.setter
    def set_region(self, new_region) :
        print(" Register of a new region ")
        if new_region in self.__pais :
            self.__region = new_region
        else :
            raise ValueError(f"La region {new_region} no es valida en {self.__pais}")


casilla = CasillaVotacion(123, ["Perú", "Colombia", "Uruguay"])
print( casilla.region )

casilla.set_region = "Bremdow"