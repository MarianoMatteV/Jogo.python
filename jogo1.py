import tkinter as tk
from tkinter import messagebox

def inicio():
    inicio = tk.Toplevel()
    inicio.title("Introdução")

    texto_introducao = tk.Label(inicio, text="Você e um grupo de pessoas chegaram no acampamento jurássico.")
    texto_introducao.pack()

    botao_continuar = tk.Button(inicio, text="Continuar", command=fase_1)
    botao_continuar.pack()

def fase_1():
    janela_fase1 = tk.Toplevel()
    janela_fase1.title("Terror no parque dos dinossauros")

    text_fase1 = tk.Label(janela_fase1, text="Com as bagagens já guardadas, o guia pergunta ao grupo se querem visitar o parque dos dinossauros ou ficar no acampamento.")
    text_fase1.pack()

    botao_a = tk.Button(janela_fase1, text="Você decide ir com o grupo visitar o parque dos dinossauros", command=lambda: acao_fase1('A'))
    botao_b = tk.Button(janela_fase1, text="Você decide ficar no acampamento.", command=lambda: acao_fase1('B'))

    botao_a.pack()
    botao_b.pack()

def acao_fase1(acao):
    if acao == 'A':
        janela_fase1_a = tk.Toplevel()
        texto_fase1_a = tk.Label(janela_fase1_a, text="Durante o passeio, você e seu grupo escutam algo e vão verificar.")
        texto_fase1_a.pack()
        botao_continuar_a = tk.Button(janela_fase1_a, text="Continuar", command=fase1_a)
        botao_continuar_a.pack()
    else:
        janela_fase1_b = tk.Toplevel()
        texto_fase1_b = tk.Label(janela_fase1_b, text="No acampamento você escuta algumas coisas caindo.\n Você silenciosamente vai ver o que estava acontecendo, mas algo assusta você.")
        texto_fase1_b.pack()
        botao_continuar_b = tk.Button(janela_fase1_b, text="Continuar", command=fase1_b)
        botao_continuar_b.pack()

def fase1_a():
    janela_fase1_a = tk.Toplevel()

    text_fase1_a = tk.Label(janela_fase1_a, text="Chegando no local vocês encontram um terrível dinossauro solto, o Scorpius rex. O que você faz?")
    text_fase1_a.pack()

    botao_a_fase1_a = tk.Button(janela_fase1_a, text="Corre.", command=lambda: acao_fase1_a('correr'))
    botao_b_fase1_a = tk.Button(janela_fase1_a, text="Se finge de morto.", command=lambda: acao_fase1_a('fingir'))

    botao_a_fase1_a.pack()
    botao_b_fase1_a.pack()

def acao_fase1_a(acao):
    if acao == 'correr':
        messagebox.showinfo("Resultado", "Você morreu, Scorpius gosta de caçar suas presas.")
    else:
        janela_fase2 = tk.Toplevel()
        janela_fase2 = tk.Label(janela_fase2, text="Você sobreviveu, Scorpius foi atrás das pessoas do seu grupo que correram.")
        janela_fase2.pack()
        

    botao_continuar = tk.Button(janela_fase2, text="Continuar", command=fase_2)
    botao_continuar.pack()


def fase1_b():
    janela_fase1_b = tk.Toplevel()

    text_fase1_b = tk.Label(janela_fase1_b, text="Um velociraptor estava dentro do acampamento. O que você faz?")
    text_fase1_b.pack()

    botao_a_fase1_b = tk.Button(janela_fase1_b, text="Se esconde.", command=lambda: acao_fase1_b('esconder'))
    botao_b_fase1_b = tk.Button(janela_fase1_b, text="Ataca ele", command=lambda: acao_fase1_b('atacar'))

    botao_a_fase1_b.pack()
    botao_b_fase1_b.pack()

def acao_fase1_b(acao):
    if acao == 'esconder':
        janela_fase2 = tk.Toplevel()
        janela_fase2 = tk.Label(janela_fase2, text="Ele não te achou. Você sobreviveu!")
        janela_fase2.pack()


    else:
        messagebox.showinfo("Resultado", "Você morreu, ele é mais forte que você.")

    botao_continuar = tk.Button(janela_fase2, text="Continuar", command=fase_2)
    botao_continuar.pack()

def fase_2():
    janela_fase2 = tk.Toplevel()
    janela_fase2.title("Falha na energia do parque")

    text_fase2 = tk.Label(janela_fase2, text="O dinossauro não te ataca. \n Ainda assustado com o que aconteceu, você percebe que está sozinho. \n A noite está chegando e ainda por cima a energia do parque acaba. \n O que você faz?")
    text_fase2.pack()

    botao_a_fase2 = tk.Button(janela_fase2, text="Você decide ir buscar suprimentos e alimentos no parque", command=lambda: acao_fase2('a'))
    botao_b_fase2 = tk.Button(janela_fase2, text="Você decide buscar os membros do seu grupo na floresta.", command=lambda: acao_fase2('b'))

    botao_a_fase2.pack()
    botao_b_fase2.pack()

def acao_fase2(acao):
    if acao == 'a':
        janela_fase_3 = tk.Toplevel()
        text_fase_3 = tk.Label(janela_fase_3, text="Você encontra alimentos e objetos que podem ser usados para se defender, além de encontrar alguns membros do grupo.")
        text_fase_3.pack()
    else:
        messagebox.showinfo("Resultado", "Você é atacado por um Alossauro. Você morreu!")

    botao_continuar = tk.Button(janela_fase_3, text="Continuar", command=fase_3)
    botao_continuar.pack()

def fase_3():
    janela_fase_3 = tk.Toplevel()
    janela_fase_3.title("Voltando para o acampamento")

    text_fase3 = tk.Label(janela_fase_3, text="Você e seu grupo devem voltar para o acampamento para esperar o resgate. \n Por qual caminho vocês vão?")
    text_fase3.pack()

    botao_a_fase3 = tk.Button(janela_fase_3, text="Vocês decidem ir pelo atalho (É um caminho mais perigoso).", command=lambda: acao_fase3('atalho'))
    botao_b_fase3 = tk.Button(janela_fase_3, text="Vocês decidade ir pelo caminho mais longo (É um caminho mais seguro).", command=lambda: acao_fase3('caminho_longo'))

    botao_a_fase3.pack()
    botao_b_fase3.pack()

def acao_fase3(acao):
    if acao == 'atalho':
        janela_fase3_alt = tk.Toplevel()
        text_fase3_alt = tk.Label(janela_fase3_alt, text="Durante a trajetória vocês vêem um grupo de dinossauros fugindo de algo.")
        text_fase3_alt.pack()
        botao_continuar = tk.Button(janela_fase3_alt, text="Continuar", command=fase3_alt)
        botao_continuar.pack()
    else:
        janela_fase_4 = tk.Toplevel()
        text_fase_4 = tk.Label(janela_fase_4, text="Vocês chegaram com segurança no acampamento.")
        text_fase_4.pack()

        botao_continuar = tk.Button(janela_fase_4, text="Continuar", command=fase_4)
        botao_continuar.pack()


def fase3_alt():
    janela_fase3_alt = tk.Toplevel()
    text_fase3_alt = tk.Label(janela_fase3_alt, text="Os dinossauros estavam fugindo de dois carnotauros, grandes predadores ferozes. \n Por onde você foge?")
    text_fase3_alt.pack()

    botao_a_fase3_alt = tk.Button(janela_fase3_alt, text="Vocês decidem fugir pelo parque.", command=lambda: acao_fase3_alt('parque'))
    botao_b_fase3_alt = tk.Button(janela_fase3_alt, text="Vocês decidem fugir pela floresta.", command=lambda: acao_fase3_alt('floresta'))

    botao_a_fase3_alt.pack()
    botao_b_fase3_alt.pack()

def acao_fase3_alt(acao):
    if acao == 'parque':
        janela_fase_4 = tk.Toplevel()
        text_fase_4 = tk.Label(janela_fase_4, text="Vocês conseguiram despistar os dois carnotauros e chegaram no acampamento.")
        text_fase_4.pack()
        botao_continuar = tk.Button(janela_fase_4, text="Continuar", command=fase_4)
        botao_continuar.pack()

    else:
        messagebox.showinfo("Resultado", "Vocês foram encurralados e mortos pelos carnotauros. Vocês morreram!")


def fase_4():
    janela_fase_4 = tk.Toplevel()
    janela_fase_4.title("Scorpius Rex no acampamento")

    text_fase4 = tk.Label(janela_fase_4, text="Chegando no acampamento vocês descansam um pouco, porém ouvem um barulho perturbador, algo parecido com um  rugido! \n Era Scorpius Rex, estava sedento de sangue e estava dentro do acampamento. \n O que você faz?")
    text_fase4.pack()

    botao_a_fase4 = tk.Button(janela_fase_4, text="Se esconde", command=lambda: acao_fase4('esconde'))
    botao_b_fase4 = tk.Button(janela_fase_4, text="Pega algo para atacá-lo", command=lambda: acao_fase4('atacar'))

    botao_a_fase4.pack()
    botao_b_fase4.pack()

def acao_fase4(acao):
    if acao == 'esconde':
        messagebox.showinfo("Resultado", "Você se comportou como uma presa. Scorpius achou você e te matou brutalmente!")
    else:
        janela_fase4_alt = tk.Toplevel()
        text_fase4_alt = tk.Label(janela_fase4_alt, text="Você vai buscar os itens que achou buscando suprimentos.")
        text_fase4_alt.pack()

        botao_continuar = tk.Button(janela_fase4_alt, text="Continuar", command=fase4_alt)
        botao_continuar.pack()

def fase4_alt():
    janela_fase4_alt1 = tk.Toplevel()

    text_fase4_alt1 = tk.Label(janela_fase4_alt1, text="Você encontra algumas coisas que você pegou, uma arma e um machado. Qual você pega?")
    text_fase4_alt1.pack()

    botao_a_fase4_alt1 = tk.Button(janela_fase4_alt1, text="Você pega o machado", command=lambda: acao_fase4_alt('machado'))
    botao_b_fase4_alt1 = tk.Button(janela_fase4_alt1, text="Você pega a arma", command=lambda: acao_fase4_alt('arma'))

    botao_a_fase4_alt1.pack()
    botao_b_fase4_alt1.pack()

def acao_fase4_alt(acao):
    if acao == 'machado':
        janela_fase5 = tk.Toplevel()
        text_acao_fase4_alt = tk.Label(janela_fase5, text="Você consegue acertar um golpe fatal na Scorpius, mas é atingido e fica envenenado. Mas felizmente você tinha pego um  kit médico. Você sobreviveu!")
        text_acao_fase4_alt.pack()

        botao_continuar = tk.Button(janela_fase5, text="Continuar", command=fase_5)
        botao_continuar.pack()
    else:
        messagebox.showinfo("Resultado", "Você pegou a arma mas esqueceu de pegar munição. Morto brutalmente pela Scorpius Rex!")

def fase_5():
    janela_fase5 = tk.Toplevel()
    janela_fase5.title("O resgate")

    text_fase5 = tk.Label(janela_fase5, text="Com a Scorpius morta era só esperar o resgate. \n Depois de algumas horas o resgate chega. \n O que você faz?")
    text_fase5.pack()

    botao_a_fase_5 = tk.Button(janela_fase5, text="Você decide ficar na ilha.", command=lambda: acao_fase_5('ficar'))
    botao_b_fase_5 = tk.Button(janela_fase5, text="Você entra no helicóptero e sai da ilha", command=lambda: acao_fase_5('sair'))

    botao_a_fase_5.pack()
    botao_b_fase_5.pack()    


def acao_fase_5(acao):
    if acao == 'ficar':
        messagebox.showinfo("Resultado", "Você é burro? Os dinossauros te comeram!")

    else:
        messagebox.showinfo("Resultado", "Você saiu em segurança da ilha e conseguiu voltar vivo para sua casa. \n PARABÉNS VOCÊ GANHOU!!!")


root = tk.Tk()
root.title("Aventura no Acampamento Jurássico")

botao_inicio = tk.Button(root, text="Iniciar", command=inicio)

botao_inicio.pack()


root.mainloop()