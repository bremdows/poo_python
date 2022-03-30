class Automovil :
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "Reposo"
        self._motor = Motor(cilindros=4)
        self._puertas = Puertas(color, 4)

    def acelerar(self, tipo="lento") :
        salida = ""
        if tipo == 'veloz' :
            salida = self._motor.inyecta_gasolina(10)
        else :
            salida = self._motor.inyecta_gasolina(3)
        
        self._estado = "Movimiento"
        return salida

    def frenar( self ) :
        
        self._estado = "Reposo"
        return self._motor.inyecta_gasolina(0)

class Puertas :
    def __init__(self, color, nro_puertas) :
        self.color = color 
        self.nro_puertas = nro_puertas
        self._tipo = "Electrico"

class Motor :
    def __init__(self, cilindros, tipo="gasolina"):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self, cantidad):
        if cantidad == 0 and cantidad >= 0:
            return f"Se dejo de inyectar gasolina, frenando el automovil ..."
        else :
            return f"Se inyecto {cantidad} de gasolina"


tesla = Automovil("Model E", "Tesla", "Negro")
print( tesla.acelerar() )
print( "Estado del auto: En", tesla._estado )
print( tesla.frenar() )
print( "Estado del auto: En", tesla._estado )

