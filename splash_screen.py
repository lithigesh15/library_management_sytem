from tkinter.ttk import Progressbar
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import center_screen
import pyglet

pyglet.font.add_file(fr'.\fonts\Game Of Squids.ttf')

def f1(master,gif,x=300,y=300,delay=0):
    master.focus_set()
    global img
    img=Image.open(fr".\Images\{gif}.gif")
    
    text=Label(master,text="GETTING",fg="white",font=("Game Of Squids",18,"bold"),bg="#1F6DC7")
    text1=Label(master,text="STARTED",fg="white",font=("Game Of Squids",18,"bold"),bg="#1F6DC7")
    text2=Label(master,text=".",fg="white",font=("Game Of Squids",18,"bold"),bg="#1F6DC7")
    text.place(x=20,y=10)
    text1.place(x=70,y=40)
    text2.place(x=225,y=40)
    s = ttk.Style()
    s.theme_use('clam')
    s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f',thickness=50)

    pb=Progressbar(master,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=350,mode='determinate',)
    pb.place(x=-10,y=240)

    f1=Frame(master,bg="white",highlightthickness=0,border="0")
    f1.place(x=0,y=82)
    l1=Label(f1,border=0,highlightthickness=0)
    l1.pack()

    def f2(t=0):
        try:
            for a in ImageSequence.Iterator(img):
                if t%2==0 and t%6==0:
                    if (t-1)%5==4:
                        pass
                    else:
                        new_str="."*((t-1)%5)
                        text2.configure(text=new_str)
                a.resize((x,y))
                a=ImageTk.PhotoImage(a)
                l1.configure(image=a)
                master.update()
                t+=1

                if pb['value']<100:
                    pb['value']+=1
                    master.update_idletasks()
                    time.sleep(0.01)
                else:
                    master.destroy()
                    w1.deiconify()
                    break
                time.sleep(delay) # Use this only to delay the gif loading speed
                
            #img.seek(0)
        except:
            return
        master.after(0,f2)
    f2()
    #master.mainloop()
