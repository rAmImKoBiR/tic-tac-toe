import os 
try :
    import tkinter 
except ModuleNotFoundError:
    try :
        import os
        os.system('pip install tkinter')
    except :
         try :
             import os
             os.system('pip install Tkinter')
         except :
                pass
try :
    import customtkinter as ct
except ModuleNotFoundError:
    os.system('pip install customtkinter')
    import customtkinter as ct
import time
import random
def tt():
    global canvas
    global O,X
    O,X=[],[]
    canvas.destroy()
    canvas=ct.CTkCanvas(root, width=600, height=600,)
    canvas.configure(bg='pink')
    canvas.pack()
    canvas.create_line(200,0,200,600, fill="black", width=2)
    canvas.create_line(400,0,400,600, fill="black", width=2)
    canvas.create_line(0,200,600,200, fill="black", width=2)
    canvas.create_line(0,400,600,400, fill="black", width=2)
    b1=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=199,command=lambda:config('b1',b1))
    b2=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b2',b2))
    b3=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b3',b3))
    b4=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=198,width=199,command=lambda:config('b4',b4))
    b5=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=198,width=198,command=lambda:config('b5',b5))
    b6=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=198,width=198,command=lambda:config('b6',b6))
    b7=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b7',b7))
    b8=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b8',b8))
    b9=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b9',b9))
    b1.place(x=0,y=0)
    b2.place(x=201,y=0)
    b3.place(x=401,y=0)
    b4.place(x=0,y=201)
    b5.place(x=201,y=201)
    b6.place(x=401,y=201)
    b7.place(x=0,y=401)
    b8.place(x=201,y=401)
    b9.place(x=401,y=401)



d,f=0,0
def rootitelconfig(text,x,y):
    global root
    root.title(f'{text} X {x}--{y} O')
h=random.choice(['X','O'])
O=[]
X=[]
def xwin(x):
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global d,f
    d=d+1
    global list 
    list=[]
    global canvas
    if 'b1' in x:
        canvas.create_line(0,100,200,100, fill="green", width=10)
    if 'b2' in x:
        canvas.create_line(200,100,400,100 ,fill="green", width=10)
    if 'b3' in x:
        canvas.create_line(400,100,600,100 ,fill="green", width=10)
    if 'b4' in x:
        canvas.create_line(0,300,200,300, fill="green", width=10)
    if 'b5' in x:
        canvas.create_line(200,300,400,300 ,fill="green", width=10)
    if 'b6' in x:
        canvas.create_line(400,300,600,300 ,fill="green", width=10)
    if 'b7' in x:
        canvas.create_line(0,500,200,500, fill="green", width=10)
    if 'b8' in x:
        canvas.create_line(200,500,400,500 ,fill="green", width=10)
    if 'b9' in x:
        canvas.create_line(400,500,600,500 ,fill="green", width=10)
    global root
    rootitelconfig('X_win',d,f)
    root.after(500,lambda:tt())
def ywin(x):    
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global d,f
    f=f+1
    rootitelconfig('O_win',d,f)
    global list
    list =[]
    global canvas
    if 'b1' in x:
        canvas.create_line(0,100,200,100, fill="green", width=10)
    if 'b2' in x:
        canvas.create_line(200,100,400,100 ,fill="green", width=10)
    if 'b3' in x:
        canvas.create_line(400,100,600,100 ,fill="green", width=10)
    if 'b4' in x:
        canvas.create_line(0,300,200,300, fill="green", width=10)
    if 'b5' in x:
        canvas.create_line(200,300,400,300 ,fill="green", width=10)
    if 'b6' in x:
        canvas.create_line(400,300,600,300 ,fill="green", width=10)
    if 'b7' in x:
        canvas.create_line(0,500,200,500, fill="green", width=10)
    if 'b8' in x:
        canvas.create_line(200,500,400,500 ,fill="green", width=10)
    if 'b9' in x:
        canvas.create_line(400,500,600,500 ,fill="green", width=10)
    global root 
    root.after(500,lambda:tt())
def drow():
    global d,f
    rootitelconfig('Drow',d,f)
    tt()
def config(w,y):
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global list
    try :
        list.remove(y)
    except:
        pass
    x=y.winfo_x()
    z=y.winfo_y()
    y.destroy()
    global h
    global O,X
    if h=='O' :
        canvas.create_line(x+30,z+30,x+200-30,z+200-30, fill="red", width=8)
        canvas.create_line(x+200-30,z+30,x+30,z+200-30, fill="red", width=8)
        X.append(w)
        list.append(w)
        h='X'
    elif h=='X' :
        canvas.create_oval(x+200-30,z+30,x+30,z+200-30, fill="red", width=8)
        O.append(w)
        list.append(w)
        h='O'
    if 'b1' in X and 'b2' in X and 'b3' in X :
        xwin(['b1','b2','b3'])
    elif 'b4' in X and 'b5' in X and 'b6' in X :
        xwin(['b4','b5','b6'])
    elif 'b7' in X and 'b8' in X and 'b9' in X :
        xwin(['b7','b8','b9'])
    elif 'b1' in X and 'b4' in X and 'b7' in X :
        xwin(['b1','b4','b7'])
    elif 'b2' in X and 'b5' in X and 'b8' in X :
        xwin(['b2','b5','b8'])
    elif 'b3' in X and 'b6' in X and 'b9' in X :
        xwin(['b3','b6','b9'])
    elif 'b1' in X and 'b5' in X and 'b9' in X :
        xwin(['b1','b5','b9'])
    elif 'b3' in X and 'b5' in X and 'b7' in X :
        xwin(['b3','b5','b7'])
    elif 'b1' in O and 'b2' in O and 'b3' in O :
        ywin(['b1','b2','b3'])
    elif 'b4' in O and 'b5' in O and 'b6' in O :
        ywin(['b4','b5','b6'])
    elif 'b7' in O and 'b8' in O and 'b9' in O :
        ywin(['b7','b8','b9'])
    elif 'b1' in O and 'b4' in O and 'b7' in O :
        ywin(['b1','b4','b7'])
    elif 'b2' in O and 'b5' in O and 'b8' in O:
        ywin(['b2','b5','b8'])
    elif 'b3' in O and 'b6' in O and 'b9' in O :
        ywin(['b3','b6','b9'])
    elif 'b1' in O and 'b5' in O and 'b9' in O :
        ywin(['b1','b5','b9'])
    elif 'b3' in O and 'b5' in O and 'b7' in O :
        ywin(['b3','b5','b7'])
    else :
        if len(list)==9:
            list=[]
            global root
            root.after(500,lambda:drow())
root=ct.CTk()
root.geometry('600x600')
root.minsize(600,600)
root.maxsize(600,600)
rootitelconfig('',0,0)
canvas=ct.CTkCanvas(root, width=600, height=600,)
canvas.configure(bg='pink')
canvas.pack()
canvas.create_line(200,0,200,600, fill="black", width=2)
canvas.create_line(400,0,400,600, fill="black", width=2)
canvas.create_line(0,200,600,200, fill="black", width=2)
canvas.create_line(0,400,600,400, fill="black", width=2)
b1=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=199,command=lambda:config('b1',b1))
b2=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b2',b2))
b3=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b3',b3))
b4=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=198,width=199,command=lambda:config('b4',b4))
b5=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=198,width=198,command=lambda:config('b5',b5))
b6=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=198,width=198,command=lambda:config('b6',b6))
b7=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b7',b7))
b8=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b8',b8))
b9=ct.CTkButton(canvas,bg_color='pink',fg_color='pink',hover_color='pink',text='',height=199,width=198,command=lambda:config('b9',b9))
list =[]
b1.place(x=0,y=0)
b2.place(x=201,y=0)
b3.place(x=401,y=0)
b4.place(x=0,y=201)
b5.place(x=201,y=201)
b6.place(x=401,y=201)
b7.place(x=0,y=401)
b8.place(x=201,y=401)
b9.place(x=401,y=401)
root.mainloop()
