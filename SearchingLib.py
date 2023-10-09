from abc import ABC, abstractmethod

class AlgBusqueda(ABC):
	@abstractmethod
	def buscar(self):
		pass
class OperacionInvalida(Exception):
	pass

class Binaria(AlgBusqueda):
	def buscar(self, L, item):
		if len(L) == 0:
			raise OperacionInvalida("El elemento no está en la colección")

		idxMedio = len(L) // 2

		if L[idxMedio] == item:
			return idxMedio
		elif L[idxMedio].menorQue(item):
			self.Binaria([L[i] for i in range(idxMedio + 1, len(L))], item)
		else:
			self.Binaria([L[i] for i in range(0, idxMedio)], item)