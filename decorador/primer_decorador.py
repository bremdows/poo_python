
# Creando un decorador en Python

# Creando la función decorador
def funcion_decoradora( funcion_parametro ) :
    def funcion_interna() :
        # Acciones adicionales añadidas
        print(" Se va a realizar un Cálculo")
        funcion_parametro()
        # Acciones adicionales que decoran
        print(" Se ha a realizado un Cálculo")
    return funcion_interna

@funcion_decoradora
def suma() :

    print( 20 + 5)

@funcion_decoradora
def resta() :

    print( 90 - 75)

suma()