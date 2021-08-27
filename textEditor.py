import tkinter as tk
from tkinter import Event, ttk
from tkinter import colorchooser,filedialog,messagebox,font
import os
from tkinter.constants import FALSE

main_application = tk.Tk()
main_application.geometry("1200x800")
main_application.title("Text Editor")
main_application.wm_iconbitmap('icon.ico')

# *********************main menu************************
# --------------------end main menu---------------------
main_menu = tk.Menu()

# File::::::
new_icon = tk.PhotoImage(file="icons2/new.png")
open_icon = tk.PhotoImage(file="icons2/open.png")
save_icon = tk.PhotoImage(file="icons2/save.png")
saveas_icon = tk.PhotoImage(file="icons2/save_as.png")
exit_icon = tk.PhotoImage(file="icons2/exit.png")

file_menu = tk.Menu(main_menu,tearoff=0)

# EDIT------------->>>>>
copy_icon = tk.PhotoImage(file="icons2/copy.png")
paste_icon = tk.PhotoImage(file="icons2/paste.png")
cut_icon = tk.PhotoImage(file="icons2/cut.png")
clear_all_icon = tk.PhotoImage(file="icons2/clear_all.png")
find_icon = tk.PhotoImage(file="icons2/find.png")

edit_menu = tk.Menu(main_menu,tearoff=0)


# VIEW---------------->>>>>>>>>>>>
tool_icon = tk.PhotoImage(file="icons2/tool_bar.png")
status_icon = tk.PhotoImage(file="icons2/status_bar.png")

view_menu = tk.Menu(main_menu,tearoff=0)


# COLOR-THEME------------------------->>>>
color1_icon = tk.PhotoImage(file="icons2/light_default.png")
color2_icon = tk.PhotoImage(file="icons2/light_plus.png")
color3_icon = tk.PhotoImage(file="icons2/dark.png")
color4_icon = tk.PhotoImage(file="icons2/monokai.png")
color5_icon = tk.PhotoImage(file="icons2/night_blue.png")
color6_icon = tk.PhotoImage(file="icons2/red.png")

colortheme_menu = tk.Menu(main_menu,tearoff=0)

color_choice = tk.StringVar()
color_icons = (color1_icon,color2_icon,color3_icon,color4_icon,color5_icon,color6_icon)

color_dict ={
    "Light Default" : ("#000000","#ffffff"),
    "Light Plus" : ("#474747","#e0e0e0"),
    "Dark" : ("#c4c4c4","#2d2d2d"),
    "Monokai" : ("#d3b774","#474747"),
    "Night Blue" : ("#ededed","#6b9dc2"),
    "Red" : ("#2d2d2d","#ffe8e8")
}
# cascade-------------------->>>>>>>>>>
main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_cascade(label="View",menu=view_menu)
main_menu.add_cascade(label="Color Theme",menu=colortheme_menu)


# ******************************************tool bar*********************************************
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font box :::
font_tuples =tk.font.families()
font_family = tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state="read only")
font_box["values"] = font_tuples
font_box.current(font_tuples.index("Arial"))
font_box.grid(row=0,column=0,padx=5)

# size box :::
size_var = tk.IntVar()
size_box=ttk.Combobox(tool_bar,width=30,textvariable=size_var,state="read only")
size_box["values"] = tuple(range(8,80,2))
size_box.current(1)
size_box.grid(row=0,column=1,padx=5)

# Buttons :::
bold_icon = tk.PhotoImage(file="icons2/bold.png")
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_icon = tk.PhotoImage(file="icons2/italic.png")
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

underline_icon = tk.PhotoImage(file="icons2/underline.png")
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

fontcolor_icon = tk.PhotoImage(file="icons2/font_color.png")
fontcolor_btn = ttk.Button(tool_bar,image=fontcolor_icon)
fontcolor_btn.grid(row=0,column=5,padx=5)

left_icon = tk.PhotoImage(file="icons2/align_left.png")
left_btn = ttk.Button(tool_bar,image=left_icon)
left_btn.grid(row=0,column=6,padx=5)

center_icon = tk.PhotoImage(file="icons2/align_center.png")
center_btn = ttk.Button(tool_bar,image=center_icon)
center_btn.grid(row=0,column=7,padx=5)

right_icon = tk.PhotoImage(file="icons2/align_right.png")
right_btn = ttk.Button(tool_bar,image=right_icon)
right_btn.grid(row=0,column=8,padx=5)

# ----------------------------------------------end tool bar--------------------------------------------


# ********************************************text editor******************************************
text_editor = tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


# font family and font size functionality:
current_font_family = "Arial"
current_font_size = 10

def font_change(main_application):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def fontsize_change(main_application):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",font_change)
size_box.bind("<<ComboboxSelected>>",fontsize_change)

# Bold Button Functionality::

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))
    
bold_btn.configure(command=change_bold)

def change_italic():
    italic_property = tk.font.Font(font=text_editor['font'])
    if italic_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if italic_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

italic_btn.configure(command=change_italic)

def change_underline():
    underline_property = tk.font.Font(font=text_editor['font'])
    if underline_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if underline_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)

def change_fontcolor():
    color_property = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_property[1])

fontcolor_btn.configure(command=change_fontcolor)


def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config("left",justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

left_btn.configure(command=align_left)

def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config("center",justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

center_btn.configure(command=align_center)

def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config("right",justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

right_btn.configure(command=align_right)


text_editor.configure(font=("Arial",10))
# -----------------------------------------end text editor--------------------------------------------


# *********************************************status bar**********************************************
status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def statusbar(event=None):
    global text_changed
    if text_editor.edit_modified():
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c').replace(" ",""))
        status_bar.config(text=f"Characters : {characters} Words : {words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",statusbar)

# --------------------end status bar ---------------------


# *********************main menu functionality************************

# File menu>>>>>>>>>>>

# VARIABLE :::
url =''

# NEW FUNCTIONALITY::::
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

file_menu.add_command(label="New",image=new_icon,compound=tk.LEFT,accelerator="Ctrl + N",command=new_file)

# OPEN FUNCTIONALITY:::::
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(("Text File","*.txt"),("All Types","*.*")))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file_menu.add_command(label="Open",image=open_icon,compound=tk.LEFT,accelerator="Ctrl + O",command=open_file)


# SAVE FUNCTIONALITY:::::

def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,"w",encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w',defaultextension="*.txt",filetypes=(("Text File","*.txt"),("All Types","*.*")))
            content2= text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

file_menu.add_command(label="Save",image=save_icon,compound=tk.LEFT,accelerator="Ctrl + S",command=save_file)

# SAVE AS functionality:::
def save_as(event=None):
    global url
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode='w',defaultextension="*.txt",filetypes=(("Text File","*.txt"),("All Types","*.*")))
        url.write(content)
        url.close()
    except:
        return

file_menu.add_command(label="Save As",image=saveas_icon,compound=tk.LEFT,accelerator="Ctrl + Alt + S",command=save_as)


# EXIT FUNCTIONALITY:::
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox= messagebox.askyesnocancel("Warning!","Do you want to save the file?")
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding="utf-8") as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode='w',defaultextension="*.txt",filetypes=(("Text File","*.txt"),("All Types","*.*")))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()        
        else:
            main_application.destroy()
    except:
        return

file_menu.add_command(label="Exit",image=exit_icon,compound=tk.LEFT,accelerator="Ctrl + Q",command=exit_func)


# Edit Menu>>>>>>

# COPY::
edit_menu.add_command(label = "Copy",image=copy_icon,compound=tk.LEFT,accelerator="Ctrl + C",command=lambda:text_editor.event_generate("<Control c>"))

# PASTE::
edit_menu.add_command(label = "Paste",image=paste_icon,compound=tk.LEFT,accelerator="Ctrl + V",command=lambda:text_editor.event_generate("<Control v>"))

# CUT::
edit_menu.add_command(label = "Cut",image=cut_icon,compound=tk.LEFT,accelerator="Ctrl + X",command=lambda:text_editor.event_generate("<Control x>"))

# CLEAR ALL::
edit_menu.add_command(label = "Clear All",image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl + Alt+ X",command=lambda:text_editor.delete(1.0,tk.END))

# FIND::

# Find Functionality::
def find_func(event=None):

    def find():
        word = find_box.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = find_box.get()
        replace_text = replace_box.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    find_dialog = tk.Toplevel()
    find_dialog.geometry("350x150+500+200")
    find_dialog.title("Find")
    find_dialog.resizable(0,0)

    # frame::
    find_frame = ttk.LabelFrame(find_dialog,text="Find/Replace")
    find_frame.pack(pady=20)

    # label::
    text_find = ttk.Label(find_frame,text="Find: ")
    text_replace = ttk.Label(find_frame,text="Replace: ")

    # entry box::
    find_box = ttk.Entry(find_frame,width =30)
    replace_box = ttk.Entry(find_frame,width =30)

    # button::
    find_btn = ttk.Button(find_frame,text="Find",command=find)
    replace_btn = ttk.Button(find_frame,text="Replace",command=replace)

    # label grid::
    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace.grid(row=1,column=0,padx=4,pady=4)

    # entry grid::
    find_box.grid(row=0,column=1,padx=4,pady=4)
    replace_box.grid(row=1,column=1,padx=4,pady=4)

    # button grid:::
    find_btn.grid(row=2,column=0,padx=4,pady=4)
    replace_btn.grid(row=2,column=1,padx=4,pady=4)

    find_dialog.mainloop()

edit_menu.add_command(label = "Find",image=find_icon,compound=tk.LEFT,accelerator="Ctrl + F",command=find_func)


# View Menu>>>>>>>>>>

show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if status_bar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view_menu.add_checkbutton(label="Tool Bar",onvalue=True,offvalue=0,variable=show_toolbar,image=tool_icon,compound=tk.LEFT,command=hide_toolbar)

view_menu.add_checkbutton(label="Status Bar",onvalue=1,offvalue=False,variable=show_statusbar,image=status_icon,compound=tk.LEFT,command=hide_statusbar)


# Color Theme Menu>>>>>>>>>>>

def color_theme():
    theme_chosen = color_choice.get()
    color_icons = color_dict.get(theme_chosen)
    fg_color,bg_color = color_icons[0],color_icons[1]
    text_editor.config(background=bg_color,foreground=fg_color)

count = 0
for i in color_dict:
    colortheme_menu.add_radiobutton(label=i,image=color_icons[count],variable=color_choice,compound=tk.LEFT,command=color_theme)
    count+=1

# --------------------end main menu functionality---------------------

main_application.config(menu=main_menu)

# Bind Shortcut Key::::::
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)
main_application.mainloop()