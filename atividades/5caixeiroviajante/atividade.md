[<img src="../../img/assets/back.png" height="35px" style="position: fixed; top: 15; opacity: 0.45">](../README.md)

# <div align="center">Exercício 5: Caixeiro-viajante</div>

## Problemática

_"O problema do caixeiro-viajante (PCV) é um problema que tenta determinar a menor rota para percorrer uma série de cidades (visitando uma única vez cada uma delas), retornando à cidade de origem. Ele é um problema de otimização NP-difícil inspirado na necessidade dos vendedores em realizar entregas em diversos locais (as cidades) percorrendo o menor caminho possível, reduzindo o tempo necessário para a viagem e os possíveis custos com transporte e combustível."_ [(Wikipédia, 2023)](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante)

## Atividades e resolução

### Passo 1

Veja a explicação do problema do caixeiro-viajante  e construa um algoritmo força bruta para resolver o problema exaustivamente dado um pequeno número de cidades (8, 9 e 10).

<details>
   <summary style="color: lightgray">
      Clique aqui para ver a resolução
   </summary>
   <div style="border: 1px solid #ccc; margin: 10px 0;">
      <div style="display: flex; justify-content: space-between; background-color: #474a51; padding: 5px 10px; border-bottom: 1px solid #ccc;">
         <span style="font-weight: bold;">Pseudocódigo</span>
      </div>
      <pre style="margin: 0; padding: 10px; overflow: auto;"><code>CaixeiroViajanteForcaBruta(Cidades)
      n &lt;- tamanho de Cidades
      Permutacoes &lt;- gerar todas as permutações possíveis de Cidades
      MelhorRota &lt;- null
      MenorDistancia &lt;- infinito
      <br>
      para cada Rota em Permutacoes
         DistanciaAtual &lt;- 0
         para i &lt;- 1 até n-1
               DistanciaAtual &lt;- DistanciaAtual + distância entre Rota[i] e Rota[i+1]
         DistanciaAtual &lt;- DistanciaAtual + distância entre Rota[n] e Rota[1]
         <br>
         se DistanciaAtual &lt; MenorDistancia
               MenorDistancia &lt;- DistanciaAtual
               MelhorRota &lt;- Rota
      <br>
      retornar MelhorRota, MenorDistancia</code></pre>
   </div>
</details>

### Passos 2 e 3

- Implemente o algoritmo construído no passo anterior utilizando a linguagem Java ou outra linguagem de programação.
- Para o programa do passo anterior, modifique o código para mostrar cada atualização no resultado de escolhas de cidade.

<details>
   <summary style="color: lightgray">
      Clique aqui para ver a resolução
   </summary>
   <p>
      Para satisfazer ambos os passos 2 e 3, eu optei por deixar o usuário escolher se ele quer depurar o código ou não.
   </p>
   <div style="border: 1px solid #ccc; margin: 10px 0;">
      <div style="display: flex; justify-content: space-between; background-color: #474a51; padding: 5px 10px; border-bottom: 1px solid #ccc;">
         <span style="font-weight: bold; color: white;">Python</span>
         <button style="background-color: slateblue; border: none; padding: 5px 10px;"><a href="implementacao.py" style="text-decoration: none; color: white">visualizar arquivo</a></button>
      </div>
      <pre style="margin: 0; padding: 10px; overflow: auto;"><code>import itertools
import math
from random import randint
from typing import List, Tuple
<br>
def distancia(cidade1: int, cidade2: int, matriz_distancias: List[List[int]]) -&gt; int:
<span style="display: inline-block; width: 20px;"></span>return matriz_distancias[cidade1 - 1][cidade2 - 1]
<br>
def caixeiro_viajante(n: int, matriz_distancias: List[List[int]], debug=False) -&gt; Tuple[List[int], int]:
<span style="display: inline-block; width: 20px;"></span>if n != len(matriz_distancias):
<span style="display: inline-block; width: 40px;"></span>raise ValueError(f"A quantidade de cidades ({n}) deve ser igual à quantidade de linhas de matriz_distancias, tendo em vista que cada linha representa uma cidade\n{matriz_distancias = }")
<span style="display: inline-block; width: 20px;"></span>cidades = [i for i in range(1,n+1)]
<span style="display: inline-block; width: 20px;"></span>permutacoes = list(itertools.permutations(cidades))
<span style="display: inline-block; width: 20px;"></span>melhor_rota = None
<span style="display: inline-block; width: 20px;"></span>menor_distancia = math.inf
<br>
<span style="display: inline-block; width: 20px;"></span>for rota in permutacoes:
<span style="display: inline-block; width: 40px;"></span>distancia_atual = 0
<span style="display: inline-block; width: 40px;"></span>for i in range(n-1):
<span style="display: inline-block; width: 60px;"></span>distancia_atual += distancia(rota[i], rota[i+1], matriz_distancias)
<span style="display: inline-block; width: 40px;"></span>distancia_atual += distancia(rota[n-1], rota[0], matriz_distancias)
<br>
<span style="display: inline-block; width: 40px;"></span>if distancia_atual &lt; menor_distancia:
<span style="display: inline-block; width: 60px;"></span>menor_distancia = distancia_atual
<span style="display: inline-block; width: 60px;"></span>melhor_rota = rota
<span style="display: inline-block; width: 60px;"></span>if debug:
<span style="display: inline-block; width: 80px;"></span>print(f"-> Nova melhor rota encontrada: {melhor_rota} com distância {menor_distancia}")
<br>
<span style="display: inline-block; width: 20px;"></span>return melhor_rota, menor_distancia
<br>
def matriz_distancias_aleatoria(tamanho: int, minimo: int = 10, maximo: int = 100) -&gt; List[List[int]]:
<span style="display: inline-block; width: 20px;"></span>return [[randint(minimo, maximo) if i != j else 0 for j in range(tamanho)] for i in range(tamanho)]
<br>
if __name__ == "__main__":
<span style="display: inline-block; width: 20px;"></span>debug = input("Deseja debugar a função? (s/n): ").lower() == "s"
<span style="display: inline-block; width: 20px;"></span>matrizes_distancias = [matriz_distancias_aleatoria(i) for i in range(8, 11)]
<span style="display: inline-block; width: 20px;"></span>for i in range(3):
<span style="display: inline-block; width: 40px;"></span>print(f"--------------------------------{8+i} CIDADES-------------------------------------------------")
<span style="display: inline-block; width: 40px;"></span>matriz_distancias = matrizes_distancias[i]
<span style="display: inline-block; width: 40px;"></span>melhor_rota, menor_distancia = caixeiro_viajante(len(matriz_distancias), matriz_distancias, debug=debug)
<span style="display: inline-block; width: 40px;"></span>print(f"\ncidades = {len(matriz_distancias)} | {melhor_rota = } | {menor_distancia = }\n\n{matriz_distancias = }", end="\n\n")
<span style="display: inline-block; width: 40px;"></span>print(f"--------------------------------FIM EXECUÇÃO de {8+i} CIDADES-------------------------------------------------\n")</code></pre>
   </div>
</details>
