import itertools
import math
from random import randint
from typing import List, Tuple

def distancia(cidade1: int, cidade2: int, matriz_distancias: List[List[int]]) -> int:
   return matriz_distancias[cidade1 - 1][cidade2 - 1]

def caixeiro_viajante(n: int, matriz_distancias: List[List[int]], debug=False) -> Tuple[List[int], int]:
   if n != len(matriz_distancias):
      raise ValueError(f"A quantidade de cidades ({n}) deve ser igual à quantidade de linhas de matriz_distancias, tendo em vista que cada linha representa uma cidade\n{matriz_distancias = }")
   cidades = [i for i in range(1,n+1)]
   permutacoes = list(itertools.permutations(cidades))
   melhor_rota = None
   menor_distancia = math.inf

   for rota in permutacoes:
      distancia_atual = 0
      for i in range(n-1):
         distancia_atual += distancia(rota[i], rota[i+1], matriz_distancias)
      distancia_atual += distancia(rota[n-1], rota[0], matriz_distancias)

      if distancia_atual < menor_distancia:
         menor_distancia = distancia_atual
         melhor_rota = rota
         if debug:
            print(f"-> Nova melhor rota encontrada: {melhor_rota} com distância {menor_distancia}")

   return melhor_rota, menor_distancia

def matriz_distancias_aleatoria(tamanho: int, minimo: int = 10, maximo: int = 100) -> List[List[int]]:
   return [[randint(minimo, maximo) if i != j else 0 for j in range(tamanho)] for i in range(tamanho)]

if __name__ == "__main__":
   debug = input("Deseja debugar a função? (s/n): ").lower() == "s"
   matrizes_distancias = [matriz_distancias_aleatoria(i) for i in range(8, 11)]
   for i in range(3):
      print(f"--------------------------------{8+i} CIDADES-------------------------------------------------")
      matriz_distancias = matrizes_distancias[i]
      melhor_rota, menor_distancia = caixeiro_viajante(len(matriz_distancias), matriz_distancias, debug=debug)
      print(f"\ncidades = {len(matriz_distancias)} | {melhor_rota = } | {menor_distancia = }\n\n{matriz_distancias = }", end="\n\n")
      print(f"--------------------------------FIM EXECUÇÃO de {8+i} CIDADES-------------------------------------------------\n")