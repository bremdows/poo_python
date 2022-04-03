# Making a second decorator in Python

""" 
    Making an ice cream without choco chips
"""

from audioop import add


def add_choco_chips( param_function ) :
    def internal_function() :
        print("Adding choco chips")
        print( param_function() )
        print("Ice cream with choco chips\n")
    return internal_function

@add_choco_chips
def vanilla_icre_cream() :
    return "Vanilla ice cream"
@add_choco_chips
def lucuma_ice_cream() :
    return "Lucuma ice cream"

vanilla_icre_cream()

lucuma_ice_cream()