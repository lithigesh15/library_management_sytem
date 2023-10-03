from tkinter import *
from PIL import Image,ImageTk
import center_screen
import pyglet
from tkinter import messagebox,ttk
import splash_screen
import mysql.connector as sql
import pie_chart
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

pyglet.font.add_file('.\\fonts\Louis George Cafe.ttf')
#pyglet.font.add_file('.\\fonts\CaviarDreams.ttf')

db=sql.connect(host='localhost',user='root',password='root',database="lib")
cursor=db.cursor()


def f1():
    w1=Tk()
    w1.configure(bg="#646FF9")
    w1.title("Admin")
    w1.resizable(False,False)
    center_screen.center_screen(900,550,w1)
    w1.overrideredirect(True)

    global Log_bg
    Log_bg=Image.open(".\\LoginIcons\\login.png")
    Log_bg=Log_bg.resize((550,550),Image.ANTIALIAS)
    Log_bg=ImageTk.PhotoImage(Log_bg)
    Login_bg=Label(w1,image=Log_bg,border=0)
    Login_bg.pack(side=LEFT)

    #Declaring string variables for 2 entry widgets
    uname_var=StringVar()
    passwd_var=StringVar()

    uname_var.set("Enter Username...")
    passwd_var.set("Enter Password...")
    
    # Welcome Message
    L1=Label(w1,text="Welcome !",bg="#646FF9",fg="white",font=("Louis George Cafe",15))
    L1.place(x=680,y=20)
    L2=Label(w1,text="Login to your account",bg="#646FF9",fg="white",font=("Louis George Cafe",12))
    L2.place(x=650,y=60)

    # Declaring a Frame for displaying error message
    def close_invalid():
        invalid.place_forget()
        
    global inv,clear
    def create_icon(x,y=30,z=30):
        ico=Image.open(f".\\LoginIcons\\minor icons\\{x}")
        ico=ico.resize((y,z))
        
        return ImageTk.PhotoImage(ico)
    
    invalid=Frame(w1,bg="#E97451",bd=0,height=20,width=215)
    #invalid.place(x=620,y=110) # This is the location of error message
    invalid.pack_propagate(False)
    invalid_txt=Label(invalid,text="Invalid Credentials ",font=("Open Sans",9),bg="#E97451",fg="#FFCCCB")
    invalid_txt.place(x=25,y=0)
    inv=create_icon("invalid.png",13,13)
    inv_ico=Label(invalid,image=inv,bg="#E97451")
    inv_ico.place(x=0,y=2)

    global clear
    clear=create_icon("exit1.png",13,13)
    clear_ico=Button(invalid,image=clear,bg="#E97451",activebackground="#E97451",bd=0,cursor="hand2",command=close_invalid)
    clear_ico.place(x=195,y=2)
    
    # Username
    L3=Label(w1,text="Username :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
    L3.place(x=617,y=145)
    e1=Entry(w1,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=uname_var,fg="#343434")
    e1.place(x=620,y=185)
    line1=Frame(w1,height=2,width=215,bg="white")
    line1.place(x=620,y=210)

    # Password
    bullet=u"\u25CF"
    L4=Label(w1,text="Password :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
    L4.place(x=617,y=235)
    e2=Entry(w1,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=passwd_var,fg="#343434")
    e2.place(x=620,y=275)
    line2=Frame(w1,height=2,width=215,bg="white")
    line2.place(x=620,y=300)
    
    # Binding options for help text
    def default_change(e):
        if uname_var.get()=="Enter Username...":
            uname_var.set("")
    def default_change_(e):
        if passwd_var.get()=="Enter Password...":
            passwd_var.set("")
            e2.configure(show=bullet)

    e1.bind("<Button-1>",default_change)
    e1.bind("<FocusIn>",default_change)

    e2.bind("<Button-1>",default_change_)
    e2.bind("<FocusIn>",default_change_)
    
    # Adding icons near entry widget
    global lock,passwd
    
    def create_icon(x,y=30,z=30):
        ico=Image.open(f".\\LoginIcons\\minor icons\\{x}")
        ico=ico.resize((y,z))
        return ImageTk.PhotoImage(ico)

    lock=create_icon("uname.png")
    lock_ico=Label(w1,image=lock,bg="#646FF9")
    lock_ico.place(x=580,y=185)

    passwd=create_icon("passwd.png")
    passwd_ico=Label(w1,image=passwd,bg="#646FF9")
    passwd_ico.place(x=580,y=275)

    # Executing mysql query
    cursor.execute("select * from admin")
    result=cursor.fetchall()
    uname_l=[]
    passwd_l=[]
    for a in result:
        uname_l+=[a[0]]
        passwd_l+=[a[1]]
      
    # Login Button
    my_uname=''
    data_id=0
    def log_check():
        if uname_var.get() in uname_l:
            data_id=uname_l.index(uname_var.get())
            pass_id=passwd_l[data_id]
            if pass_id==passwd_var.get():
                w1.withdraw()
                #print("Query Ok")
                my_uname=uname_var.get()
                load=Toplevel(w1) # Loading screen
                load.overrideredirect(True)
                center_screen.center_screen(300,255,load)
                load.configure(bg="#1F6DC7")
                    
                splash_screen.f1(load,"book_shelf1",delay=0.025)
                w1.destroy()
                main_win=Tk()
                main_win.title("Main")
                main_win.configure(bg="#EDE7E7")
                main_win.overrideredirect(True)
                main_win.state("zoomed")
                # Style
                style=ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview.Heading",font=("Georgia",11),foreground="white",background="#646ff9",borderwidth=0.5)
                style.configure("Treeview",rowheight=30,font=("Calibri",11))
                style.configure("TCombobox",selectbackground='',fieldbackground='#EDE7E7',background='#12A5BF',selectforeground="")
                style.map("Treeview",background=[("selected","grey")])
                    
                # Menu Bar Frame
                global ad_ico,ad_ico1
                def create_icon(x,y=30,z=30):
                    ico=Image.open(f".\\adminIcons\\{x}")
                    ico=ico.resize((y,z))
                    return ImageTk.PhotoImage(ico)
                ad_ico=create_icon("ad_ico.png",35,35)
                ad_ico1=create_icon("3line.png")
            
                menu_f=Frame(main_win,width=1400,height=50,bg="#646FF9")
                menu_f.place(x=0,y=0)
                l1=Label(menu_f,image=ad_ico,bg="#646FF9")
                _3line=Label(menu_f,image=ad_ico1,bg="#646FF9")
                if len(my_uname)>5:
                    my_uname=my_uname[:5]+'...'
                ad_label=Label(menu_f,text=f"Welcome , {my_uname.capitalize()}",font=("Louis George Cafe",13),bg="#646FF9",fg="white")
                ad_label.place(x=1150,y=10)

                l1.place(x=1100,y=3)
                _3line.place(x=10,y=5)
                
                dc_txt=Label(menu_f,text="Library Management System",font=("Louis George Cafe",13),bg="#646FF9",fg="white")
                dc_txt.place(x=60,y=10)
                
                # Side Frame - bg = #333333
                fs=Frame(main_win,width=300,height=720,bg="#333333")
                fs.pack_propagate(False)
                fs.place(x=0,y=50)

    
                #### Creating function block for all the buttons one by one ###
                """ Inorder to implement button wise action in single frame lets create multipurpose single frame """
                
                main_frame=Frame(main_win,height=720,width=1400,bg="#EDE7E7")
                main_frame.place(x=300,y=50)
                main_frame.pack_propagate(False)
                
                # Dashboard - Home Button
                my_tree1=''
                change_home_value=0
                def home_b(e):
                    global my_tree1
                    home_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    home_frame.place(x=0,y=0)
                    home_frame.pack_propagate(False)
                
                    global b_ico,s_ico,i_ico,r_ico
                    b_ico=create_icon("b_ico.png",50,50)
                    s_ico=create_icon("memb.png",50,50)
                    i_ico=create_icon("ib1_ico.png",50,50)
                    r_ico=create_icon("rb1_ico.png",45,50)
                    
                    b_l=Label(home_frame,text="Books",font=("Candara",15),bg="#EDE7E7",fg="#696969")
                    b_l.place(x=30,y=50)
                    sub_f=Frame(home_frame,width=200,height=150,bg="#A9A9A9")
                    sub_f.place(x=30,y=90)
                    Frame(sub_f,width=200,height=20,bg="#646FF9").place(x=0,y=0)
                    Label(sub_f,image=b_ico,bg="#A9A9A9").place(x=10,y=50)
                    Label(sub_f,text="1091",font=("Arial",26),fg="#696969",bg="#A9A9A9").place(x=85,y=50)
                    
                    s_l=Label(home_frame,text="Students",font=("Candara",15),bg="#EDE7E7",fg="#696969")
                    s_l.place(x=280,y=50)
                    sub_f1=Frame(home_frame,width=200,height=150,bg="#A9A9A9")
                    sub_f1.place(x=280,y=90)
                    Frame(sub_f1,width=200,height=20,bg="#FF3131").place(x=0,y=0)
                    Label(sub_f1,image=s_ico,bg="#A9A9A9").place(x=10,y=50)
                    Label(sub_f1,text="740",font=("Arial",26),fg="#696969",bg="#A9A9A9").place(x=85,y=50)
                    
                    i_l=Label(home_frame,text="Issued Books",font=("Candara",15),bg="#EDE7E7",fg="#696969")
                    i_l.place(x=530,y=50)
                    sub_f2=Frame(home_frame,width=200,height=150,bg="#A9A9A9")
                    sub_f2.place(x=530,y=90)
                    Frame(sub_f2,width=200,height=20,bg="#646FF9").place(x=0,y=0)
                    Label(sub_f2,image=i_ico,bg="#A9A9A9").place(x=10,y=50)
                    Label(sub_f2,text="800",font=("Arial",26),fg="#696969",bg="#A9A9A9").place(x=85,y=50)
                    
                    r_l=Label(home_frame,text="Returned Books",font=("Candara",15),bg="#EDE7E7",fg="#696969")
                    r_l.place(x=780,y=50)
                    sub_f3=Frame(home_frame,width=200,height=150,bg="#A9A9A9")
                    sub_f3.place(x=780,y=90)
                    Frame(sub_f3,width=200,height=20,bg="#FF3131").place(x=0,y=0)
                    Label(sub_f3,image=r_ico,bg="#A9A9A9").place(x=10,y=50)
                    Label(sub_f3,text="291",font=("Arial",26),fg="#696969",bg="#A9A9A9").place(x=85,y=50)

                    
                    # Frame 1 containing frame 2
                    pie_f=Frame(home_frame,height=350,width=500,highlightthickness=3,highlightbackground="black",bg="#EDE7E7")
                    pie_f.place(x=550,y=325)
                    Label(pie_f,text="Top Issued Books - Category Wise",font=("Candara",15),bg="#EDE7E7",fg="#36454F").place(x=50,y=20)
                    # Frame 2 containing Pie chart
                    pie_f1=Frame(pie_f,height=290,width=440)
                    pie_f1.place(x=20,y=50)
                    
                    pie=pie_chart.pie_chart(pie_f1,size=(6,3.5),title="",l_title="Genre",shadow=True,values=(1,2,0.5,1,1),startangle=90,labels=("Action & Adv.","Comics","Educational","Fantasy","Others"),explode=(0.02,0.1,0.01,0.02,0.02))
                    pie= FigureCanvasTkAgg(pie, pie_f1)
                    pie.get_tk_widget().place(x=-160,y=-20)

                    # Creating table
                    
                    Label(home_frame,text="Latest     ADD-ONS",font=("Candara",15),bg="#EDE7E7",fg="#36454F").place(x=30,y=285)
                
                    db=sql.connect(user="root",host="localhost",database="lib",passwd="root")
                    cursor=db.cursor()
                    cursor.execute("select * from books2 order by date_")
                    data=cursor.fetchall()
                    new_data=[]
                    for a in range(1,21):
                        a=-a
                        new_data.append(data[a])
                    f1=Frame(home_frame,width=500,height=350)
                    f1.place(x=30,y=325)
                    f1.pack_propagate(False)

                    # Treeview scrollbar
                    sb=ttk.Scrollbar(f1)
                    sb.pack(side="right",fill="y")

                    sb1=ttk.Scrollbar(f1,orient="horizontal")
                    sb1.pack(side="bottom",fill="x")

                    # Create Treeview
                    columns = ('s_no', 'title',"copies","date")
                    my_tree1=ttk.Treeview(f1,yscrollcommand=sb.set,selectmode="extended",column=columns,show="headings",height=8,xscrollcommand=sb1.set)
                    my_tree1.pack(fill="both",expand=1)


                    # define headings
                    my_tree1.column(0,width=50,minwidth=50)
                    my_tree1.heading('s_no', text='S.No',anchor="w")
                    my_tree1.column(1,width=250,minwidth=90)
                    my_tree1.heading('title', text='Name',anchor="w")
                    my_tree1.column(2,width=80,minwidth=50)
                    my_tree1.heading('copies', text='Copies',anchor="w")
                    my_tree1.column(3,width=100,minwidth=50)
                    my_tree1.heading('date', text='Date',anchor="w")

                    # add data to the treeview
                    count=0
                    for new_data in new_data:
                        if new_data[0]==0:
                            continue
                        date=new_data[-1]
                        new_data=list(new_data)
                        new_data=[count+1,new_data[2],new_data[-2],new_data[-1]]
                        
                        if count%2==0:
                            my_tree1.insert('', END, values=new_data,tag=("odd"))
                        else:
                            my_tree1.insert('', END, values=new_data,tag=("even"))
    
                        count+=1
                    """children=my_tree.get_children()
                    if children:
                        my_tree.focus(children[0])
                        my_tree.selection_set(children[0])"""
                    # Configure the scrollbar
                    sb.config(command=my_tree1.yview)
                    sb1.config(command=my_tree1.xview)

                    my_tree1.tag_configure("odd",background="silver")

                    global change_home_value,change_home
                    change_home_value=1
                    def change_home(e):
                        global change_home_value
                        if change_home_value%2==0:
                            fs1.place_forget()
                            fs.place(x=0,y=50)
                            main_frame.place(x=300,y=50)
                            s_l.place(x=280,y=50);sub_f1.place(x=280,y=90)
                            i_l.place(x=530,y=50);sub_f2.place(x=530,y=90)
                            r_l.place(x=780,y=50);sub_f3.place(x=780,y=90)
                            pie_f.place(x=550,y=325)
                            f1.configure(width=500)
                            
                        else:
                            fs.place_forget()
                            fs1.place(x=0,y=50)
                            main_frame.place(x=80,y=50)
                            s_l.place(x=340,y=50);sub_f1.place(x=340,y=90)
                            i_l.place(x=660,y=50);sub_f2.place(x=660,y=90)
                            r_l.place(x=980,y=50);sub_f3.place(x=980,y=90)
                            pie_f.place(x=720,y=325)
                            f1.configure(width=660)
                        change_home_value+=1
                    
                    _3line.bind("<Button-1>",change_home)

                def memb_b(e):
                    memb_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    memb_frame.place(x=0,y=0)
                    memb_frame.pack_propagate(False)

                def m_book(e):
                    fs.place_forget()
                    fs1.place(x=0,y=50)
                    main_frame.place(x=50,y=50)
                    m_b_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    m_b_frame.place(x=0,y=0)
                    m_b_frame.pack_propagate(False)
                    def create_icon(x,y=30,z=30):
                        ico=Image.open(f".\\bookIcons\\{x}")
                        ico=ico.resize((y,z))
                        return ImageTk.PhotoImage(ico)
                    global m_b_ico
                    m_b_ico=create_icon("m_b_ico.png",50,50)

                    # SQL Connection
                    db=sql.connect(user="root",host="localhost",database="lib",passwd="root")
                    cursor=db.cursor()
                    
                    # Upper Frame
                    #u_f=Frame(m_b_frame,bg="silver",height=60)
                    #u_f.pack(fill="x")
                    mb_l=Label(m_b_frame,text="       Manage Books",font=("Candara",15),bg="#ede7e7",fg="#36454f",image=m_b_ico,compound="left")
                    mb_l.place(x=295,y=25)
                    mb_lf=Frame(m_b_frame,width=250,height=2,bg="#696969")
                    mb_lf.place(x=280,y=95)
                    
                    # Side_frame for updating list
                    global side_f
                    # Declaring string variables
                    b_id=StringVar();b_name=StringVar();author=StringVar();genre=StringVar();qty=StringVar()
                    b_name.set("Enter book name...");author.set("Enter author name - opt.")
                    genre.set("Enter genre...");qty.set("Enter quantity...")

                    # Default book id :
                    def set_bid():
                        cursor.execute("select * from books2 order by id")
                        global count,count1,count2
                        res=cursor.fetchall()
                        count=res[-1][0]
                        count1=res[-1][1]
                        count2=res[-1][-2]
                        if count1==0:
                            count1=1001
                        b_id.set(count1+count2)
                    set_bid()

                    side_f=Frame(m_b_frame,bg='#12A5BF',height=750,width=430)
                    side_f.place(x=900,y=0)

                    # Creating Table
                    cursor.execute("select * from books2 order by id")
                    data=cursor.fetchall()
    
                    f1=Frame(m_b_frame,width=800,height=510)
                    f1.place(x=50,y=150)
                    f1.pack_propagate(False)
    
                    # Treeview scrollbar
                    sb=ttk.Scrollbar(f1)
                    sb.pack(side="right",fill="y")

                    sb1=ttk.Scrollbar(f1,orient="horizontal")
                    sb1.pack(side="bottom",fill="x")

                    # Create Treeview
                    columns = ('b_id', 'title',"author",'genre',"qty")
                    my_tree=ttk.Treeview(f1,yscrollcommand=sb.set,selectmode="extended",column=columns,show="headings",height=8,xscrollcommand=sb1.set)
                    my_tree.pack(fill="both",expand=1)


                    # define headings
                    my_tree.column(0,width=40,minwidth=40)
                    my_tree.heading('b_id', text='Book ID',anchor="w")
                    my_tree.column(1,width=160,minwidth=90)
                    my_tree.heading('title', text='Book Name',anchor="w")
                    my_tree.column(2,width=80,minwidth=50)
                    my_tree.heading('author', text='Author',anchor="w")
                    my_tree.column(3,width=100,minwidth=50)
                    my_tree.heading('genre', text='Genre',anchor="w")
                    my_tree.column(4,width=30,minwidth=30)
                    my_tree.heading('qty', text='Qty',anchor="w")

                    # add data to the treeview
                    global count
                    count=0
                    for new_data in data:
                        if new_data[0]==0:
                            continue
                        date=new_data[-1]
                        new_data=list(new_data)
                        new_data=[new_data[1],new_data[2],new_data[3],new_data[-3],new_data[-2]]
                        global my_tree1
                        if count%2==0:
                            my_tree.insert('', END, values=new_data,tag=("odd"))
                            my_tree1.insert('', END, values=new_data,tag=("odd"))
                        else:
                            my_tree.insert('', END, values=new_data,tag=("even"))
                            my_tree1.insert('', END, values=new_data,tag=("even"))
                        count+=1
                    # Configure the scrollbar
                    sb.config(command=my_tree.yview)
                    sb1.config(command=my_tree.xview)

                    my_tree.tag_configure("odd",background="silver")
                    
                    # Subsidary side frames
                    side_f1=Frame(side_f,bg='#12A5BF',height=750,width=430);side_f1.place(x=0,y=0)
                    side_f2=Frame(side_f,bg='#12A5BF',height=750,width=430)
                    side_f3=Frame(side_f,bg='#12A5BF',height=750,width=430)
                    global side_f_count
                    side_f_count=1
                    def change_side_f(e):
                        global side_f_count
                        if side_f_count%3==1:
                            side_f1.place_forget()
                            side_f2.place(x=0,y=0)
                        elif side_f_count%3==2:
                            side_f2.place_forget()
                            side_f3.place(x=0,y=0)
                            for s in my_tree.get_children():
                                my_tree.delete(s)
                            cursor.execute("select id,name,author,genre,copies from books2 order by id")
                            my_data=cursor.fetchall()
                            count_=0;loop_1=0
                            for a in my_data:
                                if loop_1==0:
                                    loop_1=1
                                    continue
                                if count_%2==0:
                                    my_tree.insert('', END, values=a,tag=("odd"))
                                else:
                                    my_tree.insert('', END, values=a,tag=("even"))
                                count_+=1
                            my_tree.tag_configure("odd",background="silver")
                        else:
                            side_f3.place_forget()
                            side_f1.place(x=0,y=0)
                            for s in my_tree.get_children():
                                my_tree.delete(s)
                            cursor.execute("select id,name,author,genre,copies from books2 order by id")
                            my_data=cursor.fetchall()
                            count_=0;loop_1=0
                            for a in my_data:
                                if loop_1==0:
                                    loop_1=1
                                    continue
                                if count_%2==0:
                                    my_tree.insert('', END, values=a,tag=("odd"))
                                else:
                                    my_tree.insert('', END, values=a,tag=("even"))
                                count_+=1
                            my_tree.tag_configure("odd",background="silver")
                        side_f_count+=1
                    
                    Frame(side_f,bg="#FFFFFF",height=2,width=1300).place(x=0,y=0)
                    Frame(side_f,bg="#696969",width=2,height=1300).place(x=0,y=2)
                    Label(side_f,text="Add     |   Update   |     Delete ",font=("Candara",16),fg="white",bg="#12A5BF").place(x=80,y=50)
                    #-SIDE F1-----------------------------------
                    # OLD side frame background color - "#008e97"
                    #Frame(main_frame,bg="#333333",height=3,width=1300).place(x=0,y=715)
                    Frame(side_f1,width=47,height=2,bg="white").place(x=80,y=90)

                    def add_book():
                        if b_name.get()=="" or e4.get()=="select" or choice.get()=="" or qty.get()=="":
                            messagebox.showerror("Invalid Input","One/More required fields are empty")
                        else:
                            global count
                            from datetime import date
                            auth=''
                            if author.get()=="Enter author name - opt.":
                                auth=''
                            else:
                                auth=author.get()
                            
                            data=[b_id.get(),b_name.get(),auth,choice.get(),qty.get()]
                            Date=StringVar();Date.set(date.today())
                            cursor.execute("select max(sno) from books2");sno=cursor.fetchall()
                            sno=sno[0][0]+1
                            cursor.execute(f"insert into books2 values ({sno},{b_id.get()},'{b_name.get()}','{auth}','{choice.get()}',{qty.get()},'{Date.get()}')")
                            db.commit()
                            messagebox.showinfo("Success","Book(s) added successfully")
                            set_bid()
                            author.set("Enter author name - opt.");b_name.set("")
                            choice.set("select");qty.set("Enter quantity...")
                            e2.focus()
                            
                            if count%2==0:
                                my_tree.insert('', END, values=data,tag=("odd"))
                            else:
                                my_tree.insert('', END, values=data,tag=("even"))

                    global img,img1,img2,img3,img4
                    Label(side_f1,text="Book ID",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=150)
                    img=create_icon("b_id_ico.png")
                    Label(side_f1,image=img,bg="#12A5BF").place(x=15,y=180)
                    e1=Entry(side_f1,font=("TimesNewRoman",11),width=39,bg="#12A5BF",bd=0,fg="#343434",textvariable=b_id,state="disabled",cursor='',disabledbackground="#12A5BF",disabledforeground='silver');e1.place(x=75,y=190)
                    Frame(side_f1,width=320,height=2,bg="white").place(x=70,y=215)

                    Label(side_f1,text="Book Name",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=240)
                    img1=create_icon("b_name_ico.png")
                    Label(side_f1,image=img1,bg="#12A5BF").place(x=15,y=270)
                    e2=Entry(side_f1,font=("TimesNewRoman",11),width=39,bg="#12A5BF",bd=0,fg="#343434",textvariable=b_name);e2.place(x=75,y=280)
                    Frame(side_f1,width=320,height=2,bg="white").place(x=70,y=305)

                    Label(side_f1,text="Author Name",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=330)
                    img2=create_icon("b_author_ico.png")
                    Label(side_f1,image=img2,bg="#12A5BF").place(x=15,y=350)
                    e3=Entry(side_f1,font=("TimesNewRoman",11),width=39,bg="#12A5BF",bd=0,fg="#343434",textvariable=author);e3.place(x=75,y=370)
                    Frame(side_f1,width=320,height=2,bg="white").place(x=70,y=395)

                    Label(side_f1,text="Choose Genre",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=420)
                    img3=create_icon("b_genre_ico.png")
                    Label(side_f1,image=img3,bg="#12A5BF").place(x=15,y=440)
                    #e4=Entry(side_f,font=("TimesNewRoman",11),width=39,bg="#12A5BF",bd=0,fg="#343434",textvariable=genre).place(x=75,y=460)
                    #Frame(side_f,width=320,height=2,bg="white").place(x=70,y=485)
                    # Combobox
                    
                    choice=StringVar()
                    e4=ttk.Combobox(side_f1,font=("Open Sans",11),width=37,state="readonly",textvariable=choice)
                    e4.place(x=75,y=460)
                    e4["values"]=("Write Own...","Action and Adventure","Autobiography","Biography","Classics","Comics","Crime & Mystery","Educational","Fantasy","Humor and Satire","Horror","Memoirs","Sci-Fi","Tragedy")
                    choice.set("select")
                    # Creating binding event for combobox
                    def select(e):
                        if choice.get()=="Write Own...":
                            e4.configure(state="normal")
                            choice.set("")
                    e4.bind("<<ComboboxSelected>>",select)

                    Label(side_f1,text="Enter Quantity",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=510)
                    img4=create_icon("b_no_ico.png")
                    Label(side_f1,image=img4,bg="#12A5BF").place(x=15,y=530)
                    e5=Entry(side_f1,font=("TimesNewRoman",11),width=39,bg="#12A5BF",bd=0,fg="#343434",textvariable=qty);e5.place(x=75,y=550)
                    Frame(side_f1,width=320,height=2,bg="white").place(x=70,y=575)
                   
                    # Binding Options
                    def default_change(e):
                        if b_name.get()=="Enter book name...":
                            b_name.set('')
                    def default_change1(e):
                        if author.get()=="Enter author name - opt.":
                            author.set('')
                    def default_change2(e):
                        if qty.get()=="Enter quantity...":
                            qty.set('')
                    
                        
                    e2.bind("<FocusIn>",default_change);e2.bind("<Return>",lambda e:e3.focus())
                    e3.bind("<FocusIn>",default_change1);e3.bind("<Return>",lambda e:e4.focus())
                    e5.bind("<FocusIn>",default_change2);e4.bind("<Return>",lambda e:e5.focus())

                    #-SIDE F2------------------------------------------------------------------
                    Frame(side_f2,width=67,height=2,bg="white").place(x=165,y=90)
                    #String Variables
                    b_idf2=StringVar();b_namef2=StringVar();authorf2=StringVar()
                    b_idf2.set("Enter book id to search...")
                    b_namef2.set("Enter new book name...")
                    authorf2.set("Enter new author name...")
                    # Sch block
                    cur=db.cursor()
                    
                    block_info=0
                    sch_data=0
                    my_id=0
                    def check_book():
                        cur.execute("select min(id),max(id) from books2 where id>1000")
                        my_range=cur.fetchall();my_range=my_range[0]
                        cur.execute(f"select copies from books2 where id={my_range[1]}")
                        copies_max=cur.fetchall()
                        my_range=[my_range[0],my_range[1]+copies_max[0][0]]

                        global block_info,sch_data
                        if b_idf2.get()=="" or b_idf2.get()=="Enter book id to search...":
                            messagebox.showerror("Invalid","Enter a valid book id ...")
                            return
                        cur.execute("select id,copies from books2");id_copies_list=cur.fetchall()
                        id_copies_list.remove((1000,1))
                        id_list=[]
        
                        for a in id_copies_list:
                            id_list.append(a[0])
                        b_id=int(b_idf2.get())
                        if b_id in id_list:
                            cur.execute(f"select id,name,author,genre,copies from books2 where id={b_id}")
                            sch_data=cur.fetchall()
                            messagebox.showinfo('Success',"Book Search Successful ...")
                            for item in my_tree.get_children():
                                my_tree.delete(item)
                            my_tree.insert('', END, values=sch_data[0],tag=('odd'))
                            my_tree.tag_configure("odd",background="silver")

                            if sch_data[0][-1]==1:
                                block_info='1_0 block'
                            else:
                                block_info='1_1 block'
                    
                        elif b_id in range(my_range[0],my_range[1]):
                            global my_id
                            block_info='2nd block'
                            for a in id_copies_list:
                                if b_id in range(a[0],a[0]+a[1]+1):
                                    my_id=a[0]
                            cur.execute(f"select id,name,author,genre,copies from books2 where id={my_id}")
                            sch_data=cur.fetchall();sch_data=list(sch_data[0]);sch_data[0]=b_id;sch_data[-1]=1
                            messagebox.showinfo('Success',"Book Search Successful ...")
                            for item in my_tree.get_children():
                                my_tree.delete(item)
                            my_tree.insert('', END, values=sch_data,tag=('odd'))
                            my_tree.tag_configure("odd",background="silver")
                        else:
                            messagebox.showinfo("Invalid","No Matching book found ...")
                            return
                        e1_f2.configure(state="normal");e2_f2.configure(state="normal")
                        e3_f2.configure(state="normal")
                        e4_f2.configure(state="readonly",textvariable=choice_f2)
                    def update_book():
                        global block_info,sch_data,my_id
                        
                        if b_idf2.get()=="" or b_idf2.get()=="Enter book id to search...":
                            messagebox.showerror("Invalid","Enter a valid book id ...")
                        elif (b_namef2.get()=='' or b_namef2.get()=='Enter new book name...') or (choice_f2.get()=='select' or choice_f2.get()==''):
                            messagebox.showerror("Invalid","One or more required fields are empty ...")
                        else:
                            auth=''
                            if authorf2.get()=="" or authorf2.get()=='Enter new author name...':
                                auth=''
                            else:
                                auth=authorf2.get()
                            if True:
                                cur.execute('select max(sno) from books2');sno=cur.fetchall();sno=sno[0][0]+1
                                Date=date.today()
                                final_data=(sno,b_idf2.get(),b_namef2.get(),auth,choice_f2.get(),1,str(Date))
                                b_id=int(b_idf2.get())
                                if block_info=='1_0 block':
                                    sch_data=list(sch_data[0]);sch_data[0]=b_id
                                    update_query="id={},name='{}',author='{}',genre='{}',copies={},date_='{}'".format(final_data[1],final_data[2],final_data[3],final_data[4],final_data[5],final_data[6])
                                    query="update books2 set "+update_query+f" where id={b_id}"
                                    cur.execute(query)
                                
                                elif block_info=='1_1 block':
                                    cur.execute(f"update books2 set copies=copies-1,id=id+1 where id={b_id}")
                                    cur.execute(f"insert into books2 values {final_data}")
                                    
                                elif block_info=="2nd block":
                                    cur.execute(f"update books2 set copies=copies-1 where id={my_id}")
                                    cur.execute(f"insert into books2 values {final_data}")
                                    
                                db.commit()                            
                                messagebox.showinfo("Success","Data Updated Sucessfuly ...")
                                for item in my_tree.get_children():
                                    my_tree.delete(item)
                                my_tree.insert('',END,values=[b_idf2.get(),b_namef2.get(),auth,choice_f2.get(),1],tag=('odd'))
                                my_tree.tag_configure("odd",background="silver")
                                b_namef2.set("Enter new book name...");authorf2.set("Enter new author name...")
                                e2_f2.configure(state="disabled")
                                e3_f2.configure(state="disabled")
                                e4_f2.configure(state="disabled",textvariable=choice_f2);choice_f2.set('select')
                                
                    global sch_ico
                    sch_ico=create_icon("sch1.png",40,40)
                    
                    Label(side_f2,text="Book ID",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=150)
                    Label(side_f2,image=img,bg="#12A5BF").place(x=15,y=180)
                    e1_f2=Entry(side_f2,font=("TimesNewRoman",11),width=31,bg="#12A5BF",bd=0,fg="#343434",textvariable=b_idf2);e1_f2.place(x=75,y=190)
                    Frame(side_f2,width=260,height=2,bg="white").place(x=70,y=215)
                    sch_b=Button(side_f2,image=sch_ico,bg="#12A5BF",bd=0,activebackground="#12A5BF",cursor="hand2",command=check_book)
                    sch_b.place(x=340,y=180)

                    Label(side_f2,text="Book Name",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=255)
                    Label(side_f2,image=img1,bg="#12A5BF").place(x=15,y=285)
                    e2_f2=Entry(side_f2,font=("TimesNewRoman",11),width=31,bg="#12A5BF",bd=0,fg="#343434",textvariable=b_namef2,state='disabled',disabledbackground="#12A5BF",disabledforeground="#a9a9a9");e2_f2.place(x=75,y=295)
                    Frame(side_f2,width=260,height=2,bg="white").place(x=70,y=320)

                    Label(side_f2,text="Author Name",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=360)
                    Label(side_f2,image=img2,bg="#12A5BF").place(x=15,y=380)
                    e3_f2=Entry(side_f2,font=("TimesNewRoman",11),width=31,bg="#12A5BF",bd=0,fg="#343434",textvariable=authorf2,state='disabled',disabledbackground="#12A5BF",disabledforeground="#a9a9a9");e3_f2.place(x=75,y=400)
                    Frame(side_f2,width=260,height=2,bg="white").place(x=70,y=425)

                    Label(side_f2,text="Choose Genre",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=465)
                    Label(side_f2,image=img3,bg="#12A5BF").place(x=15,y=495)
                    # Combobox
                    
                    choice_f2=StringVar()
                    choice_f2.set('select')
                    e4_f2=ttk.Combobox(side_f2,font=("Open Sans",11),width=30,state="disabled")
                    e4_f2.place(x=75,y=505)
                    e4_f2["values"]=("Write Own...","Action and Adventure","Autobiography","Biography","Classics","Comics","Crime & Mystery","Educational","Fantasy","Humor and Satire","Horror","Memoirs","Sci-Fi","Tragedy")
                    
                    # Creating binding event for combobox
                    def select(e):
                        if choice_f2.get()=="Write Own...":
                            e4_f2.configure(state="normal")
                            choice_f2.set("")
                    e4_f2.bind("<<ComboboxSelected>>",select)

                    # Binding Options
                    def default_change_f2(e):
                        if b_idf2.get()=="Enter book id to search...":
                            b_idf2.set("")
                    e1_f2.bind("<FocusIn>",default_change_f2);e1_f2.bind("<Return>",lambda e:sch_b.focus())

                    def default_change(e):
                        if b_namef2.get()=="Enter new book name...":
                            b_namef2.set('')
                    def default_change1(e):
                        if authorf2.get()=="Enter new author name...":
                            authorf2.set('')
                        
                    e2_f2.bind("<FocusIn>",default_change);e2_f2.bind("<Return>",lambda e:e3_f2.focus())
                    e3_f2.bind("<FocusIn>",default_change1);e3_f2.bind("<Return>",lambda e:e4_f2.focus())

                    #-SIDE F3------------------------------------------------------------------
                    Frame(side_f3,width=64,height=2,bg="white").place(x=275,y=90)
                    #--------------------------------------------------------------------------
                    #String Variables
                    b_idf3=StringVar();b_namef3=StringVar();copiesf3=StringVar()
                    b_idf3.set("Enter book id to search ...")
                    b_namef3.set("Book name will appear here ...")
                    copiesf3.set("Copies of similar books ...")
                    cur1=db.cursor()
                    block_info1=0
                    sch_data1=0
                    my_id1=0
                    # Sch block
                    def check_book1():
                        cur1.execute("select min(id),max(id) from books2 where id>1000")
                        my_range=cur1.fetchall();my_range=my_range[0]
                        cur1.execute(f"select copies from books2 where id={my_range[1]}")
                        copies_max=cur1.fetchall()
                        my_range=[my_range[0],my_range[1]+copies_max[0][0]]

                        global block_info1,sch_data1,my_id1
                        if b_idf3.get()=="" or b_idf3.get()=="Enter book id to search...":
                            messagebox.showerror("Invalid","Enter a valid book id ...")
                            return
                        cur1.execute("select id,copies from books2");id_copies_list=cur1.fetchall()
                        id_copies_list.remove((1000,1))
                        id_list=[]
        
                        for a in id_copies_list:
                            id_list.append(a[0])
                        b_id=int(b_idf3.get())
                        if b_id in id_list:
                            my_id1=int(b_idf3.get())
                            cur1.execute(f"select id,name,author,genre,copies from books2 where id={b_id}")
                            sch_data1=cur1.fetchall()
                            messagebox.showinfo('Success',"Book Search Successful ...")
                            for item in my_tree.get_children():
                                my_tree.delete(item)
                            data=sch_data1[0];data=list(data)
                            data[-1]=1
                            my_tree.insert('', END, values=data,tag=('odd'))
                            my_tree.tag_configure("odd",background="silver")

                            if sch_data1[0][-1]==1:
                                block_info1='1_0 block'
                            else:
                                block_info1='1_1 block'
            
                        elif b_id in range(my_range[0],my_range[1]):
                            block_info1='2nd block'
                            for a in id_copies_list:
                                if b_id in range(a[0],a[0]+a[1]+1):
                                    my_id1=a[0]
                            cur1.execute(f"select id,name,author,genre,copies from books2 where id={my_id1}")
                            sch_data1=cur1.fetchall()
                            data=sch_data1[0];data=list(data)
                            data[-1]=1;data[0]=b_id
                            messagebox.showinfo('Success',"Book Search Successful ...")
                            for item in my_tree.get_children():
                                my_tree.delete(item)
                            my_tree.insert('', END, values=data,tag=('odd'))
                            my_tree.tag_configure("odd",background="silver")
                        else:
                            messagebox.showinfo("Invalid","No Matching book found ...")
                            return
                        # Reseting state to normal
                        b_namef3.set(f"{sch_data1[0][1]}")

                        id_=my_id1
                        if block_info1=='1_0 block':
                            copiesf3.set("0")
                            my_tree.insert('',END,values=['','','','',''],tag='even')
                            my_tree.insert('',END,values=['No Other Books ...','','','',''],tag='even')
                            l1.config(state='disabled');l2.config(state='disabled')
                            l1.unbind("<Button-1>");l2.unbind("<Button-1>")
                        
                            return

                        l1.config(state='normal');l2.config(state='normal')
                        l1.bind("<Button-1>",c_img);l2.bind("<Button-1>",c_img1)
                        cur1.execute(f"select id,name,author,genre,copies from books2 where id={my_id1}")
                        my_data=cur1.fetchone()
                        my_data=list(my_data)
                        l=[]
                        my_count=0;my_count1=0
                        my_bid=my_data[0]
                        #my_tree.insert('',END,values=['','','','',''],tag='even')
                        my_tree.insert('',END,values=['Similar Books :','','','',''],tag='even')
                        #my_tree.insert('',END,values=['','','','',''],tag='even')
                        for a in range(my_data[-1]):
                            new_bid=my_bid+my_count
                            my_data[0]=new_bid;my_data[-1]=1
                            my_count+=1
                            if new_bid==int(b_idf3.get()):
                                continue
                            my_count1+=1
                            if my_count1%2==1:
                                my_tree.insert('',END,values=my_data,tag='odd')
                            else:
                                my_tree.insert('',END,values=my_data,tag='even')
                            my_tree.tag_configure("odd",background="silver")
                        else:
                            copies=sch_data1[0][-1];copies-=1
                            copiesf3.set(f'{copies}')
                            if block_info1=="1_1 block":
                                data=sch_data1[0];data=list(data)
                                data[-1]=copies;data[0]=id_+1
                            else:
                                data=sch_data1[0];data=list(data)
                                data[-1]=copies
                    def delete_book():
                        global block_info1
                        if block_info1=="1_0 block":
                            cur1.execute(f'delete from books2 where id={int(b_idf3.get())}')
                            db.commit()
                            messagebox.showinfo("Success","Book Deleted Successfully ...")
                            return
                        if var.get()=='':
                            messagebox.showerror("Invalid",'Select your choice ...')
                            return
                        elif var.get()=='yes':
                            global my_id1
                            cur1.execute(f'delete from books2 where id={my_id1}')
                            db.commit()
                            messagebox.showinfo("Success","Books Deleted Successfully ...")
                        elif var.get()=='no':
                            print(my_id1)
                    # Labels and entries
                    global copies_ico,ques_ico
                    Label(side_f3,text="Book ID",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=150)
                    Label(side_f3,image=img,bg="#12A5BF").place(x=15,y=180)
                    e1_f3=Entry(side_f3,font=("TimesNewRoman",11),width=31,bg="#12A5BF",bd=0,fg="#343434",textvariable=b_idf3);e1_f3.place(x=75,y=190)
                    Frame(side_f3,width=260,height=2,bg="white").place(x=70,y=215)
                    sch_b=Button(side_f3,image=sch_ico,bg="#12A5BF",bd=0,activebackground="#12A5BF",cursor="hand2",command=check_book1)
                    sch_b.place(x=340,y=180)

                    Label(side_f3,text="Book Name",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=255)
                    Label(side_f3,image=img1,bg="#12A5BF").place(x=15,y=285)
                    e2_f3=Entry(side_f3,font=("TimesNewRoman",11),width=31,bg="#12A5BF",bd=0,fg="#343434",textvariable=b_namef3,state='disabled',disabledbackground="#12A5BF",disabledforeground="#a9a9a9");e2_f3.place(x=75,y=295)
                    Frame(side_f3,width=260,height=2,bg="white").place(x=70,y=320)

                    Label(side_f3,text="Copies - Similar books",fg="white",bg="#12A5BF",font=("Open Sans",13)).place(x=70,y=360)
                    copies_ico=create_icon('copies_ico.png',27,30)
                    Label(side_f3,image=copies_ico,bg="#12A5BF").place(x=15,y=390)
                    e3_f3=Entry(side_f3,font=("TimesNewRoman",11),width=31,bg="#12A5BF",bd=0,fg="#343434",textvariable=copiesf3,state='disabled',disabledbackground="#12A5BF",disabledforeground="#a9a9a9");e3_f3.place(x=75,y=400)
                    Frame(side_f3,width=260,height=2,bg="white").place(x=70,y=425)

                    Label(side_f3,text="Delete similar books",font=("Open Sans",13),fg="white",bg="#12A5BF").place(x=70,y=465)
                    ques_ico=create_icon('ques1.png')
                    Label(side_f3,image=ques_ico,bg="#12A5BF").place(x=15,y=495)

                    # Creating RadioButton
                    var=StringVar()
                    global i1,i2
                    i1=create_icon("rb_on1.png",20,20)
                    i2=create_icon("rb_of1.png",20,20)
                    l1=Label(side_f3,text=' Yes',image=i2,compound="left",bg="#12A5BF",fg="black",font=("Open Sans",10),state="disabled")
                    l1.place(x=72,y=505)
                    l2=Label(side_f3,text=' No',image=i2,compound="left",bg="#12A5BF",fg="black",font=("Open Sans",10),state="disabled")
                    l2.place(x=155,y=505)
                    def c_img(e):
                        l1.config(image=i1);l2.config(image=i2)
                        var.set("yes")
                        #print(var.get())
                    def c_img1(e):
                        l2.config(image=i1);l1.config(image=i2)
                        var.set('no')
                        #print(var.get())
                    #l1.bind("<Button-1>",c_img);l2.bind("<Button-1>",c_img1)
                    l1.unbind("<Button-1>");l2.unbind("<Button-1>")

                    # Binding Options
                    def default_change_f3(e):
                        if b_idf3.get()=="Enter book id to search ...":
                            b_idf3.set("")
                    e1_f3.bind("<FocusIn>",default_change_f3);e1_f3.bind("<Return>",lambda e:sch_b.focus())

                    def default_changef3(e):
                        if b_namef3.get()=="Book name will appear here...":
                            b_namef3.set('')
                    def default_changef31(e):
                        if authorf3.get()=="Author name will appear here...":
                            authorf3.set('')
                        
                    e2_f3.bind("<FocusIn>",default_change);e2_f3.bind("<Return>",lambda e:e3_f3.focus())
                    e3_f3.bind("<FocusIn>",default_change1);e3_f3.bind("<Return>",lambda e:e4_f3.focus())

                    
                    # Common Buttons
                    global add_ico,update_ico,delete_ico
                    add_ico=create_icon("add1.png",120,30)
                    b1=Button(side_f1,image=add_ico,cursor="hand2",bg="#12A5BF",bd=0,activebackground="#12A5BF",command=add_book);b1.place(x=70,y=620)
                    update_ico=create_icon("update1.png",120,30)
                    Button(side_f2,image=update_ico,cursor="hand2",bg="#12A5BF",bd=0,activebackground="#12A5BF",command=update_book).place(x=70,y=620)
                    
                    delete_ico=create_icon("delete1.png",120,30)
                    Button(side_f3,image=delete_ico,cursor="hand2",bg="#12A5BF",bd=0,activebackground="#12A5BF",command=delete_book).place(x=70,y=620)

                    global next_ico
                    next_ico=create_icon("arrow_icon.png",30,30)
                    L1=Label(side_f,image=next_ico,bg="#12A5BF",cursor="hand2");L1.place(x=200,y=620)
                    L1.bind("<Button-1>",change_side_f)

                    # Help Label
                    help_txt=Label(m_b_frame,text="TIP     :     You  can  resize  table  column  width  using  cursor.",font=("Candara",12,"bold"),fg="#696969",bg="#ede7e7")
                    help_txt.place(x=50,y=678)
                    
                    global change_home_value
                    def change_mb(e):
                        global change_home_value
                        if change_home_value%2==0:
                            fs1.place_forget()
                            fs.place(x=0,y=50)
                            main_frame.place(x=300,y=50)
                            f1.configure(width=1000)
                            side_f.place_forget()
                            mb_l.place(x=445,y=25)
                            mb_lf.place(x=425,y=95)
                        else:
                            fs.place_forget()
                            fs1.place(x=0,y=50)
                            f1.configure(width=800)
                            main_frame.place(x=50,y=50)
                            side_f.place(x=900,y=0)
                            mb_lf.place(x=275,y=95)
                            mb_l.place(x=295,y=25)
                        change_home_value+=1
                    
                    _3line.bind("<Button-1>",change_mb)
                    
                def m_student(e):
                    m_stu_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    m_stu_frame.place(x=0,y=0)
                    m_stu_frame.pack_propagate(False)

                    
                def i_b(e):
                    i_b_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    i_b_frame.place(x=0,y=0)
                    i_b_frame.pack_propagate(False)

                def r_b(e):
                    r_b_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    r_b_frame.place(x=0,y=0)
                    r_b_frame.pack_propagate(False)

                def v_record(e):
                    v_r_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    v_r_frame.place(x=0,y=0)
                    v_r_frame.pack_propagate(False)

                def edit(e):
                    edit_frame=Frame(main_frame,height=720,width=1400,bg="#EDE7E7")
                    edit_frame.place(x=0,y=0)
                    edit_frame.pack_propagate(False)
                    
                def logout(e):
                    res=messagebox.askquestion("Confirm","Confirm Logout?")
                    if res=='yes':
                        main_win.destroy()
                        f1()
                    
                # Header
                header_f=Frame(fs,bg="#333333",width=300,height=35)
                header_f.pack_propagate(False)
                header_f.place(x=0,y=20)
                header_txt=Label(header_f,text="Dashboard",fg="lightgrey",bg="#333333",font=("Louis George Cafe",11,"bold"))
                header_txt.place(x=10,y=3)

                # More and Less
                global more_ico,more_ico1,less_ico,less_ico1
                more_ico=create_icon("more.png",25,25)
                more_ico1=create_icon("more.png",30,30)
                less_ico=create_icon("less.png",25,25)
                less_ico1=create_icon("less.png",30,30)
                
                # Home Page Button
                global db_ico,db_ico1
                db_ico=create_icon("db_ico.png",25,25)
                db_ico1=create_icon("db_ico.png",32,32)
                
                db_l=Label(fs,text="    Home Page\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=db_ico,compound="left",border=0,width=350,height=40)
                db_l.place(x=-43,y=60)

                # Members Button
                global memb_ico,memb_ico1
                memb_ico=create_icon("memb.png")
                memb_ico1=create_icon("memb.png",34,34)

                memb_l=Label(fs,text="    Members\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=memb_ico,compound="left",border=0,width=350,height=40)
                memb_l.place(x=-43,y=110)

                # Header 2
                header_f2=Frame(fs,bg="#333333",width=300,height=35)
                header_f2.pack_propagate(False)
                header_f2.place(x=0,y=170)
                header_txt2=Label(header_f2,text="Features",fg="lightgrey",bg="#333333",font=("Louis George Cafe",11,"bold"))
                header_txt2.place(x=10,y=3)

                # Manage Books
                global mb_ico,mb_ico1
                mb_ico=create_icon("mb_ico.png",25,25)
                mb_ico1=create_icon("mb_ico.png",32,32)
                
                mb_l=Label(fs,text="    Manage Books\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=mb_ico,compound="left",border=0,width=350,height=40)
                mb_l.place(x=-43,y=210)

                # Manage students
                global ms_ico,ms_ico1
                ms_ico=create_icon("ms_ico.png",25,25)
                ms_ico1=create_icon("ms_ico.png",32,32)
                
                ms_l=Label(fs,text="    Manage Students\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=ms_ico,compound="left",border=0,width=350,height=40)
                ms_l.place(x=-13,y=260)

                # Issue Book
                global ib_ico,ib_ico1
                ib_ico=create_icon("ib_ico.png",25,25)
                ib_ico1=create_icon("ib_ico.png",32,32)
                
                ib_l=Label(fs,text="    Issue Book\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=ib_ico,compound="left",border=0,width=350,height=40)
                ib_l.place(x=-43,y=310)

                # Return Book
                global rb_ico,rb_ico1
                rb_ico=create_icon("rb_ico.png",25,25)
                rb_ico1=create_icon("rb_ico.png",32,32)
                
                rb_l=Label(fs,text="    Return Book\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=rb_ico,compound="left",border=0,width=350,height=40)
                rb_l.place(x=-43,y=360)

                # View Records
                global vr_ico,vr_ico1
                vr_ico=create_icon("vr_ico.png",25,25)
                vr_ico1=create_icon("vr_ico.png",32,32)
                
                vr_l=Label(fs,text="    View Records\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=vr_ico,compound="left",border=0,width=350,height=40)
                vr_l.place(x=-43,y=410)

                # Header 3
                header_f3=Frame(fs,bg="#333333",width=300,height=35)
                header_f3.pack_propagate(False)
                header_f3.place(x=0,y=460)
                header_txt3=Label(header_f3,text="Account",fg="lightgrey",bg="#333333",font=("Louis George Cafe",11,"bold"))
                header_txt3.place(x=10,y=3)
                
                # Edit
                global edit_ico,edit_ico1
                edit_ico=create_icon("edit_ico.png",23,23)
                edit_ico1=create_icon("edit_ico.png",30,30)
                
                edit_l=Label(fs,text="    Edit\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=edit_ico,compound="left",border=0,width=410,height=40)
                edit_l.place(x=-107,y=500)
                
                # Logout
                global logout_ico,logout_ico1
                logout_ico=create_icon("logout_ico.png",25,25)
                logout_ico1=create_icon("logout_ico.png",32,32)
                
                logout_l=Label(fs,text="    Logout\t\t",bg="#333333",fg="white",font=("Open Sans",11),image=logout_ico,compound="left",border=0,width=410,height=40)
                logout_l.place(x=-107,y=550)



                # Secondary side frame
                fs1=Frame(main_win,width=50,height=720,bg="#333333")
                fs1.pack_propagate(False)
                #fs1.place(x=0,y=50)
                #fs.place_forget()
                l_more=Label(fs1,image=more_ico,bg="#333333");l_more.place(x=10,y=280)
                global l_less
                l_less=Label(fs1,image=less_ico,bg="#333333")
                l_1=Label(fs1,image=db_ico,bg="#333333");l_1.place(x=10,y=40)
                l_2=Label(fs1,image=memb_ico,bg="#333333");l_2.place(x=8,y=100)
                l_3=Label(fs1,image=mb_ico,bg="#333333");l_3.place(x=10,y=160)
                l_4=Label(fs1,image=ms_ico,bg="#333333");l_4.place(x=10,y=220)
                l_5=Label(fs1,image=ib_ico,bg="#333333")
                l_6=Label(fs1,image=rb_ico,bg="#333333")
                l_7=Label(fs1,image=vr_ico,bg="#333333")
                l_8=Label(fs1,image=edit_ico,bg="#333333")
                l_9=Label(fs1,image=logout_ico,bg="#333333")
                f_dummy=Frame(fs1,bg="#333333",width=50,height=50)
                f_dummy.pack_propagate(False)
                    
                def change_config(x,y,z):
                    x.configure(image=y)
                    x.place(x=7,y=z)
                    
                def reverse(x,y,z):
                    x_=10
                    if x==l_2:
                        x_=8
                    x.configure(image=y)
                    x.place(x=x_,y=z)

                def more_config(e):
                    l_more.place_forget()
                    f_dummy.place_forget()
                    l_less.place(x=10,y=580)
                    l_5.place(x=10,y=280)
                    l_6.place(x=10,y=340)
                    l_7.place(x=10,y=400)
                    l_8.place(x=10,y=460)
                    l_9.place(x=10,y=520)

                def less_config(e):
                    f_dummy.place(x=10,y=580)
                    l_less.place_forget()
                    l_5.place_forget();l_6.place_forget();l_7.place_forget();l_8.place_forget();l_9.place_forget()
                    l_more.place(x=10,y=280)

                def change_home_page(e):
                    global change_home_value
                    change_home_value=1
                    home_b(e)
                    change_home(e)
                def change_mb_page(e):
                    global change_home_value
                    change_home_value=0
                    m_book(e)
                    
                l_1.bind("<Enter>",lambda e:change_config(l_1,db_ico1,40))
                l_1.bind("<Leave>",lambda e:reverse(l_1,db_ico,40))
                l_1.bind("<Button-1>",change_home_page)
                l_2.bind("<Enter>",lambda e:change_config(l_2,memb_ico1,100))
                l_2.bind("<Leave>",lambda e:reverse(l_2,memb_ico,100))
                l_3.bind("<Enter>",lambda e:change_config(l_3,mb_ico1,160))
                l_3.bind("<Leave>",lambda e:reverse(l_3,mb_ico,160))
                l_3.bind("<Button-1>",change_mb_page)
                l_4.bind("<Enter>",lambda e:change_config(l_4,ms_ico1,220))
                l_4.bind("<Leave>",lambda e:reverse(l_4,ms_ico,220))
                l_5.bind("<Enter>",lambda e:change_config(l_5,ib_ico1,280))
                l_5.bind("<Leave>",lambda e:reverse(l_5,ib_ico,280))
                l_6.bind("<Enter>",lambda e:change_config(l_6,rb_ico1,340))
                l_6.bind("<Leave>",lambda e:reverse(l_6,rb_ico,340))
                l_7.bind("<Enter>",lambda e:change_config(l_7,vr_ico1,400))
                l_7.bind("<Leave>",lambda e:reverse(l_7,vr_ico,400))
                l_8.bind("<Enter>",lambda e:change_config(l_8,edit_ico1,460))
                l_8.bind("<Leave>",lambda e:reverse(l_8,edit_ico,460))
                l_9.bind("<Enter>",lambda e:change_config(l_9,logout_ico1,520))
                l_9.bind("<Leave>",lambda e:reverse(l_9,logout_ico,520))
                l_9.bind("<Button-1>",logout)

                l_more.bind("<Enter>",lambda e:change_config(l_more,more_ico1,280))
                l_more.bind("<Leave>",lambda e:reverse(l_more,more_ico,280))
                l_more.bind("<Button-1>",more_config)
                
                l_less.bind("<Enter>",lambda e:change_config(l_less,less_ico1,580))
                l_less.bind("<Leave>",lambda e:reverse(l_less,less_ico,580))
                l_less.bind("<Button-1>",less_config)
                                
                # Binding options for all labels
                
                
                db_l.bind("<Enter>",lambda e: db_l.configure(bg="#3b3c36"))
                db_l.bind("<Button-1>",home_b)
                db_l.bind("<Leave>",lambda e: db_l.configure(bg="#333333"))
                
                memb_l.bind("<Enter>",lambda e: memb_l.configure(bg="#3b3c36"))
                memb_l.bind("<Button-1>",memb_b)
                memb_l.bind("<Leave>",lambda e: memb_l.configure(bg="#333333"))

                mb_l.bind("<Enter>",lambda e: mb_l.configure(bg="#3b3c36"))
                mb_l.bind("<Button-1>",m_book)
                mb_l.bind("<Leave>",lambda e: mb_l.configure(bg="#333333"))
                
                ms_l.bind("<Enter>",lambda e: ms_l.configure(bg="#3b3c36"))
                ms_l.bind("<Button-1>",m_student)
                ms_l.bind("<Leave>",lambda e: ms_l.configure(bg="#333333"))

                ib_l.bind("<Enter>",lambda e: ib_l.configure(bg="#3b3c36"))
                ib_l.bind("<Button-1>",i_b)
                ib_l.bind("<Leave>",lambda e: ib_l.configure(bg="#333333"))
                
                rb_l.bind("<Enter>",lambda e: rb_l.configure(bg="#3b3c36"))
                rb_l.bind("<Button-1>",r_b)
                rb_l.bind("<Leave>",lambda e: rb_l.configure(bg="#333333"))

                vr_l.bind("<Enter>",lambda e: vr_l.configure(bg="#3b3c36"))
                vr_l.bind("<Button-1>",v_record)
                vr_l.bind("<Leave>",lambda e: vr_l.configure(bg="#333333"))
                
                edit_l.bind("<Enter>",lambda e: edit_l.configure(bg="#3b3c36"))
                edit_l.bind("<Button-1>",edit)
                edit_l.bind("<Leave>",lambda e: edit_l.configure(bg="#333333"))
                
                logout_l.bind("<Enter>",lambda e: logout_l.configure(bg="#3b3c36"))
                logout_l.bind("<Button-1>",logout)
                logout_l.bind("<Leave>",lambda e: logout_l.configure(bg="#333333"))
                
                
                # Creating close button
                
                global close
                close=create_icon("exit2.png",25,25)
                close_ico=Button(main_win,image=close,bg="#696FF3",activebackground="#696FF3",command=main_win.destroy,bd=0,cursor="hand2")
                close_ico.place(x=1325,y=10)

                home_b(1)

            else:
                invalid_txt.configure(text="Invalid Password !")
                invalid.place(x=620,y=110)
                
        elif (uname_var.get=="" or uname_var.get()=="Enter Username...") or (passwd_var.get=="" or passwd_var.get=="Enter Password..."):
            invalid_txt.configure(text="Invalid Credentials !")
            invalid.place(x=620,y=110)
            w1.after(2000,lambda :invalid.place_forget())
        else:
            invalid_txt.configure(text="No account found !")
            invalid.place(x=620,y=110) # This is the location of error message
            w1.after(2000,lambda :invalid.place_forget())
    global l1,s1
    l1=Image.open(f".\\LoginIcons\\login_b.png")
    l1=l1.resize((230,45))
    l1=ImageTk.PhotoImage(l1)
    
    log_b=Button(w1,image=l1,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=log_check)
    log_b.place(x=600,y=350)

    # Signup Button

    # Signup Window :
    def f2():
        w1.destroy()
        w2=Tk()
        w2.configure(bg="#646FF9")
        w2.title("Admin")
        w2.resizable(False,False)
        center_screen.center_screen(900,680,w2)
        w2.overrideredirect(True)

        global Lib_bg
        Lib_bg=Image.open(".\\LoginIcons\\signup.png")
        Lib_bg=Lib_bg.resize((550,680),Image.ANTIALIAS)
        Lib_bg=ImageTk.PhotoImage(Lib_bg)
        Login_bg=Label(w2,image=Lib_bg,border=0)
        Login_bg.pack(side=LEFT)

        #Declaring string variables for 2 entry widgets
        uname_var=StringVar()
        passwd_var=StringVar()
        ques_var=StringVar()
        ans_var=StringVar()
        var=StringVar()
        
        uname_var.set("Enter Username...")
        passwd_var.set("Enter Password...")
        ques_var.set("Enter Question...")
        ans_var.set("Enter Answer...")
        var.set('n')
        
        # Welcome Message
        L1=Label(w2,text="Signup Page",bg="#646FF9",fg="white",font=("Louis George Cafe",15))
        L1.place(x=680,y=10)
        L2=Label(w2,text="Create new account here",bg="#646FF9",fg="white",font=("Louis George Cafe",12))
        L2.place(x=650,y=53)

        # Username
        L3=Label(w2,text="Username :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L3.place(x=617,y=125)
        e1=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=uname_var,fg="#343434")
        e1.place(x=620,y=165)
        line1=Frame(w2,height=2,width=215,bg="white")
        line1.place(x=620,y=190)

        # Password
        bullet=u"\u25CF"
        L4=Label(w2,text="Password :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L4.place(x=617,y=215)
        e2=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=passwd_var,fg="#343434")
        e2.place(x=620,y=255)
        line2=Frame(w2,height=2,width=215,bg="white")
        line2.place(x=620,y=280)

        # Security Question
        L5=Label(w2,text="Your Security Question :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L5.place(x=617,y=305)
        e3=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=ques_var,fg="#343434")
        e3.place(x=620,y=345)
        line3=Frame(w2,height=2,width=215,bg="white")
        line3.place(x=620,y=370)
    
        # Security Answer
        L6=Label(w2,text="Your Answer :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L6.place(x=617,y=395)
        e4=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=ans_var,fg="#343434")
        e4.place(x=620,y=435)
        line4=Frame(w2,height=2,width=215,bg="white")
        line4.place(x=620,y=460)

        # Admin Access
        global i1,i2
        def create_icon(x,y=30,z=30):
            ico=Image.open(f".\\bookIcons\\{x}")
            ico=ico.resize((y,z))
            return ImageTk.PhotoImage(ico)

        L7=Label(w2,text="Admin Controls :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L7.place(x=617,y=485)
    
        i1=create_icon("rb_on1.png",20,20)
        i2=create_icon("rb_of1.png",20,20)
        ls=Label(w2,text=' Yes',image=i2,compound="left",bg="#646FF9",fg="black",font=("Open Sans",10),state="normal")
        ls.place(x=620,y=527)
        ln=Label(w2,text=' No',image=i1,compound="left",bg="#646FF9",fg="black",font=("Open Sans",10),state="normal")
        ln.place(x=700,y=527)
        global access_value
        access_value=False
        def c_img(e):
            global access_value
            if access_value==1:
                ls.config(image=i1);ln.config(image=i2)
                var.set("y")
            else:
                note_txt=Label(w2,text="Note : Please close the popup window to continue...",bg='#646FF9',fg='silver',font=('Open Sans',9))
                note_txt.place(x=570,y=565)

                ### SUB Program for popup window ###
                popup=Toplevel()
                center_screen.center_screen(250,150,popup)
                
                # Creating a Frame
                p_f=Frame(popup,height=150,width=250,highlightbackground='black',highlightthickness=1,bg='silver')
                p_f.pack();p_f.pack_propagate(False)
                t_f=Frame(p_f,height=40,width=250,bg='#249794')
                t_f.pack()
                
                # String Variable
                adm_cd=StringVar()
                
                popup.focus();popup.grab_set()
                popup.overrideredirect(True)
                Label(t_f,text="System Message",bg='#249794',font=("Louis George Cafe",13),fg='white').place(x=40,y=12)
                Frame(t_f,width=400,height=1,bg='#249794').place(x=0,y=39)
                Label(popup,text="Enter access code     : ",bg='silver',font=('Louis George Cafe',11)).place(x=10,y=60)
                ad_cd=Entry(popup,font=("TimesNewRoman",10),width=10,bg="silver",fg="#343434",textvariable=adm_cd,border=0)
                Frame(popup,height=2,width=69,bg="white").place(x=170,y=88)
                ad_cd.place(x=170,y=65)

                # Hint Message
                hint=Label(popup,bg='silver',font=('Georgia',9),text='Hint :    4 digit code',fg='grey')
                
                # Error Message
                global inv1,succ1
                invalid=Frame(popup,bg="#E65151",bd=0,height=20,width=145)
                invalid.pack_propagate(False)
                disp_msg=Label(invalid,text="Invalid Credentials !",font=("Open Sans",9),bg="#E65151",fg="#FFCCCB")
                disp_msg.place(x=25,y=0)
                ico=Image.open(f".\\LoginIcons\\minor icons\\invalid.png")
                ico=ico.resize((13,13))
                inv1=ImageTk.PhotoImage(ico)
                ico=Image.open(f".\\LoginIcons\\minor icons\\succ.png")
                ico=ico.resize((13,13))
                succ1=ImageTk.PhotoImage(ico)
                inv_ico=Label(invalid,image=inv1,bg="#E65151")
                inv_ico.place(x=0,y=2)
                
                # Defining function call
                def check_cd(e):
                    global access_value
                    if adm_cd.get()=='1234':
                        hint.place_forget
                        inv_ico.configure(image=succ1,bg='#008040')
                        invalid.configure(bg='#008040')
                        disp_msg.configure(text="       Success !",bg='#008040',fg='white')
                        invalid.place(x=10,y=105)
                        popup.after(2000,lambda :popup.destroy())
                        access_value=1
                        note_txt.place_forget()
                        c_img(e)
                    else:
                        invalid.place(x=10,y=105)
                        popup.after(3000,lambda :invalid.place_forget())
                        hint.place(x=10,y=102)
                    
                # Buttons
                global conf,notify
                ico=Image.open(f".\\LoginIcons\\notify.png")
                ico=ico.resize((25,25))
                notify=ImageTk.PhotoImage(ico)
                ico=Image.open(f".\\LoginIcons\\conf.png")
                ico=ico.resize((75,25))
                conf=ImageTk.PhotoImage(ico)
                Label(t_f,image=notify,bg='#249794').place(x=6,y=9)
                conf_b=Label(p_f,image=conf,bg="silver",cursor='hand2')

                x=Label(t_f,text="x",font=('Louis George Cafe',18),bg='#249794',cursor='hand2',fg='white')
                x.place(x=225,y=6)
                conf_b.place(x=165,y=100)
                conf_b.bind('<Button-1>',check_cd)
                ad_cd.focus()
                # Post operation commands
                def exit_popup(e):
                    popup.destroy()
                    note_txt.place_forget()
                x.bind('<Button-1>',exit_popup)
        
        def c_img1(e):
            ln.config(image=i1);ls.config(image=i2)
            var.set('n')
        ls.bind("<Button-1>",c_img);
        ln.bind("<Button-1>",c_img1)
        #ls.unbind("<Button-1>");ln.unbind("<Button-1>")
                    
        # Binding options for help text
        def default_change1(e):
            if uname_var.get()=="Enter Username...":
                uname_var.set("")
        def default_change2(e):
            if passwd_var.get()=="Enter Password...":
                passwd_var.set("")
                e2.configure(show=bullet)
        def default_change3(e):
            if ques_var.get()=="Enter Question...":
                ques_var.set("")
        def default_change4(e):
            if ans_var.get()=="Enter Answer...":
                ans_var.set("")

        e1.bind("<Button-1>",default_change1)
        e1.bind("<FocusIn>",default_change1)

        e2.bind("<Button-1>",default_change2)
        e2.bind("<FocusIn>",default_change2)

        e3.bind("<Button-1>",default_change3)
        e3.bind("<FocusIn>",default_change3)

        e4.bind("<Button-1>",default_change4)
        e4.bind("<FocusIn>",default_change4)
    
        # Adding icons near entry widget
        global lock,passwd,ques,ans,access
    
        def create_icon(x,y=30,z=30):
            ico=Image.open(f".\\LoginIcons\\minor icons\\{x}")
            ico=ico.resize((y,z))
            return ImageTk.PhotoImage(ico)

        lock=create_icon("uname.png")
        lock_ico=Label(w2,image=lock,bg="#646FF9")
        lock_ico.place(x=580,y=165)

        passwd=create_icon("passwd.png")
        passwd_ico=Label(w2,image=passwd,bg="#646FF9")
        passwd_ico.place(x=580,y=255)

        ques=create_icon("sec_ques.png",25,25)
        ques_ico=Label(w2,image=ques,bg="#646FF9")
        ques_ico.place(x=583,y=345)
    
        ans=create_icon("ans.png",25,25)
        ans_ico=Label(w2,image=ans,bg="#646FF9")
        ans_ico.place(x=583,y=435)
                
        access=create_icon('sec_ques1.png',25,25)
        ques_ico=Label(w2,image=access,bg="#646FF9")
        ques_ico.place(x=583,y=525)
        
        # Back Button
        def f3():
            w2.destroy()
            f1()
            
        global l1,s1,s2
        l1=Image.open(f".\\LoginIcons\\arrow_icon1.png")
        l1=l1.resize((35,35))
        l1=ImageTk.PhotoImage(l1)
    
        back_b=Button(w2,image=l1,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=f3)
        back_b.place(x=575,y=605)
    
        # Signup Button
        
        # Declaring a Frame for displaying error message
        def close_invalid():
            invalid.place_forget()
        
        global inv,clear

        def create_icon(x,y=30,z=30):
            ico=Image.open(f".\\LoginIcons\\minor icons\\{x}")
            ico=ico.resize((y,z))
        
            return ImageTk.PhotoImage(ico)
    
        invalid=Frame(w2,bg="#E97451",bd=0,height=20,width=215)
        #invalid.place(x=635,y=87) # This is the location of error message

        invalid.pack_propagate(False)
        invalid_txt=Label(invalid,text="Invalid Credentials !",font=("Open Sans",9),bg="#E97451",fg="#FFCCCB")
        invalid_txt.place(x=25,y=0)
        inv=create_icon("invalid.png",13,13)
        inv_ico=Label(invalid,image=inv,bg="#E97451")
        inv_ico.place(x=0,y=2)

        global clear
        clear=create_icon("exit1.png",13,13)
        clear_ico=Button(invalid,image=clear,bg="#E97451",activebackground="#E97451",bd=0,cursor="hand2",command=close_invalid)
        clear_ico.place(x=195,y=2)
        
        cursor.execute("select * from admin")
        result=cursor.fetchall()
        l=[]
        for a in result:
            l+=[a[0]]
            
        # Creating function block as invoke command
        def sign_up():
            
            if uname_var.get() in l:
                invalid_txt.configure(text="Account already exists !")
                invalid.place(x=635,y=87)
                w2.after(3000,lambda :invalid.place_forget())
            elif (uname_var.get()=="" or uname_var.get()=="Enter Username...") or (passwd_var.get=="" or passwd_var.get()=="Enter Password...") or (ques_var.get()=="" or ques_var.get()=="Enter Question...") or (ans_var.get()=="" or ans_var.get()=="Enter Answer..."):
                invalid_txt.configure(text="Invalid Credentials !")
                invalid.place(x=635,y=87)
                w2.after(3000,lambda :invalid.place_forget())
                
            else:
                cursor.execute(f"insert into admin2 values ('{uname_var.get()}','{passwd_var.get()}','{ques_var.get()}','{ans_var.get()}','{var.get()}')")
                db.commit()
                messagebox.showinfo("Success","Account created successfully")
                
                uname_var.set("Enter Username...")
                e2.configure(show="")
                passwd_var.set("Enter Password...")
                ques_var.set("Enter Question...")
                ans_var.set("Enter Answer...")
        
            
        s1=Image.open(f".\\LoginIcons\\sign_b.png")
        s1=s1.resize((215,45))
        s1=ImageTk.PhotoImage(s1)
        s2=Image.open(f".\\LoginIcons\\sign_b1.png")
        s2=s2.resize((215,45))
        s2=ImageTk.PhotoImage(s2)
    
        sign_b=Button(w2,image=s2,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=sign_up)
        sign_b.place(x=620,y=600)
        #sign_b.bind('<Enter>',lambda e :sign_b.config(image=s1))
        #sign_b.bind('<Leave>',lambda e :sign_b.config(image=s2))

        # Binding Options for focus set
        e1.bind("<Return>",lambda e :e2.focus_set())
        e2.bind("<Return>",lambda e :e3.focus_set())
        e3.bind("<Return>",lambda e :e4.focus_set())
        e4.bind("<Return>",lambda e :sign_b.focus_set())

        # Creating close button
        global close
        close=create_icon("exit2.png",22,22)
        close_ico=Button(w2,image=close,bg="#646FF9",activebackground="#646FF9",command=w2.destroy,bd=0,cursor="hand2")
        close_ico.place(x=860,y=10)

    s1=Image.open(f".\\LoginIcons\\sign_b.png")
    s1=s1.resize((230,45))
    s1=ImageTk.PhotoImage(s1)
    
    sign_b=Button(w1,image=s1,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=f2)
    sign_b.place(x=600,y=410)

    # Forgot Password
    
    # Creating function block for invoking forgot pass win
    def forg_pass():
        w1.destroy()
        w2=Tk()
        w2.configure(bg="#646FF9")
        w2.title("Admin")
        w2.resizable(False,False)
        center_screen.center_screen(930,600,w2)
        w2.overrideredirect(True)

        global Lib_bg
        Lib_bg=Image.open(".\\LoginIcons\\idea.png")
        Lib_bg=Lib_bg.resize((550,600),Image.ANTIALIAS)
        Lib_bg=ImageTk.PhotoImage(Lib_bg)
        Login_bg=Label(w2,image=Lib_bg,border=0)
        Login_bg.pack(side=LEFT)

        #Declaring string variables for 2 entry widgets
        uname_var=StringVar()
        passwd_var=StringVar()
        ques_var=StringVar()
        ans_var=StringVar()
        
        uname_var.set("Enter Username...")
        passwd_var.set("Enter New Password...")
        ques_var.set("Question will appear here...")
        ans_var.set("Enter Answer...")
        
        # Welcome Message
        L1=Label(w2,text="Reset Password",bg="#646FF9",fg="white",font=("Louis George Cafe",15))
        L1.place(x=660,y=10)
        #L2=Label(w2,text="Input your username to search",bg="#646FF9",fg="white",font=("Louis George Cafe",12))
        #L2.place(x=650,y=53)

        # Declaring a Frame for displaying error message
        def close_invalid():
            invalid.place_forget()
            
        global inv,sch,clear
        def create_icon(x,y=30,z=30):
            ico=Image.open(f".\\LoginIcons\\minor icons\\{x}")
            ico=ico.resize((y,z))
            return ImageTk.PhotoImage(ico)
    
        invalid=Frame(w2,bg="#E97451",bd=0,height=20,width=225)
    
        invalid.pack_propagate(False)
        invalid_txt=Label(invalid,text="Username not found ",font=("Open Sans",9),bg="#E97451",fg="#FFCCCB")
        invalid_txt.place(x=25,y=0)
        inv=create_icon("invalid.png",13,13)
        inv_ico=Label(invalid,image=inv,bg="#E97451")
        inv_ico.place(x=0,y=2)

        global clear
        clear=create_icon("exit1.png",13,13)
        clear_ico=Button(invalid,image=clear,bg="#E97451",activebackground="#E97451",bd=0,cursor="hand2",command=close_invalid)
        clear_ico.place(x=205,y=2)

        ### Username - main code
        
        ## MYSQL QUERY
        cursor.execute("select * from admin")
        result=cursor.fetchall()
        uname_l=[]
        ques_l=[]
        ans_l=[]
        for a in result:
            uname_l+=[a[0]]
            ques_l+=[a[2]]
            ans_l+=[a[3]]
        data_id=0
        def u_sch():
            global data_id
            if uname_var.get() in uname_l:
                close_invalid()
                data_id=uname_l.index(uname_var.get())
                
                ques_var.set(ques_l[data_id])
                e3.configure(state="normal",cursor="xterm")
                e4.configure(state="normal",cursor="xterm")
                
            else:
                
                ques_var.set("Question will appear here...")
                e3.configure(state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")
                
                ans_var.set("Enter Answer...")
                e3.configure(state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")

                passwd_var.set("Enter New Password...")
                e4.configure(state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")

                invalid_txt.configure(text="Username not found")
                invalid.place(x=620,y=60)
                w2.after(2000,lambda :invalid.place_forget())
                
        L3=Label(w2,text="Username :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L3.place(x=617,y=105)
        e1=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=uname_var,fg="#343434")
        e1.place(x=620,y=145)
        line1=Frame(w2,height=2,width=215,bg="white")
        line1.place(x=620,y=170)

        sch=Image.open(f".\\LoginIcons\\minor icons\\sch3.png")
        sch=sch.resize((40,40))
        sch=ImageTk.PhotoImage(sch)
    
        search_b=Button(w2,image=sch,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=u_sch)
        search_b.place(x=840,y=135)
        
        # Security Question
        L4=Label(w2,text="Your Security Question :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L4.place(x=617,y=195)
        e2=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=ques_var,fg="#343434",state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")
        e2.place(x=620,y=235)
        line2=Frame(w2,height=2,width=215,bg="white")
        line2.place(x=620,y=260)
    
        # Security Answer
        L5=Label(w2,text="Your Answer :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L5.place(x=617,y=285)
        e3=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=ans_var,fg="#343434",state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")
        e3.place(x=620,y=325)
        line3=Frame(w2,height=2,width=215,bg="white")
        line3.place(x=620,y=350)

        # Password
        bullet=u"\u25CF"
        L6=Label(w2,text="New Password :",bg="#646FF9",fg="white",font=("TimesNewRoman",10))
        L6.place(x=617,y=375)
        e4=Entry(w2,font=("TimesNewRoman",9),width=30,bg="#646FF9",bd=0,textvariable=passwd_var,fg="#343434",state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")
        e4.place(x=620,y=415)
        line4=Frame(w2,height=2,width=215,bg="white")
        line4.place(x=620,y=440)
        
        # Binding options for help text
        def default_change1(e):
            if uname_var.get()=="Enter Username...":
                uname_var.set("")
                
        def default_change3(e):
            if e3["state"]=="disabled":
                pass
            elif ans_var.get()=="Enter Answer...":
                ans_var.set("")
                
        def default_change4(e):
            if e4["state"]=="disabled":
                pass
            elif passwd_var.get()=="Enter New Password...":
                passwd_var.set("")

        e1.bind("<Button-1>",default_change1)
        e1.bind("<FocusIn>",default_change1)

        e3.bind("<Button-1>",default_change3)
        e3.bind("<FocusIn>",default_change3)

        e4.bind("<Button-1>",default_change4)
        e4.bind("<FocusIn>",default_change4)
    
        # Adding icons near entry widget
        global lock,passwd,ques,ans
    
        def create_icon(x,y=30,z=30):
            ico=Image.open(f".\\LoginIcons\\minor icons\\{x}")
            ico=ico.resize((y,z))
            return ImageTk.PhotoImage(ico)

        lock=create_icon("uname.png")
        lock_ico=Label(w2,image=lock,bg="#646FF9")
        lock_ico.place(x=580,y=145)

        passwd=create_icon("passwd.png")
        passwd_ico=Label(w2,image=passwd,bg="#646FF9")
        passwd_ico.place(x=580,y=235)

        ques=create_icon("sec_ques.png",25,25)
        ques_ico=Label(w2,image=ques,bg="#646FF9")
        ques_ico.place(x=583,y=325)
    
        ans=create_icon("ans.png",25,25)
        ans_ico=Label(w2,image=ans,bg="#646FF9")
        ans_ico.place(x=583,y=415)

        # Back Button
        def f3():
            w2.destroy()
            f1()
            
        global b1,r1
        b1=Image.open(f".\\LoginIcons\\back.png")
        b1=b1.resize((230,45))
        b1=ImageTk.PhotoImage(b1)
    
        back_b=Button(w2,image=b1,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=f3)
        back_b.place(x=620,y=530)
    
        # Reset Button
        def reset_pass():
            data_id=0
            if uname_var.get() in uname_l:
                close_invalid()
                data_id=uname_l.index(uname_var.get())
            # print(data_id)
            crct_ans=ans_l[data_id]
            if ans_var.get()==crct_ans and (passwd_var.get()!="" and passwd_var.get()!="Enter New Password..."):
                close_invalid()
                cursor.execute(f"update admin set passwd='{passwd_var.get()}' where uname='{uname_var.get()}'")
                db.commit()
                messagebox.showinfo("Success","Password changed successfully")

                ques_var.set("Question will appear here...")
                e2.configure(state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")
                
                ans_var.set("Enter Answer...")
                e3.configure(state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")

                passwd_var.set("Enter New Password...")
                e4.configure(state="disabled",disabledbackground="#646FF9",disabledforeground="#9A9999",cursor="")
            else:
                if passwd_var.get()=="" and ans_var.get()=="tkinter@123":
                    invalid_txt.configure(text="Password can't be empty")
                
                elif passwd_var.get()=="Enter New Password..." and ans_var.get()=="tkinter@123":
                    invalid_txt.configure(text="Password can't be empty")
                else:
                    invalid_txt.configure(text="Invalid Answer")
                invalid.place(x=620,y=60)
                w2.after(2000,lambda :invalid.place_forget())
                
        r1=Image.open(f".\\LoginIcons\\reset.png")
        r1=r1.resize((230,45))
        r1=ImageTk.PhotoImage(r1)
    
        reset_b=Button(w2,image=r1,border="0",bg="#646FF9",cursor="hand2",activebackground="#646FF9",command=reset_pass)
        reset_b.place(x=620,y=480)

        # Binding Options for focus set
        e2.bind("<Return>",lambda e :e3.focus_set())
        e3.bind("<Return>",lambda e :e4.focus_set())
        e4.bind("<Return>",lambda e :reset_b.focus_set())

        # Creating close button
        global close
        close=create_icon("exit2.png",20,20)
        close_ico=Button(w2,image=close,bg="#646FF9",activebackground="#646FF9",command=w2.destroy,bd=0,cursor="hand2")
        close_ico.place(x=900,y=10)
                                    ##### Function block ends here #####
    global f_p
    f_p=create_icon("f_pass.png")
    pass_b=Button(w1,text="Forgot Password ?",image=f_p,compound="left",bg="#646FF9",font=("Segoe UI",9),activebackground="#646FF9",cursor="hand2",fg="white",border=0,activeforeground="white",command=forg_pass)
    pass_b.place(x=660,y=480)

    # Binding Options for focus set
    e1.bind("<Return>",lambda e :e2.focus_set())
    e2.bind("<Return>",lambda e :log_b.focus_set())

    # Creating close button
    global close
    close=create_icon("exit2.png",25,25)
    close_ico=Button(w1,image=close,bg="#646FF9",activebackground="#646FF9",command=w1.destroy,bd=0,cursor="hand2")
    close_ico.place(x=860,y=10)
        
f1()
