import random
import time

#Modo fácil, ado ado ado se perder é viado

golsuser = 0
golsPC = 0
print("="*20, " PENALIDADES", "="*20)
time1 = str(input("Digite o nome do seu time: "))
time2 = str(input("Digite o nome do time do computador: "))

#Disputa de penaltis
for i in range(1, 6):
    bater = str(input("Deseja bater o penalti? [S/N] ")).upper()
    if bater == "S":
        #Gera a escolha pra cobrança
        print('''╔═════════════════════╗
║  5   |  4   |  3 ║ 
║  2   |  1   |  0 ║
            ''')
        #Cobrança do usuário, defesa PC
        print("{}° Batida" .format(i))
        EscolhaUser = int(input("\033[1;34;0mAonde quer bater?\033[m "))
        EscolhaPC = random.randint(0, 5)
        if EscolhaUser <= 5 and EscolhaUser >= 0:
            if EscolhaUser != EscolhaPC:
                golsuser += 1
                print("Olha a batida...")
                time.sleep(1)
                print("\033[1;34;0mOlha o gooool!\033[m")
            elif EscolhaUser == EscolhaPC:
                print("Olha a batida...")
                time.sleep(1)
                print("\033[1;31;0mDefendeeeu!\033[m")
        else:
            time.sleep(1)
            print("\033[1;31;0mPra foraaaa!\033[m")
        print("\033[1;34;0m{}\033[m {} x {} \033[1;31;0m{}\033[m" .format(time1, golsuser, golsPC, time2))

        #cobrança do PC, defesa do usuário
    defender = str(input("Deseja defender o penalti? [S/N] ")).upper()
    if defender == "S":
        # Gera a escolha pra cobrança
        print('''╔═════════════════════╗
║  5   |  4   |  3 ║ 
║  2   |  1   |  0 ║
                ''')
        print("{}° Defesa".format(i))
        defuser = int(input("Aonde deseja defender? "))
        atakPC = random.randint(0, 6)
        if atakPC <= 5 and atakPC >= 0:
            if defuser != atakPC:
                golsPC += 1
                time.sleep(1)
                print("\033[1;31;0mOlha o goooool!\033[m")
            elif defuser == atakPC:
                time.sleep(1)
                print("\033[1;34;0mGrande defesa do goleiro\033[m")
        else:
            time.sleep(1)
            print("\033[1;34;0mPra fora, longe do gol!\033[m")
        print("\033[1;34;0m{}\033[m {} x {} \033[1;31;0m{}\033[m" .format(time1, golsuser, golsPC, time2 ))

    #Encerra o jogo caso o usuário digite "N"
    elif defender != "S":
        print("\033[1;35;0mJogo encerrado pelo usuário\033[m")
        break

    else:
        print("\033[1;35;0mJogo encerrado pelo usuário\033[1;35;0m")
        break

#Imprime o resultado da partida
print("="*20)
print("Placar final: ")
print("\033[1;34;0m{}\033[m {} x {} \033[1;31;0m{}\033[m" .format(time1, golsuser, golsPC, time2 ))


#Define quem venceu
if golsuser > golsPC:
    print("Vitória do \033[1;34;0m{}\033[m " .format(time1))
elif golsPC > golsuser:
    print("Vitória do \033[1;31;0m{}\033[m" .format(time2))

elif golsuser == golsPC:
    print("Empate!")

#dfdsf
