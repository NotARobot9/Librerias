from abc import ABC, abstractmethod

class AlgOrdenamiento(ABC):
	@abstractmethod
	def ordenar():
		pass

class Burbuja(AlgOrdenamiento):
	def ordenar(self, L):
		for _ in L:
			for i in range(len(L) - 1):
				if L[i + 1].menorQue(L[i]):
					L[i], L[i + 1] = L[i + 1], L[i]
                    
class Seleccion(AlgOrdenamiento):
    def ordenar(self, L):
        for i in range(len(L)):
            min_idx = i
            for j in range(i + 1, len(L)):
                if L[j].menorQue(L[min_idx]):
                    min_idx = j
            L[i], L[min_idx] = L[min_idx], L[i]
					


