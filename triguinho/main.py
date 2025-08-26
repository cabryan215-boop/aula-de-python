import random
def main():
    numAle = random.randint(1,30)
    num=0
    tentativas= 0
    while num != numAle:
        num = int (input("digite um numero: "))

        if num >numAle:
            print("o numero é menor que ",num)
        elif num < numAle:
            print("o numero é maior que ",num)
        print("")
        tentativas += 1
    print("voce acertou com ",tentativas,"tentativas")           
    return 0
main()    