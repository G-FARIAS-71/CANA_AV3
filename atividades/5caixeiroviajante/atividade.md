[<img src="../../img/assets/back.png" height="35px" style="position: fixed; top: 15; opacity: 0.45">](../README.md)

# <div align="center">Exercício 5: Caixeiro-viajante</div>

## Problemática

O problema do caixeiro-viajante (PCV) é um problema que tenta determinar a menor rota para percorrer uma série de cidades (visitando uma única vez cada uma delas), retornando à cidade de origem. Ele é um problema de otimização NP-difícil inspirado na necessidade dos vendedores em realizar entregas em diversos locais (as cidades) percorrendo o menor caminho possível, reduzindo o tempo necessário para a viagem e os possíveis custos com transporte e combustível.” [(Wikipédia, 2023)](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante)

## Atividades e resolução

### Passo 1

Veja a explicação do problema do caixeiro-viajante  e construa um algoritmo força bruta para resolver o problema exaustivamente dado um pequeno número de cidades (8, 9 e 10).

<details>

   <summary style="color: lightgray">
        Clique aqui para ver a resolução
    </summary>
    
```rs
CaixeiroViajanteForcaBruta(Cidades)
	n <- tamanho de Cidades
	Permutações <- gerar todas as permutações possíveis de cidades
	MelhorRota <- null
	MenorDistância <- infinito
	
	para cada rota em permutações
		DistânciaAtual <- 0
		para i <- 1 até n-1
			DistânciaAtual <- DistânciaAtual + distância entre Rota[i] e Rota[i+1]
		DistânciaAtual <- DistânciaAtual + distancia entre Rota[n] e Rota[1]

		se DistânciaAtual < MenorDistância
			MenorDistancia <- DistânciaAtual
			MelhorRota <- Rota

	retornar MelhorRota, MenorDistância
```

</details>

### Passos 2 e 3

- Implemente o algoritmo construído no passo anterior utilizando a linguagem Java ou outra linguagem de programação.
- Para o programa do passo anterior, modifique o código para mostrar cada atualização no resultado de escolhas de cidade.

<details>
   <summary style="color: lightgray">
        Clique aqui para ver a resolução
    </summary>

```python
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
```

</details>