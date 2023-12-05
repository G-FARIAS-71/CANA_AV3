[<img src="../../img/assets/back.png" height="35px" style="position: fixed; top: 15; opacity: 0.45">](../README.md)

# <div align="center">Exercício 1: Ordenação</div>

1 - Para um vetor sobre o domínio dos números inteiros positivos, desejamos resolver o problema de ordenação dos elementos deste vetor em ordem decrescente. Construa três algoritmos para resolver este problema, utilizando pelo menos uma vez cada um dos seguintes paradigmas algorítmicos: força bruta e divisão e conquista.

2 - Implemente os algoritmos de ordenação construídos no passo anterior utilizando a linguagem Java ou outra linguagem de programação.

3 - Para cada programa do passo anterior, modifique o código para mostrar cada atualização feita no vetor de entrada até que uma saída válida seja obtida. Inclua um print com os resultados do console.

<hr>

<details>

   <summary style="color: lightgray">
        Clique aqui para ver a resolução
    </summary>

Em busca de satisfazer os requisitos dessa atividade, foram escolhidos três algoritmos: insertion sort, quick sort e bubble sort.

Abaixo estão os pseudocódigos e as implementações em java de cada algoritmo.

Porém, antes de apresentá-los, será mostrada a função em java utilizada na classe para printar os elementos do array, o que auxilia no debug.

```java
public static void imprime(int []v) {
	for(int i=0;i<v.length;i++) {
		System.out.print(v[i]+" ");
	}
	System.out.println();
}
```

Além disso, gostaria de ressaltar que as implementações estão em formato de funções que devem estar dentro de uma classe; afinal de contas, se não fosse assim, não seria java.

## Insertion Sort (força bruta) 

   <details>
      <summary style="color: lightgray">
         Clique aqui para ver o pseudocódigo e a implementação do insertion sort
      </summary>

### Pseudocódigo
```rs
procedimento InsertionSort(a1,a2,a3,...an)
   para j de 2 até n
      x<-aj
      i<-j-1
      enquanto i>0 e ai>x
         ai+1<-ai
         i<-i-1
      ai+1<-x
```

### Implementação
```java
public static void InsertionSort(int []v) {
	int aux;
	int j;
	for(int i=1;i<v.length;i++) {
		aux=v[i];
		j=i;
		while(j>0 && v[j-1]<aux) {
			v[j]=v[j-1];
			j--;
		}
		v[j]=aux;
		imprime(v);
	}
}
```

   </details>

## Quick Sort (divisão e conquista)

   <details>
      <summary style="color: lightgray">
         Clique aqui para ver o pseudocódigo e a implementação do quick sort
      </summary>

### Pseudocódigo
```rs
procedimento QuickSort(a1,a2,a3,...an,p,r)
   se p<r
      q<-Partition(a1,a2,a3,...an,p,r)
      QuickSort(a1,a2,a3,...an,p,q-1)
      QuickSort(a1,a2,a3,...an,q+1,r)

funcao Partition(a1,a2,a3,...an,p,r)
   x<-ar
   i<-p-1
   para j de p até r-1
      se aj>=x então
         i<-i+1
         trocar ai com  aj
   trocar ai+1 com ar
   retornar i+1
```

### Implementação
```java
public static void QuickSort(int[]v){
	QuickSort(v,0,v.length-1);
}
private static void QuickSort(int[]v,int p,int r) {
	if(p<r) {
		int q = Partition(v,p,r);
		QuickSort(v,p,q-1);
		QuickSort(v,q+1,r);
	}
}
private static int Partition(int[]v,int p,int r) {
	int x=v[r];
	int i=p-1;
	imprime(v);
	for(int j=p;j<r;j++) {
		if(v[j]>=x) {
			i++;
			int aux=v[i];
			v[i]=v[j];
			v[j]=aux;
			imprime(v);
		}
	}
	int aux=v[i+1];
	v[i+1]=v[r];
	v[r]=aux;
	imprime(v);
	return i+1;
}
```

   </details>

## Bubble Sort (força bruta)

   <details>
      <summary style="color: lightgray">
         Clique aqui para ver o pseudocódigo e a implementação do bubble sort
      </summary>

### Pseudocódigo
```rs
procedimento BubbleSort(a1,a2,a3,...an)
para i de 1 até n
	para j de 1 até n-i
		se aj<aj+1 então troque aj com aj+1
```

### Implementação
```java
public static void BubbleSort(int []v) {
	imprime(v);
	for(int i=0;i<v.length-1;i++) {
		for(int j=0;j<v.length-1-i;j++) {
			if(v[j]<=v[j+1]) {
				int aux=v[j];
				v[j]=v[j+1];
				v[j+1]=aux;
				imprime(v);
			}
		}
	}
}
```
   </details>
</details>