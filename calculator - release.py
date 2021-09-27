from time import time, timezone
from tkinter import*
import parser
from datetime import*

hora = datetime.now().strftime('%H')

op = ""

if hora >= "19":
    md = int(1)
elif hora <= "07":
    md = int(0)



def igual():
    global op
    math_expression = parser.expr(op).compile()
    result = eval(math_expression)
    vs_1["text"]=result

def opes(operador):
    global op
    op = op + operador
    vs_2["text"]=op
def nums(num):
    global op
    op = op + num
    vs_2["text"]=op


def fun_del():
    global op
    if op != "0":        
        op = op[:-1]
        vs_2["text"]=op
def fun_del_all():
    global op
    op = ""
    vs_2["text"]="0"


def mod():
    global md
    if md == int(1):
        w.config(bg="#25292e")
        vs_1["bg"]="#25292e"
        #b_1["bg"]="#25292e"
        md = md - int(1)
    elif md == int(0):
        w.config(bg="#3e4042")
        md = md + int(1)

w = Tk()

vs_1 = Label(w, text="", font=("Arial Rounded", "13"), bg="#ffffff")
vs_2 = Label(w, text="0", font=("Arial", "11"), bg="#ffffff")
vs_1.grid(column="0", row="0", columnspan="6")
vs_2.grid(column="0", row="1", columnspan="6")


b_0 = Button(w, text="0", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("0")).grid(column="0", row="5")
b_1 = Button(w, text="1", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("1")).grid(column="0", row="2")
b_2 = Button(w, text="2", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("2")).grid(column="1", row="2")
b_3 = Button(w, text="3", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("3")).grid(column="2", row="2")
b_4 = Button(w, text="4", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("4")).grid(column="0", row="3")
b_5 = Button(w, text="5", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("5")).grid(column="1", row="3")
b_6 = Button(w, text="6", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("6")).grid(column="2", row="3")
b_7 = Button(w, text="7", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("7")).grid(column="0", row="4")
b_8 = Button(w, text="8", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("8")).grid(column="1", row="4")
b_9 = Button(w, text="9", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: nums("9")).grid(column="2", row="4")

b_del = Button(w, text="⟵", bg="#ffffff", width= "6", height="2", command=fun_del). grid(column="1", row="5")
b_del_all = Button(w, text="0⟵", bg="#ffffff", width= "6", height="2", command=fun_del_all).grid(column="2", row="5")

t = Label(w, text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|").grid(column="3", row="2", rowspan="6")

b_sum = Button(w, text="+", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: opes("+")).grid(column="4", row="2")
b_res = Button(w, text="-", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: opes("-")).grid(column="5", row="2")
b_mult = Button(w, text="*", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: opes("*")).grid(column="4", row="3")
b_div = Button(w, text="/", font=("Courier"), bg="#ffffff", width="6", height="2", command=lambda: opes("/")).grid(column="5", row="3")
b_resul = Button(w, text="=", font=("Courier"), bg="#ffffff", width="13", height="2", command=igual).grid(column="4", row="4", columnspan="2")
b_mode = Button(w, text="☾", font=("Courier", "19"), bg="#ffffff", width="4", command=mod).grid(column="4", row="5")


mod()
w.mainloop()