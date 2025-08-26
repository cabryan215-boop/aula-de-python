def main():
    altura= float ( input("digite a sua altura: "))
    idade=int1
    (input("digite a sua idade: "))
    isCasado= (input("vc é casado?: "))
    sexo=input("digite seu sexo: ")
    nome=input("digite seu nome: ")
    peso=float(input("digite seu peso: "))
    cpf=input("digite seu cpf: ")

    print("o",nome,"mede",altura,"de altura,tem",idade ,"anos de idade")
    print("É do sexo", sexo,",pesa",peso,"kg e seu cpf É:",cpf)
    if isCasado == "S" or isCasado == "s":
        print("o",nome,"é casado")
    elif isCasado == "sou" or isCasado == "Sou":
        print("o",nome,"é casado")
    else:
        print("o",nome,"se divorciou recentemente")

    return 0
main()