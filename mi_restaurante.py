
import customtkinter as ck
from customtkinter import IntVar, StringVar, END, filedialog
import string
import random
import datetime
from CTkMessagebox import CTkMessagebox


operador = ''

#dolares
precios_comida = [160, 250, 230, 300, 200, 99, 105, 165]
precios_bebida = [15, 22, 20, 25, 70, 110, 40, 90]
precios_postres = [30, 30, 25, 17, 25, 40, 45, 15]
revisar_comida = []
revisar_bebidas = []
revisar_postres = []

def click_boton(numero):

    global operador
    operador = operador + numero
    visor_calculador.delete(0, END)
    visor_calculador.insert(END, operador)

def borrar():
    global operador

    operador = ''
    visor_calculador.delete(0, END)

def obtener_total():
    global operador

    resultado = str(eval(operador))

    visor_calculador.delete(0, END)
    visor_calculador.insert(0, resultado)
    operador = ''

def revisar_check():

    indice = 0
    for c in cuadros_comida:
        if variables_comidas[indice].get() == 1:
            cuadros_comida[indice].configure(state='normal')
            if cuadros_comida[indice].get() == '0':
                cuadros_comida[indice].delete(0, END)
            cuadros_comida[indice].focus()
        else:
            cuadros_comida[indice].configure(state='disabled')
            texto_comida[indice].set('0')
        indice += 1

    indice = 0
    for c in cuadros_bebidas:
        if variables_bebidas[indice].get() == 1:
            cuadros_bebidas[indice].configure(state='normal')
            if cuadros_bebidas[indice].get() == '0':
                cuadros_bebidas[indice].delete(0, END)
            cuadros_bebidas[indice].focus()
        else:
            cuadros_bebidas[indice].configure(state='disabled')
            texto_bebidas[indice].set('0')
        indice += 1

    indice = 0
    for c in cuadros_postres:
        if variables_postres[indice].get() == 1:
            cuadros_postres[indice].configure(state='normal')
            if cuadros_postres[indice].get() == '0':
                cuadros_postres[indice].delete(0, END)
            cuadros_postres[indice].focus()
        else:
            cuadros_postres[indice].configure(state='disabled')
            texto_postres[indice].set('0')
        indice += 1

def total():
    
    icon = r"C:\Users\Pablo\OneDrive\Documentos\Python\Meta_dia_10\5501325.png"
    resultado = listo()
    resultado1 = comprobar()

    if resultado == True or resultado1 == True:

        CTkMessagebox(title="Error", message="Favor de revisar su pedido,Seleccione una opción o ingresa una cantidad",
                    icon="warning")
        return
    
    else:

        #comida             
        sub_total_comida = 0
        indice = 0

        for cantidad in texto_comida:

            sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[indice])
            indice += 1
        
        #Bebidas
        sub_total_bebidas = 0
        indice = 0

        for cantidad in texto_bebidas:

            sub_total_bebidas = sub_total_bebidas + (float(cantidad.get()) * precios_bebida[indice])
            indice += 1

        #Bebidas
        sub_total_postres = 0
        indice = 0

        for cantidad in texto_postres:

            sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[indice])
            indice += 1

        #Subtotal
        Subtotal = sub_total_comida + sub_total_bebidas + sub_total_postres
        impuestos = Subtotal * 0.07
        total = Subtotal + impuestos

        var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
        var_costo_bebidas.set(f'$ {round(sub_total_bebidas, 2)}')
        var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
        var_subtotal.set(f'$ {round(Subtotal, 2)}')
        var_impuesto.set(f'$ {round(impuestos, 2)}')
        var_total.set(f'$ {round(total, 2)}')

def recibo():
         
        resultado = listo()
        resultado1 = comprobar()

        if resultado == True or resultado1 == True:

            CTkMessagebox(title="Error", message="Primero haga su pedido!", icon="warning")
            return
    
        else:

            texto_recibo.delete(1.0, END)
            numero_recibo = f'N# - {random.randint(1000, 9999)}'
            fecha = datetime.datetime.now()

            fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year}  -  {fecha.hour}:{fecha.minute}'
            texto_recibo.insert(END, f' Datos: {numero_recibo}\t\t          {fecha_recibo}\n')
            texto_recibo.insert(END, f'*' * 54 + '\n')
            texto_recibo.insert(END, ' Items\t\tCant.\tCosto Items\n')
            texto_recibo.insert(END, f'-' * 64 + '\n')

            indice = 0
            for comida in texto_comida:

                if comida.get() != '0':
                    texto_recibo.insert(END, f' {lista_comidas[indice]}\t\t    {comida.get()}\t'
                                        f'${round(int(comida.get()) * precios_comida[indice],2)}\n')
                    
                indice += 1


            indice = 0
            for bebida in texto_bebidas:

                if bebida.get() != '0':
                    texto_recibo.insert(END, f' {lista_bebidas[indice]}\t\t    {bebida.get()}\t'
                                        f'${round(int(bebida.get()) * precios_bebida[indice],2)}\n')
                    
                indice += 1


            indice = 0
            for postres in texto_postres:

                if postres.get() != '0':
                    texto_recibo.insert(END, f' {lista_postres[indice]}\t\t    {postres.get()}\t'
                                        f'${round(int(postres.get()) * precios_postres[indice],2)}\n')
                    
                indice += 1


            texto_recibo.insert(END, f'*' * 54 + '\n')
            texto_recibo.insert(END, f' Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
            texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebidas.get()}\n')
            texto_recibo.insert(END, f' Costo de los Postres: \t\t\t{var_costo_postres.get()}\n')

            texto_recibo.insert(END, f'*' * 54 + '\n')
            texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
            texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuesto.get()}\n')
            texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')

            texto_recibo.insert(END, f'*' * 54 + '\n')
            texto_recibo.insert(END, '\n !Gracias por su preferencia¡\n')

def guardar():

    resultado = listo()
    resultado1 = comprobar()

    if resultado == True or resultado1 == True:

        CTkMessagebox(title="Error", message="No hay nada por guardar!", icon="warning")
        return
    
    else:

        info_recibo = texto_recibo.get(1.0, END)
        archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        archivo.write(info_recibo)
        archivo.close()
        CTkMessagebox(title='Recibo',message="Su recibo ha sido guardado",icon="check", option_1="Gracias")

def resetear():


    #Borrar contenido de caja de texto
    texto_recibo.delete(0.1, END)

    #Resetear los contadores de comida
    for texto in texto_comida:
        texto.set('0')

    for texto in texto_bebidas:
        texto.set('0')

    for texto in texto_postres:
        texto.set('0')

    #Desactivar las cajas de cantidad de comida
    for cuadro in cuadros_comida:
        cuadro.configure(state='disabled')

    for cuadro in cuadros_bebidas:
        cuadro.configure(state='disabled')

    for cuadro in cuadros_postres:
        cuadro.configure(state='disabled')

    #Desactivar todas las apciones generadas un pedido anterior
    for var in variables_comidas:
        var.set(0)

    for var in variables_bebidas:
        var.set(0)

    for var in variables_postres:
        var.set(0)

    #Borrar cantidad de dinero de pedido  
    var_costo_comida.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

def lista_precios():

    cuadro_texto = 'de'


    cuadro = CTkMessagebox(title='Precios',message=cuadro_texto,option_1="OK",width=300, height=700,font=('dosis',35)
                           ,button_color="green", button_width=100, button_height=60)
    
    cuadro_texto = ck.CTkFrame(cuadro, width=980, height=348, fg_color="grey5")
    cuadro_texto.place(relx=0.01, rely=0.11)
    cuadro.geometry('1000x500+0+100')

    contador_especial = 0

    for com in lista_comidas:

        com = ck.CTkLabel(cuadro_texto, text=com + '\t -- ', font=('dosis',25,'bold'),text_color='SkyBlue3')
        com.place(relx=.02, rely=0.06 + contador_especial)

        contador_especial += 0.11

    contador_especial = 0
    for pre in precios_comida:

        pre = ck.CTkLabel(cuadro_texto, text=' $' + str(pre), font=('dosis',25,'bold'),text_color='yellow')
        pre.place(relx=.18, rely=0.06 + contador_especial)

        contador_especial += 0.11


    #Lista de bebidas y precios
    contador_especial = 0
    lista = ['--','--','--','--','--','--','--','--']
    for com in lista_bebidas:

        com = ck.CTkLabel(cuadro_texto, text=com,font=('dosis',25,'bold'),text_color='SkyBlue3')
        com.place(relx=.35, rely=0.06 + contador_especial)

        contador_especial += 0.11

    contador_especial = 0

    for g in lista:

        g = ck.CTkLabel(cuadro_texto, text=g,font=('dosis',25,'bold'),text_color='SkyBlue3')
        g.place(relx=.51, rely=0.06 + contador_especial)

        contador_especial += 0.11

    contador_especial = 0
    for pre in precios_bebida:

        pre = ck.CTkLabel(cuadro_texto, text=' $' + str(pre), font=('dosis',25,'bold'),text_color='yellow')
        pre.place(relx=.55, rely=0.06 + contador_especial)

        contador_especial += 0.11


    #lista de postres y precios
    contador_especial = 0
    for com in lista_postres:

        com = ck.CTkLabel(cuadro_texto, text=com,font=('dosis',25,'bold'),text_color='SkyBlue3')
        com.place(relx=.68, rely=0.06 + contador_especial)

        contador_especial += 0.11

    contador_especial = 0

    for g in lista:

        g = ck.CTkLabel(cuadro_texto, text=g,font=('dosis',25,'bold'),text_color='SkyBlue3')
        g.place(relx=.83, rely=0.06 + contador_especial)

        contador_especial += 0.11

    contador_especial = 0
    for pre in precios_postres:

        pre = ck.CTkLabel(cuadro_texto, text=' $' + str(pre), font=('dosis',25,'bold'),text_color='yellow')
        pre.place(relx=.87, rely=0.06 + contador_especial)

        contador_especial += 0.11   

def listo():

    for comi in variables_comidas:
        if comi.get() == 0:
            revisar_comida.append(comi)
            
        else:
            print(comi.get())
    print(len(revisar_comida))

    for bebida in variables_bebidas:
        if bebida.get() == 0:
            revisar_bebidas.append(bebida)

        else:
            print(bebida.get())

    print(len(revisar_bebidas))

    for poste in variables_postres:
        if poste.get() == 0:
            revisar_postres.append(poste)

        else:
            print(poste.get())
            
    print(len(revisar_postres))

    if len(revisar_comida) >= 8 and len(revisar_bebidas) >= 8 and len(revisar_postres) >= 8:
        print("jaja")
        resetear()
        revisar_comida.clear()
        revisar_bebidas.clear()
        revisar_postres.clear()
        return True

    else:
        revisar_comida.clear()
        revisar_bebidas.clear()
        revisar_postres.clear()
        return False
    
def comprobar():
    
    for c in cuadros_comida:
        for b in cuadros_bebidas:
            for p in cuadros_postres:

                if c.get() == '' or b.get() == '' or p.get() == '':

                        return True
                     

ck.set_appearance_mode("system")  # Modes: system (default), light, dark
ck.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = ck.CTk()  # create CTk window like you do with the Tk window
app.geometry("1020x680+0+0")
app.title("Retaurante")
app.resizable(width=False, height=False)


#Panel superior
panel_superior = ck.CTkFrame(app, bg_color="black",width=1000, height=80)
panel_superior.pack(padx=20, pady=15)

etiqueta_factura = ck.CTkLabel(panel_superior, text="Sistema de Facturación", font=("dosis", 58), width=27, text_color="lime")
etiqueta_factura.place(relx=.2, rely=.2)

#Panel Izquierdo
panel_izquierdo = ck.CTkFrame(app, bg_color="black",width=600, height=380)
panel_izquierdo.place(relx=0.02, rely=0.15)

etiqueta_comida = ck.CTkLabel(panel_izquierdo, text="Comida", text_color="orange", font=("dosis", 30))
etiqueta_comida.place(relx=0.05, rely=0.01)

etiqueta_bebida = ck.CTkLabel(panel_izquierdo, text="Bebidas", text_color="orange", font=("dosis", 30))
etiqueta_bebida.place(relx=0.33, rely=0.01)

etiqueta_postres = ck.CTkLabel(panel_izquierdo, text="Postres", text_color="orange", font=("dosis", 30))
etiqueta_postres.place(relx=0.64, rely=0.01)

#Panel Derecha
panel_derecha = ck.CTkFrame(app, bg_color="black",width=368, height=564)
panel_derecha.place(relx=0.62, rely=0.15)


#Panel inferior (costos)
panel_costos =  ck.CTkFrame(app, fg_color="grey5",width=600, height=180)
panel_costos.place(relx=0.02, rely=0.72)

#Panel botones
panel_botones = ck.CTkFrame(panel_derecha, fg_color="grey5",width=380, height=60)
panel_botones.place(relx=0.03, rely=0.9)

#Panel Recibo
panel_recibo = ck.CTkFrame(panel_derecha)
panel_recibo.place(relx=0.03, rely=0.50)

#Panel Calculadora
panel_calculadora = ck.CTkFrame(panel_derecha,fg_color="black",width=348, height=265)
panel_calculadora.place(relx=0.03, rely=0.01)


#lista de Productos
lista_comidas = ['Pollo', 'Cordero', 'Salmon', 'Merluza', 'Kebab', 'Pizza', 'Pizza1', 'Pizza2']
lista_bebidas = ['Agua', 'Soda', 'Jugo', 'Coca', 'Vino Tinto', 'Vino Bco.', 'Cerveza', 'Tequila']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Mousse', 'Pastel', 'P. 3 leches','Pan']

#Generar Items comida
variables_comidas = []
cuadros_comida = []
texto_comida = []
contador = 0
contador_0 = 0

for comida in lista_comidas:

    #crear checkbox
    variables_comidas.append('')
    variables_comidas[contador] = ck.IntVar()
    comida = ck.CTkCheckBox(panel_izquierdo, text=comida.title(), font=("dosis", 20),command=revisar_check,
                            variable=variables_comidas[contador],onvalue=1,offvalue=0)
    
    comida.place(relx=.05, rely=.13 + contador_0)
    contador_0 += 0.09
    
    #Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = ck.StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = ck.CTkEntry(panel_izquierdo, text_color="lime",font=("dosis",18)
                                    ,width=40, state="disabled", textvariable=texto_comida[contador])
    cuadros_comida[contador].place(relx=.23, rely=.03 + contador_0)

    contador += 1

#Generar Items bebidas
variables_bebidas = []
cuadros_bebidas = []
texto_bebidas = []
contador_0 = 0
contador = 0

for bebidas in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = ck.IntVar()
    bebidas = ck.CTkCheckBox(panel_izquierdo, text=bebidas.title(), font=("dosis", 20), onvalue=1, 
                            offvalue=0, variable=variables_bebidas[contador],command=revisar_check)
    
    bebidas.place(relx=.33, rely=.13 + contador_0)
    contador_0 += 0.09

    #Crear los cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = ck.StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = ck.CTkEntry(panel_izquierdo,text_color="lime", font=("dosis",18),width=40, state="disabled", textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].place(relx=.54, rely=.03 + contador_0)

    contador += 1
#Generar Items Postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador_0 = 0
contador = 0

for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = ck.IntVar()
    postres = ck.CTkCheckBox(panel_izquierdo, text=postres.title(), font=("dosis", 20), onvalue=1, 
                            offvalue=0, variable=variables_postres[contador],command=revisar_check)
    
    postres.place(relx=.64, rely=.13 + contador_0)
    contador_0 += 0.09

    #Crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = ck.StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = ck.CTkEntry(panel_izquierdo,text_color="lime",font=("dosis",18),width=40, state="disabled", textvariable=texto_postres[contador])
    cuadros_postres[contador].place(relx=.89, rely=.03 + contador_0)

    contador += 1

#Boton Precios de Comidas, Bebidas y Postres
    
boton_precios = ck.CTkButton(panel_izquierdo,fg_color=("DarkSlateGrey"),text="Lista de Precios",font=("dosis",18,'bold'),
                             border_color="black",width=200, height=40,command=lista_precios)
boton_precios.place(relx=0.35, rely=0.88)


#variables
var_costo_comida = ck.StringVar()
var_costo_bebidas = ck.StringVar()
var_costo_postres = ck.StringVar()
var_subtotal = ck.StringVar()
var_impuesto = ck.StringVar()
var_total = ck.StringVar()


#Etiquetas Costo comida y Campos de entrada    
etiqueta_costo_comida = ck.CTkLabel(panel_costos, text="Costo Comida", font=("dosis",22,'bold'),text_color="tomato2")
etiqueta_costo_comida.place(relx=0.04, rely=0.07)

texto_costo_comida = ck.CTkEntry(panel_costos, text_color="lime", font=("dosis",13),width=100, state="readonly", textvariable=var_costo_comida)
texto_costo_comida.place(relx=0.30, rely=0.07)

#Etiquetas Costo bebidas y Campos de entrada    
etiqueta_costo_bebida = ck.CTkLabel(panel_costos, text="Costo Bebida", font=("dosis",22,'bold'), text_color="tomato2")
etiqueta_costo_bebida.place(relx=0.04, rely=0.35)

texto_costo_bebida = ck.CTkEntry(panel_costos, text_color="lime", font=("dosis",13),width=100, state="readonly", textvariable=var_costo_bebidas)
texto_costo_bebida.place(relx=0.30, rely=0.35)

#Etiquetas Costo postres y Campos de entrada    
etiqueta_costo_postres = ck.CTkLabel(panel_costos, text="Costo Postres", font=("dosis",22,'bold'), text_color="tomato2")
etiqueta_costo_postres.place(relx=0.04, rely=0.63)

texto_costo_bebida = ck.CTkEntry(panel_costos, text_color="lime", font=("dosis",13),width=100, state="readonly", textvariable=var_costo_postres)
texto_costo_bebida.place(relx=0.30, rely=0.63)


#Etiquetas Subtotal y Campos de entrada    
etiqueta_subtotal = ck.CTkLabel(panel_costos, text="Subtotal", font=("dosis",22,'bold'), text_color="tomato2")
etiqueta_subtotal.place(relx=0.55, rely=0.07)

texto_subtotal = ck.CTkEntry(panel_costos, text_color="lime", font=("dosis",13),width=100, state="readonly", textvariable=var_subtotal)
texto_subtotal.place(relx=0.75, rely=0.07)

#Etiquetas impuestos y Campos de entrada    
etiqueta_impuestos = ck.CTkLabel(panel_costos, text="Impuestos", font=("dosis",22,'bold'), text_color="tomato2")
etiqueta_impuestos.place(relx=0.55, rely=0.35)

texto_impuestos = ck.CTkEntry(panel_costos, text_color="lime", font=("dosis",13),width=100, state="readonly", textvariable=var_impuesto)
texto_impuestos.place(relx=0.75, rely=0.35)

#Etiquetas total y Campos de entrada    
etiqueta_total = ck.CTkLabel(panel_costos, text="Total", font=("dosis",22,'bold'), text_color="tomato2")
etiqueta_total.place(relx=0.55, rely=0.63)

texto_total = ck.CTkEntry(panel_costos, text_color="lime", font=("dosis",13),width=100, state="readonly", textvariable=var_total)
texto_total.place(relx=0.75, rely=0.63)

#Botones
Botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
contador_columnas = 0

for boton in Botones:

    boton = ck.CTkButton(panel_botones, text=boton.title(), font=("dosis",14,'bold'),fg_color='OrangeRed3',
                        text_color="black",border_color="black",width=87, height=48)
    boton.grid(row=0, column=contador_columnas)

    botones_creados.append(boton)

    contador_columnas += 1

botones_creados[0].configure(command=total)
botones_creados[1].configure(command=recibo)
botones_creados[2].configure(command=guardar)
botones_creados[3].configure(command=resetear)
#area de recibo
    
texto_recibo = ck.CTkTextbox(panel_recibo, font=("dosis", 16,'bold'), width=348, height=210,fg_color="grey5")
texto_recibo.grid(row=0, column=0)

#calculadora
visor_calculador = ck.CTkEntry(panel_calculadora, font=("dosis",18,'bold'), width=345)
visor_calculador.place(relx=0.01, rely=0.01)

botones_calculadora = ['7','8','9','+','4','5','6','-','1','2','3','x','R','B','0','/']
botones_guardados = []
x = 0
y = 0
for boton in botones_calculadora:

    boton = ck.CTkButton(panel_calculadora, text=boton.title(), font=("dosis", 16, 'bold'), text_color="white", 
                         fg_color="green",width=70, height=50)
    boton.place(relx=.03 + x, rely=0.13 + y)

    botones_guardados.append(boton)

    x += 0.25

    if x > 0.8:

        y += 0.22

    if x == 1:
        x = 0

botones_guardados[0].configure(command=lambda : click_boton('7'))
botones_guardados[1].configure(command=lambda : click_boton('8'))
botones_guardados[2].configure(command=lambda : click_boton('9'))
botones_guardados[3].configure(command=lambda : click_boton('+'))
botones_guardados[4].configure(command=lambda : click_boton('4'))
botones_guardados[5].configure(command=lambda : click_boton('5'))
botones_guardados[6].configure(command=lambda : click_boton('6'))
botones_guardados[7].configure(command=lambda : click_boton('-'))
botones_guardados[8].configure(command=lambda : click_boton('1'))
botones_guardados[9].configure(command=lambda : click_boton('2'))
botones_guardados[10].configure(command=lambda : click_boton('3'))
botones_guardados[11].configure(command=lambda : click_boton('*'))
botones_guardados[12].configure(command=obtener_total)
botones_guardados[13].configure(command=borrar)
botones_guardados[14].configure(command=lambda : click_boton('0'))
botones_guardados[15].configure(command=lambda : click_boton('/'))




app.mainloop()