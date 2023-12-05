def fibonacci(n, memo = {}):
    if n == 0 or n == 1:
        return n
    
    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


def main():
    n = int(input("Digite um valor para n: "))

    while n < 0:
        print("n deve ser um número não-negativo.")
        n = int(input("Digite um valor para n: "))

    print("Calculando Fibonacci(n)...")

    while n >= 0:
        print(f"Fibonacci({n}) = {fibonacci(n)}")
        n -= 1


if __name__ == "__main__":
    main()
    