class Lavadora :
    def __init__(self):
        pass

    def lavar(self, temperatura="seco") :
        print( self._llenar_tanque_agua(temperatura) )
        print( self._añadir_jabon() )
        print( self._lavar() )
        print( self._centrifugar() )
    
    def _llenar_tanque_agua(self, temperatura) :
        return "Llenando el tanque con agua\nModo de lavado: {}".format(temperatura)

    def _añadir_jabon(self) :
        return "Agregando jabon o detergente"

    def _lavar(self):
        return "Lavando la ropa"

    def _centrifugar(self):
        return "Centrifugando para secar la ropita"

if __name__ == '__main__' :
    oster = Lavadora()
    oster.lavar()