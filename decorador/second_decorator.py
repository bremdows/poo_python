# Making a second decorator in Python

""" 
    Making an ice cream without choco chips
"""

def add_choco_chips( param_function ) :
    def internal_function() :
        print("Adding choco chips")
        param_function()
        print("Ice cream with choco chips")
    return internal_function


def vanilla_icre_cream() :
    return "Vanilla icre cream"

def lucuma_ice_cream() :
    return "Lucuma ice cream"

print( vanilla_icre_cream() )

print( lucuma_ice_cream() )