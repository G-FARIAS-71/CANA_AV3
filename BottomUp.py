def fibonacci(n):
    if n == 0 or n == 1:
        return n

    f = [0] * (n + 1)
    f[0] = 0
    f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]

def main():
    n = int(input("Digite um valor para n: "))

    while n < 0:
        print("n deve ser um número não-negativo.")
        n = int(input("Digite um valor para n: "))

    print("Calculando Fibonacci(n)...")
    
    for i in range(n + 1):
        print(f"Fibonacci[{i}] = {fibonacci(i)}")


if __name__ == "__main__":
    main()
    

