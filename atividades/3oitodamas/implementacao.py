from typing import Dict, List, TypeAlias
from copy import deepcopy

# Eu amo static-typing.
BoardType: TypeAlias = List[List[int]]

def empty_board(n: int) -> BoardType:
	"""
	Gera um tabuleiro `BoardType` inicializado e vazio.
	"""
	return deepcopy([[0] * n for _ in range(n)])

def print_board(board: BoardType) -> None:
	"""
	Dispõe graficamente o tabuleiro `board` em UTF-8.
	"""
	print("\n".join(" ".join("♛" if piece == 1 else "." for piece in row) for row in board))

def are_there_n_queens(board: BoardType, n: int) -> bool:
	"""
	Retorna `True` se existem `n` rainhas/damas no tabuleiro `board`.
	"""
	return sum(piece == 1 for row in board for piece in row) == n

def is_safe(board: BoardType, row: int, column: int) -> bool:
	"""
	Retorna `False` se a posição dada é insegura para uma rainha.
	Retorna `True` caso contrário.
	"""

	size = len(board)
	
	# Verifica se há outra dama na mesma linha.
	for c in range(size):
		if (board[row][c] == 1) and (c != column):
			return False

	# Verifica se há outra dama na mesma coluna.
	for r in range(size):
		if (board[r][column] == 1) and (r != row):
			return False
	
	# Verifica se há outra dama na mesma diagonal principal.
	for i in range(size):
		diagonal_row = row - column + i
		if 0 <= diagonal_row < size:
			if (board[diagonal_row][i] == 1) and ((diagonal_row, i) != (row, column)):
				return False
	
	# Verifica se há outra dama na mesma diagonal secundária.
	for i in range(size):
		diagonal_row = row + column - i
		if 0 <= diagonal_row < size:
			if (board[diagonal_row][i] == 1) and ((diagonal_row, i) != (row, column)):
				return False
	
	# Caso não haja nenhum conflito, retorne `True` (seguro).
	return True

def solve_n_queens(board: BoardType, debug: bool = False, steps: bool = False) -> None:
	"""
	Dispõe uma solução para o problema.
	"""

	# Cópia do tabuleiro fornecido.
	board_copy: BoardType = deepcopy(board)

	# N-rainhas.
	n = len(board_copy)

	# Flag de parada.
	found: bool = False

	# Iterações.
	checks: int = 0

	def backtrack(n: int, row: int = 0):

		nonlocal board_copy, found, checks

		# A flag de parada foi definida?
		# Então pare.
		if found:
			return

		# Já existem `n` rainhas?
		if are_there_n_queens(board_copy, n):
			
			# Imprima o tabuleiro.
			print_board(board_copy)
			
			# Defina a flag de "solução encontrada".
			found = True

		# Caso não, itere sobre todas as colunas.
		for column in range(len(board_copy)):

			# Caso uma solução já tenha sido encontrada, pare.
			if found:
				return

			# Adicione uma verificação.
			checks += 1

			# Verifique cada posição (row, column).
			if is_safe(board_copy, row, column):

				# Coloque uma dama na posição [row][column].
				board_copy[row][column] = 1

				if debug:
					print(f"-> Tentando a posição [{row}][{column}].")
					if steps:
						print_board(board_copy)
						print()

				# Chame recursivamente a função para colocar as outras damas.
				backtrack(n, row + 1)

				# Não há necessidade de fazer backtracking caso a solução já tenha sido encontrada.
				if found:
					return

				# Backtracking: remove a dama da posição [row][column].
				# NOTE: Caso tenha dado certo, não há necessidade de executar isso.
				board_copy[row][column] = 0

				if debug:
					print(f"<- Nenhuma posição segura, backtracking em [{row}][{column}].")
					if steps:
						print_board(board_copy)
						print()

	# Comece realizando o backtracking na primeira linha.
	backtrack(n, 0)

	if not found:
		print("Nenhuma solução encontrada.")
	else:
		print(f"{checks} posições foram verificadas.")

# Crie um tabuleiro vazio.
board: BoardType = empty_board(n = 8)

# Encontre uma solução.
solve_n_queens(board, debug = False, steps = False)