# Import this program to add pie chart to your output

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def pie_chart(master,labels=["Label1","Label2","Label3"],values=[1,1,1],place_x=0,place_y=0,explode=(0,0,0),shadow=False,startangle=90,l_title="Title",size=(3,3),colors=( "orange", "cyan", "brown","grey", "indigo", "beige"),title="Title"):
    figure = Figure(figsize=size,dpi=100,facecolor="#EDE7E7")
    subplot = figure.subplots()
    wedges=subplot.pie(values, colors = colors,wedgeprops={ 'linewidth' : 1, 'edgecolor' : "#696969" }, explode=explode, autopct='%1.1f%%', shadow=shadow, startangle=startangle,labeldistance=1.2) 
    subplot.axis('scaled')
    subplot.set_title(title)
    

    leg=subplot.legend(title=l_title,bbox_to_anchor=(1,1),facecolor="#EDE7E7",labels=labels)
    for a in leg.get_texts():
        a.set_color("#696969")
        
    
    return figure
    
    #pie = FigureCanvasTkAgg(figure, master)
    #pie.get_tk_widget().place(x=-150+place_x,y=0+place_y)

#pie_chart(root,size=(6,3.5),place_x=0,place_y=0,shadow=True,explode=(0,0.1,0.1,0,0,0,0,0,0),title="Books in each category",labels=[1,2,3,4,5,6,7,8,9],values=[1,1,1,1,1,1,1,2,2])
