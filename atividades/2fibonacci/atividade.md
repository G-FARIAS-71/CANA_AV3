[<img src="../../img/assets/back.png" height="35px" style="position: fixed; top: 15; opacity: 0.45">](../README.md)

# <div align="center">Exercício 2 – Fibonacci</div>

“Na matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores. A sequência recebeu o nome do matemático italiano Leonardo de Pisa ou Leonardo Fibonacci, mais conhecido por apenas Fibonacci, que descreveu, no ano de 1202, o crescimento de uma população de coelhos, a partir desta. Esta sequência já era, no entanto, conhecida na antiguidade.” (Wikipédia, 2023). 

<hr><hr>

## Passo 1: 

Construa um algoritmo de divisão-e-conquista para retornar o valor na sequência de Fibonacci de acordo com uma entrada n, um inteiro não-negativo, que indica a posição do elemento na sequência. O algoritmo deve possuir uma complexidade de tempo Θ(2^n).

<details>

   <summary>
      Clique aqui para ver a resolução do exercício
   </summary>

```rs
função fibonacci(n):
   se n igual a 0 ou n igual a 1:
      retornar n
   senão:
      retornar fibonacci(n - 1) + fibonacci(n - 2)
```

</details>

<hr>

## Passo 2: 

Para o mesmo problema do passo anterior, construa um algoritmo de programação dinâmica na abordagem top-down. O algoritmo deve possuir uma complexidade de tempo Θ(n).

<details>
   <summary>
      Clique aqui para ver a resolução do exercício
   </summary>

```rs
função fibonacci(n, memo = {}):
   se n igual a 0 ou n igual a 1:
      retornar n

   se n estiver em memo:
      retornar memo[n]

   memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
   retornar memo[n]
```

</details>

<hr>

## Passo 3: 

Para o mesmo problema do passo 1, construa um algoritmo de programação dinâmica na abordagem bottom-up. O algoritmo deve possuir uma complexidade de tempo Θ(n).

<details>
   <summary>
      Clique aqui para ver a resolução do exercício
   </summary>

```rs
função fibonacci(n):
   se n igual a 0 ou n igual a 1:
      retornar n

   f = lista de tamanho (n + 1) preenchida com 0
   f[0] = 0
   f[1] = 1

   para i de 2 a té n:
      f[i] = f[i - 1] + f[i - 2]

   retornar f[n]
```

</details>

<hr>

## Passo 4: 

Implemente os algoritmos construídos no exercício 2 utilizando a linguagem Java ou outra linguagem de programação.

<details>
   <summary>
      Clique aqui para ver a resolução do exercício
   </summary>

   ### [Passo 1](DividirConquistar.py)

   <details>
      <summary>
         Clique aqui para ver o algoritmo divisão-e-conquista
      </summary>

```py
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci(n - 1) + fibonacci(n - 2)
```

   </details>

   ### [Passo 2](TopDown.py)

   <details>
      <summary>
         Clique aqui para ver o algoritmo TopDown
      </summary>

```py
def fibonacci(n, memo = {}):
    if n == 0 or n == 1:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

   </details>

   ### [Passo 3](BottomUp.py)

   <details>
      <summary>
         Clique aqui para ver o algoritmo BottomUp
      </summary>

```py
def fibonacci(n, memo = {}):
   if n == 0 or n == 1:
      return n

   f = [0] * (n + 1)
   f[0] = 0
   f[1] = 1

   for i in range(2, n + 1):
      f[i] = f[i - 1] + f[i - 2]

   return f[n]
```

</details>

<hr>

## Passo 5: 

Para cada programa do passo anterior, modifique o código para mostrar o resultado de cada cálculo de Fibonacci até que uma saída válida seja obtida. Inclua um print com os resultados do console.

   ### [Passo 1](DividirConquistar.py)

   <details>
      <summary>
         Clique aqui para ver o algoritmo divisão-e-conquista
      </summary>

```py
def fibonacci(n):
    if n == 0 or n == 1:
      print(f'condição de parada: {n = }')
      return n
    
    termo1soma = fibonacci(n - 1)
    print({termo1soma = } quando {n = })

    termo2soma = fibonacci(n - 2)
    print({termo2soma = } quando {n = })

    soma = termo1soma + termo2soma
    print(f'({termo1soma = }) + ({termo2soma = }): {soma}')
    return soma
```

   </details>

   ### [Passo 2](TopDown.py)

   <details>
      <summary>
         Clique aqui para ver o algoritmo TopDown
      </summary>

```py
def fibonacci(n, memo = {}):
   if n == 0 or n == 1:
      print(f'condição de parada padrão do fibonacci: {n = }')
      return n

   if n in memo:
        print(f'condição de parada da programação dinâmica: {n = }')
        return memo[n]
    
    termo1soma = fibonacci(n - 1, memo)
    print({termo1soma = } quando {n = })

    termo2soma = fibonacci(n - 2)
    print({termo2soma = } quando {n = })

    memo[n] = termo1soma + termo2soma
    print(f'({termo1soma = }) + ({termo2soma = }): {memo[n]}\nNovo memo: {memo}')

    return memo[n]
```

   </details>

   ### [Passo 3](BottomUp.py)

   <details>
      <summary>
         Clique aqui para ver o algoritmo BottomUp
      </summary>

```py
def fibonacci(n, memo = {}):
   if n == 0 or n == 1:
      print(f'Condição de parada padrão do fibonacci: {n = }')
      return n

   f = [0] * (n + 1)
   f[0] = 0
   f[1] = 1

   print(f"Vetor inicial: {f}")

   for i in range(2, n + 1):
      f[i] = f[i - 1] + f[i - 2]
      print(f"{f = }")

   print(f"Vetor final: {f}")
   return f[n]
```