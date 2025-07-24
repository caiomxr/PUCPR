import random


def tamanho_tabu():
    while True:
        print("Você quer o tabuleiro 5x10 ou 10x10?")
        tam_tabu = input("1 - 5x10 || 2 - 10x10: ")

        if tam_tabu == "1":
            linhas = 5
            colunas = 10
            break
        elif tam_tabu == "2":
            linhas = 10
            colunas = 10
            break
        else:
            print("Opção inválida")
    return linhas, colunas, tam_tabu


def tabuleiro(linhas, colunas, caractere='💧'):
    tabuleiroo = [[caractere for _ in range(colunas)] for _ in range(linhas)]
    return tabuleiroo


def colocar_navios(tabuleiroo, tam_tabu):
    print("Posicione seus navios (5)")
    if tam_tabu == "1":
        prompt_linha = "Qual linha você quer colocar o navio? (0-4): "
        prompt_coluna = "Qual coluna você quer colocar o seu navio? (0-9): "
    else:
        prompt_linha = "Qual linha você quer colocar o navio? (0-9): "
        prompt_coluna = "Qual coluna você quer colocar o seu navio? (0-9): "

    navios_posicionados = 0
    while navios_posicionados < 5:
        print(f"Posicionando navio {navios_posicionados + 1} de 5")
        linha = int(input(prompt_linha))
        colun = int(input(prompt_coluna))

        if tabuleiroo[linha][colun] == '🚢':
            print("Você já tem um navio nessa posição")
        else:
            tabuleiroo[linha][colun] = '🚢'
            print(f"Navio posicionadoem ({linha}, {colun})!")
            navios_posicionados += 1
    return tabuleiroo


def colocar_navios_pc(tabuleiroo_pc, tam_tabu):
    print("O computador está colocando os navios")
    navios_posicionados = 0
    while navios_posicionados < 5:
        if tam_tabu == "1":
            linha_pc = random.randint(0, 4)
            colun_pc = random.randint(0, 9)
        else:
            linha_pc = random.randint(0, 9)
            colun_pc = random.randint(0, 9)

        if tabuleiroo_pc[linha_pc][colun_pc] == '💧':
            tabuleiroo_pc[linha_pc][colun_pc] = '🚢'
            navios_posicionados += 1
    print("O computador posicionou todos os navios")
    return tabuleiroo_pc


def turno_do_jogador(tabuleiro_oculto, tabuleiro_pc, tam_tabu):

    print("Sua vez")

    if tam_tabu == "1":
        prompt_linha = "Linha do seu tiro (0-4): "
        prompt_coluna = "Coluna do seu tiro (0-9): "
    else:
        prompt_linha = "Linha do seu tiro (0-9): "
        prompt_coluna = "Coluna do seu tiro (0-9): "

    while True:
        linha_tiro = int(input(prompt_linha))
        coluna_tiro = int(input(prompt_coluna))

        if tabuleiro_pc[linha_tiro][coluna_tiro] in ['🔥', '❌']:
            print("Escolha outra (Você ja atirou nessa posição")
        else:
            break

    if tabuleiro_oculto[linha_tiro][coluna_tiro] == '🚢':
        print("Você ecertou")
        tabuleiro_pc[linha_tiro][coluna_tiro] = '🔥'
        return True
    else:
        print("Você errou")
        tabu_pc[linha_tiro][coluna_tiro] = '❌'
        return False


def turno_computador(tabuleiro_jogador, linhas, colunas):

    print("Vez do Computador")

    while True:
        linha_pc = random.randint(0, linhas - 1)
        coluna_pc = random.randint(0, colunas - 1)

        if tabuleiro_jogador[linha_pc][coluna_pc] not in ['🔥', '❌']:
            break

    print(f"O computador atirou em ({linha_pc}, {coluna_pc})")

    if tabuleiro_jogador[linha_pc][coluna_pc] == '🚢':
        print("O computador acertou um dos seus navios")
        tabuleiro_jogador[linha_pc][coluna_pc] = '🔥'
        return True
    else:
        print("Computador errou")
        tabuleiro_jogador[linha_pc][coluna_pc] = '❌'
        return False



def exibir_tabu(tab_jogador, tabu_visivel):


    num_colunas = len(tab_jogador[0])
    header_colunas = " ".join(map(str, range(num_colunas)))


    print("\n" + "=" * 40)
    print("SEU TABULEIRO")
    print(f"   {header_colunas}")
    for i, linha in enumerate(tab_jogador):
        print(f"{i:<2} {' '.join(linha)}")


    print("\n" + "~" * 40 + "\n")


    print("SEUS ATAQUES NO COMPUTADOR")
    print(f"   {header_colunas}")
    for i, linha in enumerate(tabu_visivel):
        print(f"{i:<2} {' '.join(linha)}")
    print("=" * 40)




linhas_jogo, colunas_jogo, tamanho_escolhido = tamanho_tabu()


tabu_navios = colocar_navios(tabuleiro(linhas_jogo, colunas_jogo), tamanho_escolhido)


tabu_oculto = colocar_navios_pc(tabuleiro(linhas_jogo, colunas_jogo), tamanho_escolhido)
tabu_pc = tabuleiro(linhas_jogo, colunas_jogo)


jogador_restantes = 5
navios_pc_restantes = 5

while True:
    exibir_tabu(tabu_navios, tabu_pc)
    print(f"Navios restantes: Você ({jogador_restantes}) - Computador ({navios_pc_restantes})")

    if turno_do_jogador(tabu_oculto, tabu_pc, tamanho_escolhido):
        navios_pc_restantes -= 1

    if navios_pc_restantes == 0:
        print("Vitoria!")
        exibir_tabu(tabu_navios, tabu_pc)
        break

    input("Pressione Enter para a vez do computador")

    if turno_computador(tabu_navios, linhas_jogo, colunas_jogo):
        jogador_restantes -= 1

    if jogador_restantes == 0:
        print("Derrota")
        exibir_tabu(tabu_navios, tabu_pc)
        break