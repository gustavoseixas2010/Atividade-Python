from tkinter import *

janelaPedidos = Tk()
janelaPedidos.geometry("500x200")
janelaPedidos.title("Pedidos")

barraMenu = Menu(janelaPedidos)
janelaPedidos.config(menu = barraMenu)
subMenu = Menu(barraMenu)
barraMenu.add_cascade(label="Arquivo",menu=subMenu)
subMenu.add_command(label="Novo")
subMenu.add_command(label="Abrir")
subMenu.add_command(label="Salvar")
subMenu2 = Menu(barraMenu)
barraMenu.add_cascade(label="Editar",menu=subMenu2)
subMenu3 = Menu(barraMenu)

frameCampos = Frame(janelaPedidos)

labelTitulo = Label(text = "CONTROLE DE PEDIDOS")

labelNumP = Label(frameCampos,text="Nº do Pedido:")
entryNumP = Entry(frameCampos,width=7)
labelNumP.grid(column=0,row=0,sticky=E)
entryNumP.grid(column=1,row=0,sticky=W)

labelCód = Label(frameCampos,text = "Cód.Produto:")
entryCód = Entry(frameCampos,width=7)
labelCód.grid(column=3, row=0,sticky=E)
entryCód.grid(column=4,row=0,sticky=W)

labelVend = Label(frameCampos,text="Vendedor:")
entryVend = Entry(frameCampos,width=15)
labelVend.grid(column=0,row=1,stick=E)
entryVend.grid(column=1,row=1,sticky=W)

labelClie = Label(frameCampos,text="Cliente:")
entryClie = Entry(frameCampos,width=15)
labelClie.grid(column=0,row=2,stick=E)
entryClie.grid(column=1,row=2,sticky=W)

labelData = Label(frameCampos,text= "Data do Pedido:")
entryData = Entry(frameCampos,width=9)
labelData.grid(column=0,row=3,sticky=W)
entryData.grid(column=1,row=3,sticky=W)

labelPrd = Label(frameCampos,text = "Produto:")
entryPrd = Entry(frameCampos,width=15)
labelPrd.grid(column=0,row=4,sticky=E)
entryPrd.grid(column=1,row=4,sticky=W)

labelQtd = Label(frameCampos,text="Quantidade:")
entryQtd = Entry(frameCampos,width=5)
labelQtd.grid(column=3, row=3,sticky=E)
entryQtd.grid(column=4,row=3,sticky=W)

labelVlr = Label(frameCampos,text = "Total:")
entryVlr = Entry(frameCampos,width=8)
labelVlr.grid(column=0,row=5,sticky=E)
entryVlr.grid(column=1,row=5,sticky=W)

botNovo = Button(text = "Novo")
botRegistrar = Button(text = "Registrar")
botExcluir = Button(text = "Excluir")

labelTitulo.pack()

frameCampos.pack()

botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botAlterar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaPedidos.mainloop

