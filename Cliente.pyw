from tkinter import *

janelaClientes = Tk()
janelaClientes.geometry("500x200")
janelaClientes.title("Clientes")

barraMenu = Menu(janelaClientes)
janelaClientes.config(menu = barraMenu)
subMenu = Menu(barraMenu)
barraMenu.add_cascade(label="Arquivo",menu=subMenu)
subMenu.add_command(label="Novo")
subMenu.add_command(label="Abrir")
subMenu.add_command(label="Salvar")
subMenu2 = Menu(barraMenu)
barraMenu.add_cascade(label="Editar",menu=subMenu2)
subMenu3 = Menu(barraMenu)
barraMenu.add_cascade(label="Pesquisar",menu=subMenu3)
subMenu3.add_command(label="Nome do Cliente")
subMenu4 = Menu(barraMenu)
barraMenu.add_cascade(label="Ajuda",menu=subMenu4)

frameCampos = Frame(janelaClientes)

labelTitulo = Label(text = "CADASTRO DE CLIENTES")

labelCódigo = Label(frameCampos,text = "Cód. do Cliente:")
entryCódigo = Entry(frameCampos,width=5)

labelNome = Label(frameCampos,text = "Nome do Cliente:")
entryNome = Entry(frameCampos,width=38)

labelEndereço = Label(frameCampos,text = "Endereço:")
entryEndereço = Entry(frameCampos,width=30)

labelTelefone = Label(frameCampos,text = "Celular:")
entryTelefone = Entry(frameCampos,width=15)

labelNumero = Label(frameCampos,text = "Nº:")
entryNumero = Entry(frameCampos,width=6)

labelCPF = Label(frameCampos,text = "CPF:")
entryCPF = Entry(frameCampos,width=14)

labelCódigo.grid(column=0, row=0)
entryCódigo.grid(columnspan=5,column=1,row=0,sticky=W)

labelNome.grid(column=0, row=1,sticky=E)
entryNome.grid(column=1,row=1,sticky=W)

labelEndereço.grid(column = 0, row=2,sticky=E)
entryEndereço.grid(column = 1, row=2,sticky=W)

labelNumero.grid(column = 1, row=2,sticky=E)
entryNumero.grid(column = 2, row=2,sticky=W)

labelTelefone.grid(column = 0, row=4,sticky=E)
entryTelefone.grid(column = 1, row=4,sticky=W)

labelCPF.grid(column=0, row =5,sticky=E)
entryCPF.grid(column=1, row =5,sticky=W)

botNovo = Button(text = "Novo")
botRegistrar = Button(text = "Cadastrar")
botAlterar = Button(text = "Alterar")
botExcluir = Button(text = "Excluir")


labelTitulo.pack()
frameCampos.pack()
botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botAlterar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaClientes.mainloop()
