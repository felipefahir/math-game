from tkinter import * 
from random import randint
from time import sleep
import os
import math


cont = 0
vez = 0

janela = Tk()
janela.title("Jogo Matematico")
janela.iconbitmap('simbolo-de-matematica.png')


def Choese():
    global btn4,btn3,btn2,btn1,label
    label = Label(janela, text=('escolha um para iniciar o game'))
    label.grid(column=0, row=0)
    sleep(1)
   #Multiplicação
    btn1 = Button(janela, text="Multiplicação", command=nunMulti)
    btn1.grid(column=0, row=1)
   #Divisão
    btn2 = Button(janela, text="Divisão", command=nunDivi)
    btn2.grid(column=1, row=1)
   #Adição
    btn3 = Button(janela, text="Adição", command=nunAdi)
    btn3.grid(column=2, row=1)
   #Subtração
    btn4 = Button(janela, text="Subtração", command=nunSub)
    btn4.grid(column=3, row=1)


def nunMulti():
    global top,res, rannun2, rannun1, reslabel
    
    top = nunMulti
    rannun1 = randint(1, 1000)
    rannun2 = randint(1,1000)
    res = rannun1*rannun2 
    reslabel = Label(janela, text=f'{rannun1} x {rannun2} = ')
    reslabel.grid(column=0, row=0)
    check()


def nunDivi():
    global top,res, rannun2, rannun1, reslabel
    
    top = nunDivi
    rannun1 = randint(1, 1000)
    rannun2 = randint(1,500)
    res = math.floor(rannun1/rannun2 )
    reslabel = Label(janela, text=f'{rannun1} : {rannun2} = ')
    reslabel.grid(column=0, row=0)
    check()


def nunAdi():
    global top,res, rannun2, rannun1, reslabel
    
    top = nunAdi
    rannun1 = randint(1, 1000)
    rannun2 = randint(1,1000)
    res = rannun1+rannun2 
    reslabel = Label(janela, text=f'{rannun1} + {rannun2} = ')
    reslabel.grid(column=0, row=0)
    res = str(res)

    check()


def nunSub():
    global top,res, rannun2, rannun1 , reslabel
    
    top = nunSub
    rannun1 = randint(1, 1000)
    rannun2 = randint(1,1000)
    res = rannun1-rannun2 
    reslabel = Label(janela, text=f'{rannun1} - {rannun2} = ')
    reslabel.grid(column=0, row=0)
    check()




def verificar():
    global yget_res,yres,cont
    yget_res = yres.get()
    str_res = f'{res}'
    
    if yget_res in str_res:
        cont = cont + 1
        yres.destroy()
        verifica.destroy()
        correto = Label(janela ,text="Correto")
        correto.grid(column=0, row=0)

        top()
    else:
        ttop = top
        yres.destroy()
        verifica.destroy()
        reslabel.destroy()

        error = Label(janela, text=f'''ERRADO 
A resposta certa seria {res}''')
        error.grid(column=0, row=0)
        

        def Keep():
            btn_keeporpass1.destroy()
            btn_keeporpass2.destroy() 
            error.destroy()
            error_2.destroy()
            yres.destroy()
            verifica.destroy()
            reslabel.destroy()
            ttop() 

        def Pass():

            h4 = Label(janela, text=f'Seu acerto foi de {cont}/{vez}')
            h4.grid(column=0, row=0)
            btn_keeporpass1.destroy()
            btn_keeporpass2.destroy() 
            error.destroy()
            error_2.destroy()
            yres.destroy()
            verifica.destroy()
            reslabel.destroy()


        error_2 = Label(janela, text="Quer continuar?")
        error_2.grid(column=0, row=1)
        btn_keeporpass1 = Button(janela, text="Continuar", command=Keep)
        btn_keeporpass2 = Button(janela, text="Sair", command=Pass)
        btn_keeporpass1.grid(column=0, row=2)
        btn_keeporpass2.grid(column=1, row=2) 
        
        
        
        


def check():
    global vez,cont,yres,yget_res,verifica
    btn1.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    label.destroy()

    vez += 1
    yres = Entry(janela)
    verifica = Button(janela, text="Enter", command=verificar) 
    yres.grid(column=0, row=1)
    verifica.grid(column=2, row=1)
    


Choese()



janela.mainloop()