def divisoria():
    print("----------------------------------------------------")
#Imprima os números de 1 a 10 com laço while:
divisoria()
numero = 1
print("Contando de 1 a 10:")
while numero <= 10:
    print(numero)
    numero +=1

#Imprimindo os números de 10 a 1 com laço while:
divisoria()
numero2 = 10
print("Contando de 10 a 1: (Ordem decrescente)")

while numero2 >=1:
    print(numero2)
    numero2 -=1

#Solicite ao usuário um número e repita o programa até que o usuário digite 0:
divisoria()
print("Acerte o número que estou pensando: ")
numero3 = int(input("Digite um número: "))
while numero3 != 0:
    print("Você digitou:", numero3,"... Esse não é o número que estou pensando")
    numero3 = int(input("Digite um número: "))
# Esse bloco abaixo não funcionou como esperado e foi mantido apenas
# como referência de código incorreto.
# if numero3 == 0:
#     print("Parabéns, você acertou!")
#     break
# else:
#     numero3 = int(input("Digite um número: "))

print("Parabéns, você acertou!")

#O mesmo exercício agora usando o IF para verificar
#Aqui ia criar um loop infinito, que será quebrado quando a condição do if for satisfeita
divisoria()
print("Acerte o número que estou pensando: (Usando IF)")
while True:
    numero4 = int(input("Acerte o número que estou pensando: "))
    if numero4 == 0:
        print("Parabéns, você acertou!")
        break
    else:
        print("Você digitou:", numero4, "... Esse não é o número que estou pensando")
