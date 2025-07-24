caminho = input("Escolha um caminho, voce ira pela direita (d) ou pela esquerda (e)? ")

if caminho == 'd':

    montanha = input("Voce se deparou com uma montanha, voce ira subir (y) ou não (n)?")

    if montanha == 'y':
        print("Você tentou subir a montanha, mas escorregou e caiu 30 metros de altura, e morreu na queda.")
    
    elif montanha =='n':
        print("Você foi covarde e nao tentou subir a montanha, entao na volta voce é brutalmete morto por um gorila.")

    else:
        print("Você ficou indeciso com a escolha, então uma pedra caiu da montanha, te esmagando")


elif caminho == 'e':

    rio = input("Você se deparou com um rio, voce vai atravessalo (y) ou não (n) ")

    if rio == 'y':
        print("Foi tentou atravessar o rio, mas o rio te puxou e voce caiu de uma cachoeira de 40 metros de altura, morrendo na queda.")
    
    elif rio == 'n':
        print("Você é um medroso, entao decidiu voltar, mas na volta você foi brutalmente devorado por uma onça.")
    
    else:
        print("Você ficou indeciso com a escolha, então uma cobra te picou e você morreu em menos de uma hora.")

else:
    print("Você decidiu voltar para casa.")
    