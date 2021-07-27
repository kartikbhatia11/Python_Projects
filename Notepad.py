from tkinter import *
from tkinter import filedialog
import os
import sys

root=Tk()
root.title('Untitled - Kitaab')
root.geometry('500x500')
root.iconbitmap('D:\icons8-task-64.ico')


# Creating MenuBar

MenuBar=Menu(root)
root.config(menu=MenuBar)

# Defining New file funtion

def New():
    root.title('Untitled - Kitaab')
    text.delete(1.0,END)


# Defining New Window Function

def New_Window():
    pass

        
# Defining Open function

def Open():
    global file
    file=filedialog.askopenfilename(defaultextension='.txt')

    if file=='':
        pass
    else:
        global text
        root.title(os.path.basename(file.rstrip('.txt')) + ' - Kitaab')
        t=open(file,'r').read()
        text.delete(1.0,END)
        text.insert(END,t)
    print(file)


# defining Save Function

def Save():
    global text
    if root.title()=='Untitled - Kitaab':
        file_name=filedialog.asksaveasfile(defaultextension='.txt')

        if file_name=='':
            pass
        else:
            t=open(file_name.name,'w')
            t.write(text.get(1.0,END))
            t.close()

            root.title(os.path.basename(file.name).replace('.txt','') + ' - Kitaab')

    else:
        t=open(file,'w')
        t.write(text.get(1.0,END))
        t.close()

# Defining Save_as Function

def Save_as():
    file=filedialog.asksaveasfile(defaultextension='.txt')

    if file=='':
        pass
    else:
        t=open(file.name,'w')
        t.write(text.get(1.0,END))
        t.close()

        root.title(os.path.basename(file.name).replace('.txt','') + ' - Kitaab')
    

# Creating SubMenu1

SubMenu1=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label='File',menu=SubMenu1)
SubMenu1.add_command(label='New',command=New,accelerator="Ctrl+N")
SubMenu1.add_command(label='New Window',command=New_Window,state=DISABLED)
SubMenu1.add_command(label='Open',command=Open)
SubMenu1.add_command(label='Save',command=Save)
SubMenu1.add_command(label='Save As...',command=Save_as)
SubMenu1.add_command(label='Page Setup',state=DISABLED)
SubMenu1.add_command(label='Print...',state=DISABLED)
SubMenu1.add_command(label='Exit',command=root.destroy)



def Undo():
    global text
    text.event_generate('<<Undo>>')


def Cut():
    global text
    text.event_generate('<<Cut>>')


def Copy():
    global text
    text.event_generate('<<Copy>>')


def Paste():
    global text
    text.event_generate('<<Paste>>')


def Delete():
    global text
    text.event_generate('<<Delete>>')
    

# Creating SubMenu2

SubMenu2=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label='Edit',menu=SubMenu2)
SubMenu2.add_command(label='Undo',command=Undo,state=DISABLED)
SubMenu2.add_command(label='Cut',command=Cut)
SubMenu2.add_command(label='Copy',command=Copy)
SubMenu2.add_command(label='Paste',command=Paste)
SubMenu2.add_command(label='Delete',state=DISABLED)
SubMenu2.add_command(label='Search with Bing...',state=DISABLED)
SubMenu2.add_command(label='Find',state=DISABLED)
SubMenu2.add_command(label='Find Next',state=DISABLED)
SubMenu2.add_command(label='Find Previous',state=DISABLED)
SubMenu2.add_command(label='Replace',state=DISABLED)
SubMenu2.add_command(label='Go To...',state=DISABLED)
SubMenu2.add_command(label='Select All',state=DISABLED)
SubMenu2.add_command(label='Date/Time',state=DISABLED)

# Creating SubMenu3

SubMenu3=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label='Format',menu=SubMenu3,state=DISABLED)
SubMenu3.add_command(label='Word Wrap')
SubMenu3.add_command(label='Font...')

# Creating SubMenu4

SubMenu4=Menu(MenuBar,tearoff=0)
k=MenuBar.add_cascade(label='View',menu=SubMenu4,state=DISABLED)
SubMenu=Menu(k,tearoff=0)
SubMenu4.add_cascade(label='Zoom',menu=SubMenu,state=DISABLED)
SubMenu.add_command(label='Zoom in')
SubMenu.add_command(label='Zoom out')
SubMenu.add_command(label='Restore Default Zoom')
SubMenu4.add_command(label='Status Bar')

# Creating SubMenu5

SubMenu5=Menu(MenuBar,tearoff=0)
MenuBar.add_cascade(label='Help',menu=SubMenu5,state=DISABLED)
SubMenu5.add_command(label='View Help')
SubMenu5.add_command(label='Send Feedback')
SubMenu5.add_command(label='About Us')


text=Text(root,font='Arial 16')
text.pack(fill=BOTH,expand=True)

scrollv=Scrollbar(text,bg='white',width=16)
scrollv.pack(side='right',fill='y')

scrollh=Scrollbar(text,orient=HORIZONTAL,bg='white',width=16)
scrollh.pack(side='bottom',fill='x')
