from tkinter import*
import numpy as np
from scipy import special as sp
#==============Main Window=================
Main = Tk()
Main.geometry("400x700+100+100")
Main.title("Calculator")
#=============Create Frames================
frame1 = Frame(Main, width= 380, height= 100,bg="white")
frame1.pack(side= TOP)
frame2 = Frame(Main, width= 350, height= 500,bg="grey")
frame2.pack()


#=============Initialize Variables=============
Input = StringVar()
operand = ""

#==============Button Click==================
def btnPress(num):
    global operand
    operand = operand + str(num)
    Input.set(operand)

def btnDelete():
    global operand
    operand = operand[0:-1]
    Input.set(operand)

def btnSqrt():
    global operand
    sqrt = str(float(operand)**(0.5))
    Input.set(sqrt)
    operand = ""

def btnClear():
    global operand
    operand = ""
    Input.set(operand)

def btnSin():
    global operand
    sin_eval = eval(str(operand))
    sine = sp.sindg(sin_eval)
    Input.set(sine)
    operand = ""

def btnCos():
    global operand
    cos_eval = eval(str(operand))
    cosine = sp.cosdg(cos_eval)
    Input.set(cosine)
    operand = ""

def btnTan():
    global operand
    tan_eval = eval(str(operand))
    tangent = sp.tandg(tan_eval)
    Input.set(tangent)
    operand = ""

def btnEquals():
    global operand
    evaluation = eval(str(operand))
    Input.set(evaluation)
    operand = str(evaluation)

#=============Create Label and Entry================
label = Label(frame1, text= "BASIC CALCULATOR", font= ("calibri", 15, "bold"), fg= "red")
label.grid(row=0,column=0)
entry = Entry(frame1, width= 50,bg="powder blue", bd= 10, textvariable= Input, relief= SUNKEN, justify= "right",insertwidth= 10)
entry.grid(columnspan= 5)

#================Calculator==================
btn7 = Button(frame2, text= "7", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(7))
btn7.grid(row=3,column=0)

btn8 = Button(frame2, text= "8", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(8))
btn8.grid(row=3,column=1)

btn9 = Button(frame2, text= "9", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(9))
btn9.grid(row=3,column=2)

btnplus = Button(frame2, text= "+", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress("+"))
btnplus.grid(row=3,column=3)

btnsine = Button(frame2, text= "sin", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnSin())
btnsine.grid(row=3,column=4)

btn4 = Button(frame2, text= "4", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(4))
btn4.grid(row=4,column=0)

btn5 = Button(frame2, text= "5", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(5))
btn5.grid(row=4,column=1)

btn6 = Button(frame2, text= "6", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(6))
btn6.grid(row=4,column=2)

btnminus = Button(frame2, text= "-", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress("-"))
btnminus.grid(row=4,column=3)

btncosine = Button(frame2, text= "cos", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnCos())
btncosine.grid(row=4,column=4)

btn1 = Button(frame2, text= "1", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(1))
btn1.grid(row=5,column=0)

btn2 = Button(frame2, text= "2", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(2))
btn2.grid(row=5,column=1)

btn3 = Button(frame2, text= "3", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(3))
btn3.grid(row=5,column=2)

btntimes = Button(frame2, text= "x", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress("*"))
btntimes.grid(row=5,column=3)

btntangent = Button(frame2, text= "tan", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnTan())
btntangent.grid(row=5,column=4)

btn0 = Button(frame2, text= "0", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress(0))
btn0.grid(row=6,column=0)

btnC = Button(frame2, text= "c", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnClear())
btnC.grid(row=6,column=1)

btnequal = Button(frame2, text= "=", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnEquals())
btnequal.grid(row=6,column=2)

btndivide = Button(frame2, text= "/", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress("/"))
btndivide.grid(row=6,column=3)

btnsqrt = Button(frame2, text= "sqrt", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnSqrt())
btnsqrt.grid(row=6,column=4)

btndecimal = Button(frame2, text= ".", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnPress("."))
btndecimal.grid(row=7,column=0)

btndel = Button(frame2, text= "Del", padx= 5,pady= 5, bd= 8, bg= "powder blue",font= ("calibri", 15, "bold"), command= lambda: btnDelete())
btndel.grid(row=7,column=4)

Main.mainloop()
