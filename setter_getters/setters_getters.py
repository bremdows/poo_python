class Millas:
	def __init__(self):
		self._distancia = 0

	# Función para obtener el valor de _distancia
	# Usando el decorador property
	@property
	def obtener_distancia(self):
		print("Llamada al método getter")
		return self._distancia

	# Función para definir el valor de _distancia
	@obtener_distancia.setter
	def definir_distancia(self, valor):
		if valor < 0:
			raise ValueError("No es posible convertir distancias menores a 0.")
		print("Llamada al método setter")
		self._distancia = valor
	
	@obtener_distancia.deleter
	def del_distancia(self) :
		print("Delete the propertie distancia")
		del self._distancia

# Creamos un nuevo objeto 
avion = Millas()

# Indicamos la distancia
avion.definir_distancia = 200
# Obtenemos su atributo distancia
print(avion.obtener_distancia)
# delete the propertie 
del avion.del_distancia