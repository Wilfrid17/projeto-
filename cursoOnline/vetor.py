
# Solicita ao usuário a quantidade de números que ele deseja digitar
N = int(input("Quanto numero voce deseja digitar: ?"))

# Cria uma lista (vetor) inicializada com zeros, com tamanho igual a N
vet = [0 for x in range(N)]

# Loop para preencher o vetor com os números fornecidos pelo usuário
for i in range(0, N):
    # Solicita ao usuário um número e armazena no índice correspondente do vetor
    vet[i] = float(input("Digite o numero: ?"))

# Imprime uma linha em branco para separar a entrada dos resultados
print()

# Imprime o cabeçalho "VALORES" sem quebrar a linha
print("VALORES ", end=" ")

# Loop para imprimir os valores armazenados no vetor
for i in range(0, N):
    # Imprime cada valor do vetor com uma casa decimal, sem quebrar a linha
    print(f"{vet[i]:.1f}", end="")

# Imprime uma linha em branco após os valores
print("")

# Inicializa a variável soma com 0 para calcular a soma dos valores do vetor
soma = 0

# Loop para somar todos os valores do vetor
for i in range(0, N):
    # Adiciona o valor atual do vetor à variável soma
    soma = soma + vet[i]

# Imprime a soma total dos valores com duas casas decimais
print(f"SOMA = {soma:.2f}")

# Calcula a média dos valores do vetor dividindo a soma pelo número de elementos
media = soma / N

# Imprime a média dos valores com duas casas decimais
print(f"MEDIA = {media:.2f}")