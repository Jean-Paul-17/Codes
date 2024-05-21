import tkinter as tk
ventana=tk.Tk()
imagen=tk.PhotoImage(file="img_calculadora.png")
ventana.resizable(width=False, height=False)
ventana.geometry("476x700")

label_img=tk.Label(ventana, image=imagen)
label_img.pack()

#Caja de números
entry=tk.Entry(ventana)
entry.place(x=50, y=50, width=350, height=25)

#Botones numéricos
num1=tk.Button(ventana, text="1")
num1.place(x=115, y=640, width=60, height=40)

num2=tk.Button(ventana, text="2")
num2.place(x=205, y=640, width=60, height=40)

num3=tk.Button(ventana, text="3")
num3.place(x=290, y=640, width=60, height=40)

num4=tk.Button(ventana, text="4")
num4.place(x=115, y=580, width=60, height=40)

num5=tk.Button(ventana, text="5")
num5.place(x=205, y=580, width=60, height=40)

num6=tk.Button(ventana, text="6")
num6.place(x=290, y=580, width=60, height=40)

num7=tk.Button(ventana, text="7")
num7.place(x=115, y=520, width=60, height=40)

num8=tk.Button(ventana, text="8")
num8.place(x=205, y=520, width=60, height=40)

num9=tk.Button(ventana, text="9")
num9.place(x=290, y=520, width=60, height=40)

#Botones aritméticos
button_mas=tk.Button(ventana, text="+")
button_mas.place(x=380, y=640, width=60, height=40)

button_menos=tk.Button(ventana, text="-")
button_menos.place(x=380, y=580, width=60, height=40)

button_por=tk.Button(ventana, text="X")
button_por.place(x=380, y=520, width=60, height=40)

button_division=tk.Button(ventana, text="÷")
button_division.place(x=380, y=460, width=60, height=40)
ventana.mainloop()