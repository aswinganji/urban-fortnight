#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Name : ")
print("We will be learning how to create a application on juipter which has GUI elements and how to manuipulate the output as per the values selected from the GUI components")


# # Code for GUI compenents and manuipulating the output

# In[1]:


from tkinter import Tk,filedialog
from ipywidgets import widgets
from IPython.display import display,clear_output
import pandas as pd
import matplotlib.pyplot as plt

graph_type = ['Cukodoo....','line','bar']
df = ''
headtail = ['head','tail']
number300 = ['5','10','20','30']

def select_files(b):
    clear_output()
    global graph_type
    global df
    root = Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename()
    df = pd.read_csv(file_name)
    print(file_name)
    
    xlabel_widget = widgets.Dropdown(options = df.columns)
    ylabel_widget = widgets.Dropdown(options = df.columns)
    graph_widgets = widgets.Dropdown(options = graph_type)
    
    head_tail = widgets.Dropdown(options = headtail)
    number = widgets.Dropdown(options = number300)
    
    graph = widgets.interactive(display_plot,xaxis = xlabel_widget,yaxis = ylabel_widget)
    
    display(graph)
    
fileselect = widgets.Button(description = "File Select")
fileselect.on_click(select_files)

display(fileselect)

def display_plot(xaxis,yaxis,graph_type):
    global df
    if(graph_type == 'line'):
        plt.subplots(figsize = (19,8))
        plt.plot(df[xaxis],df[yaxis],linewidth = 3.0)
        plt.xlabel(xaxis)
        plt.ylabel(yaxis)
        plt.show()
        
    elif(graph_type == 'bar'):
        plt.subplots(figsize = (19,8))
        plt.bar(df[xaxis],df[yaxis],color = ['red','yellow','green','blue','black'])
        plt.xlabel(xaxis)
        plt.xticks(rotation = 'vertical')
        plt.ylabel(yaxis)
        plt.show()
    else:
        print("Choose Valid Option")


# In[ ]:




