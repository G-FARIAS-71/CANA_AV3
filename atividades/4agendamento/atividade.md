[<img src="../../img/assets/back.png" height="35px" style="position: fixed; top: 15; opacity: 0.45">](../../README.md)

# <div align="center">Exercício 4: Agendamento</div>

## Problemática

_Sua empresa de desenvolvimento de software recebeu muitas ofertas de projeto para o ano de 2024 e seus analistas projetaram quando os projetos seriam iniciados e concluídos, além de calcular um valor de lucro para cada projeto. Em outras palavras, cada oferta possui uma data de início, uma data de conclusão e um valor de lucro. Como os projetos são muitos e existem conflitos de data, será necessário fazer uma escolha entre quais projetos serão desenvolvidos._

## Resolução

### Passo 1

- De acordo com o cenário acima, construa um algoritmo guloso para escolher quais projetos serão desenvolvidos. O algoritmo deve receber como entrada a lista de projetos, com data inicial, data final e um número real de lucro.

<details>
    <summary style="color: lightgray">
        Clique aqui para ver a resolução
    </summary>

```rs
ROTINA TEM_CONFLITO(A, B)

	SE [A está em conflito com B] 
		RETORNE FALSO
	CASO CONTRÁRIO
		RETORNE VERDADEIRO

ROTINA RESOLVER_AGENDAMENTO_DE_PROJETOS(PROJETOS, CRITÉRIO)

	ORDENAR(PROJETOS, CRITÉRIO)

	SELECIONADOS := []

	PARA CADA PROJETO EM PROJETOS [1]

		PARA CADA SELECIONADO EM SELECIONADOS [2]

			SE TEM_CONFLITO(PROJETO, SELECIONADO) ENTÃO
				PULE A ITERAÇÃO EM [1] E CONTINUE (continue/skip)

		ADICIONAR(PROJETO, SELECIONADOS)

    IMPRIMIR SELECIONADOS
```
</details>

### Passos 2 e 3

- Implemente o algoritmo construído no passo anterior utilizando a linguagem Java ou outra linguagem de programação.
- Para o programa do passo anterior, modifique o código para mostrar cada seleção assim que é realizada.

<details>
    <summary style="color: lightgray">
        Clique aqui para ver a resolução
    </summary>

```python
from datetime import datetime
from typing import Dict, List, TypeAlias
from typing_extensions import Self

class Project:

	name: str
	start: datetime
	finish: datetime
	
	duration: int
	profit: float

	ratio: float

	def __init__(self, name: str, start: str, finish: str, profit: int | float) -> None:
		
		# O nome do projeto.
		self.name = name

		# Converta as datas de `str` para `datetime`.
		self.start = datetime.strptime(start, "%d/%m/%Y")
		self.finish = datetime.strptime(finish, "%d/%m/%Y")
		self.duration = (self.finish - self.start).days

		# Aqui está o lucro.
		self.profit = profit

		# Aqui está uma proporção entre o lucro e duração (lucro por dia).
		self.ratio = self.profit / self.duration

	def __repr__(self) -> str:
		delta = self.finish - self.start
		return f"Project(\"{self.name}\", {delta.days} day(s), R${self.profit:,.2f})"

	def conflicts_with(self, other: Self) -> bool:
		return not ((self.finish < other.start) or (other.finish < self.start))

ProjectList: TypeAlias = List[Project]

def solve_project_scheduling(projects: ProjectList) -> None:

	# Ordenar os projetos com base em um critério!
	projects.sort(key = lambda x: (x.finish, x.ratio), reverse = True)

	# Este serão os projetos escolhidos.
	selected_projects: ProjectList = []

	# Para cada projeto possível..
	for project in projects:

		# Esta flag serve para indicar que houve conflito.
		flag: bool = False

		# Verifique se todos os projetos funcionam com o projeto.
		for selected in selected_projects:
		
			# Se existe algum conflito, então não vai funcionar.
			if project.conflicts_with(selected):
				flag = True
				break

		# Se algum projeto deu conflito, não adicione-o.
		if flag:
			continue

		# Caso não deu conflito, adicione-o.
		selected_projects.append(project)

	# Custo total.
	total: float = 0.0

	print(f"Projetos Selecionados ({len(selected_projects)} projeto(s)):\n")
	for project in selected_projects:
		print("->", project)
		total += project.profit

	# Agora, re-ordene por data.
	selected_projects.sort(key = lambda x: x.finish)

	print()
	print(str("\n".join(project.start.strftime("%d/%m/%Y") + " até " + project.finish.strftime("%d/%m/%Y") for project in selected_projects)))

	print(f"\nLucro Total: R$ {total:,.2f}")

solve_project_scheduling([
	
	Project("Projeto A", "01/01/2023", "02/01/2023", 20_000),
	Project("Projeto B", "03/01/2023", "05/01/2023", 30_000),
	Project("Projeto C", "06/01/2023", "10/01/2023", 25_000),
	Project("Projeto D", "06/01/2023", "12/01/2023", 40_000),
	Project("Projeto E", "08/01/2023", "15/01/2023", 15_000),
	Project("Projeto F", "10/01/2023", "20/01/2023", 35_000),
	Project("Projeto G", "12/01/2023", "18/01/2023", 28_000),
	Project("Projeto H", "13/01/2023", "25/01/2023", 60_000),
	Project("Projeto I", "15/01/2023", "23/01/2023", 45_000),
	Project("Projeto J", "17/01/2023", "21/01/2023", 12_000),
	Project("Projeto K", "18/01/2023", "30/01/2023", 55_000),
	Project("Projeto L", "20/01/2023", "25/01/2023", 22_000),
	Project("Projeto M", "22/01/2023", "28/01/2023", 38_000),
	Project("Projeto N", "24/01/2023", "31/01/2023", 70_000),
	Project("Projeto O", "26/01/2023", "30/01/2023", 32_000)

])
```
</details>