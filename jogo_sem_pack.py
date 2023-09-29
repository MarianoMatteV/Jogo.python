while True:
  print("Você chegou no acampamento jurássico")
  #FASE 1
  print("ESCOLHA UMA OPÇÃO \n (A) Você decide ir com um grupo de pessoas passear pelo parque dos dinossauros \n (B) Você decide ficar no acampamento")

  escolha_um = input("Resposta: ")
  print()
  if escolha_um != "B":
    print("No caminho vocês encontram um terrível dinossauro solto, o Scorpius rex")

    print("Você encontra a Scorpius, o que você faz? \n (A) Correr \n (B) Se fingir de morto")
    escolha_dois = input("Resposta: ")
    print()
    if escolha_dois != "B":
      print("Você morreu, Scorpius gosta de caçar suas presas.")
      continue
    else:
      print("Você sobreviveu, Scorpius foi atrás das pessoas do seu grupo que correram.")
  else:
    print("Um Utahraptor invade o acampamento")


  print("Você encontra o Utahraptor, o que você faz? \n (A) Você se esconde \n (B) Você tenta atacar o dinossauro")
  escolha_tres = input("Resposta: ")
  print()
  if escolha_tres == "A":
    print("Ele não te achou. Você sobreviveu!")
  #if escolha_tres == "B":
  else:
    print("Ele é mais forte que você. Você morreu!")
    continue

  #FASE 2:
  print("A energia do parque é cortada e você tem duas opções: \n (A) Buscar alimento e suprimentos \n (B) Procurar seu grupo")
  decisao_um = input("Resposta: ")
  print()
  if decisao_um == "A":
    print("Você encontra alimentos e objetos que podem ser usados para se defender, também encontra alguns membros do grupo")
  else:
    print("Você é atacado por um Alossauro. Você morreu!")
    continue
  #FASE 3
  print("Você e seu grupo devem voltar para o acampamento e esperar um resgate. Por qual caminho vocês vão? \n (A) Ir pelo atalho \n (B) Ir pelo caminho mais longo")
  decisao_dois = input("Resposta: ")
  print()
  if decisao_dois != "A":
    print("Vocês chegaram no acampamento seguros.")

  else:
    print("Vocês encontram 2 Carnotauros! \n (A) Fugir pelo parque \n (B) Fugir pela floresta")
    consequencia_1 = input("Resposta: ")
    print()
    if consequencia_1 != "B":
      print("Vocês conseguiram despistar os dois carnotauros e chegaram no acampamento.")
    else:
      print("Vocês foram encurralados e mortos pelos carnotauros. Vocês morreram!")
      continue

  #FASE 4
  print("Scorpius invade o acampamento, o que você faz? \n (A) Se esconder \n (B) Atacar o dinossauro")
  decisao_tres = input("Resposta: ")
  print()
  if decisao_tres == "A":
    print("Scorpius te achou e te matou")
    continue
  else:
    print("Você tem duas opções de armamentos! \n (A) Pegar o machado \n (B) Pegar a arma")
  consequencia_dois = input("Resposta: ")
  print()
  if consequencia_dois != "B":
    print("Você acertou um golpe fatal na Scorpius, mas é atingido e fica envenenado. Mas felizmente você tinha um  kit médico. Você sobreviveu!")

  else:
    print("Voce não sabia usar a arma e foi morto brutalmente pela Scorpius Rex!")
    break

  #FASE 5
  print("O helicóptero chega, o que você faz? \n (A) Você decide ficar \n (B) Você entra no helicóptero e sai ")
  decisao_final = input("Resposta: ")
  print()
  if decisao_final != "B":
    print("Você é burro? Os dinossauros te comeram.")
  else:
    print("Você sobreviveu!!!")
    break