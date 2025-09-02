def main():
    quantAlunos= int(input("digite a quantidade novamente"))
    while quantAlunos<1:
        print("numero invalido,digite novamente ")
        quantAlunos=int(input("digite a quantidade de alunos:"))
    nomes=[""]*quantAlunos    
    i=0
    while i in range (len(nomes)):
        nomes[i]=input("digite o nome do aluno: ")
        i += 1
    print(nomes)
    return 0
main()    