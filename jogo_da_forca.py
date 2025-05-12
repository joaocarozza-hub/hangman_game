import random

# Lista de palavras
palavras = ['brigadeiro', 'morango', 'chocolate', 'beijinho', 'doce', 'confeito', 'leite', 'granulado']

# Escolhe uma palavra aleatória
palavra = random.choice(palavras).lower()
letras_certas = []
tentativas = 6

print("Bem-vindo ao Jogo da Forca!")
print("Adivinhe a palavra relacionada a docinhos")

# Loop principal
while tentativas > 0:
    exibicao = ''
    for letra in palavra:
        if letra in letras_certas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '

    print("\nPalavra: ", exibicao.strip())

    if '_' not in exibicao:
        print("Parabéns! Você adivinhou a palavra:", palavra)
        break

    tentativa = input("Digite uma letra: ").lower()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra.")
        continue

    if tentativa in letras_certas:
        print("Você já tentou essa letra.")
        continue

    if tentativa in palavra:
        letras_certas.append(tentativa)
        print("Letra correta!")
    else:
        tentativas -= 1
        print(f"Letra errada! Você ainda tem {tentativas} tentativa(s).")

if tentativas == 0:
    print(f"\nFim de jogo! A palavra era: {palavra}")
