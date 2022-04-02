from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import win32api
import win32print

root = Tk()
root.title('technicalankit! Textpad')
root.geometry("1200x680")

# set variable for open file namre
global open_status_name
open_status_name = False

#set the variable of selected texy
global selected
selected = False

#create A new file function
def new_file():
    my_text.delete("1.0", END)
    # Update status bar
    root.title('New File -Textpad!')
    status_bar.config(text="New File     ")

    global open_status_name
    open_status_name = False

# Open New file
def open_file():
    #delete previous text
    my_text.delete("1.0", END)

    #grab filename
    text_file= filedialog.askopenfilename(title = "Open a file",filetypes=(("Text Files","*.txt"),("HTML","*.html"),("All files","*.*")))
    # Check to see therei s a file name
    if text_file:
        # glocal the file name
        global open_status_name
        open_status_name = text_file
    # Update SStatus Bar
    name = text_file
    status_bar.config(text=name)
    root.title(f'{name}-Textpad!')

    # Open the file
    text_file = open(text_file,'r')
    stuff = text_file.read()

    # Writing The text
    my_text.insert(END,stuff)

    # close the open file
    text_file.close()

# save as file
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",title="save File",filetypes=(("Text Files","*.txt"),("HTML","*.html"),("All files","*.*")))
    if text_file:
        # Update status bars
        name = text_file
        root.title(f'{name}-Textpad!')
        status_bar.config(text=name)

        #save the file
        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0,END))
        #close the file
        text_file.close()

#save file
def save_file():
    global open_status_name
    if open_status_name:
        #save the file
        text_file = open(open_status_name,'w')
        text_file.write(my_text.get(1.0,END))
        #close the file
        text_file.close()
        root.title(f'{open_status_name}-Textpad!')
        status_bar.config(text=open_status_name)
    else:
        save_as_file()

# Cut text
def cut_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Grab selected text
            selected = my_text.selection_get()
            #Deleting sekected text
            my_text.delete("sel.first","sel.last")
            # Clear Cipboard 
            root.clipboard_clear()
            root.clipboard_append(selected)

# Copy text
def copy_text(e):
    global selected
    # check to see that whweatther see keybioard shotcut
    if e:
        selected = root.clipboard_get()
    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)

# paste text
def paste_text(e):
    global selected
    # Keyboard shortcut
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position,selected)
# Bold Text
def bold_it():
    bold_font = font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight = "bold")

    # Configure a tag
    my_text.tag_configure("bold",font=bold_font)

    # Current tags
    current_tags = my_text.tag_names("sel.first")
    # If statement tag has benn used
    if "bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
        my_text.tag_add("bold","sel.first","sel.last")
# Italic Text
def Italics_it():
    italics_font = font.Font(my_text,my_text.cget("font"))
    italics_font.configure(slant="italic")

    # Configure a tag
    my_text.tag_configure("italic",font=italics_font)

    # Current tags
    current_tags = my_text.tag_names("sel.first")
    # If statement tag has benn used
    if "italic" in current_tags:
        my_text.tag_remove("italic","sel.first","sel.last")
    else:
        my_text.tag_add("italic","sel.first","sel.last")
# Change Selected Text color
def text_color():
    #Pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        #status_bar.config(text=my_color)

        color_font = font.Font(my_text,my_text.cget("font"))

        # Configure a tag
        my_text.tag_configure("colored",font=color_font,foreground=my_color)

        # Current tags
        current_tags = my_text.tag_names("sel.first")
        # If statement tag has benn used
        if "colored" in current_tags:
            my_text.tag_remove("colored","sel.first","sel.last")
        else:
            my_text.tag_add("colored","sel.first","sel.last")

# Change Bg color
def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)

# Change All text color
def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(foreground=my_color)
# Print file
def file_print():
    printer_name = win32print.GetDefaultPrinter()
    status_bar.config(text=printer_name)
    # Grab the file
    file_to_print = filedialog.askopenfilename(defaultextension=".*",title="save File",filetypes=(("Text Files","*.txt"),("HTML","*.html"),("All files","*.*")))

    if file_to_print:
        win32api.ShellExecute(0,"print",file_to_print,None,".",0)

#Create tool bar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)
#Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)


#Create our scrollbar for the textbox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

# Create our Horizontal Scroll Bar
hor_scroll = Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)

#Create Text Box
my_text = Text(my_frame,width=97,height=25,font=("Helvetica",16),selectbackground = "yellow",selectforeground = "black",undo = True,yscrollcommand = text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()


#configure our scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

#create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add file menu
file_menu  = Menu(my_menu,tearoff = False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label = "New",command=new_file)
file_menu.add_command(label = "Open",command=open_file)
file_menu.add_command(label = "Save",command=save_file)
file_menu.add_command(label = "Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label = "Print File",command=file_print)
file_menu.add_separator()
file_menu.add_command(label = "Exit",command=root.quit)

# Add Edit menu
edit_menu  = Menu(my_menu,tearoff = False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label = "Cut",command=lambda:cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label = "Copy",command=lambda:copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label = "Paste",command=lambda:paste_text(False),accelerator="(Ctrl+v)")
edit_menu.add_separator()
edit_menu.add_command(label = "Undo",command=my_text.edit_undo,accelerator="(Ctrl+z)")
edit_menu.add_command(label = "Redo",command=my_text.edit_redo, accelerator="(Ctrl+y)")

# Add color menu
color_menu  = Menu(my_menu,tearoff = False)
my_menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label = "Selected Text",command=text_color)
color_menu.add_command(label = "All Text",command=all_text_color)
color_menu.add_command(label = "BackGround",command=bg_color)

# Add status bar at bottom
status_bar = Label(root,text='Ready   ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=15)

# Edit Bindings
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)

# Create Button

# Bold Button
bold_button = Button(toolbar_frame,text="Bold",command=bold_it)
bold_button.grid(row=0 , column=0,sticky=W,padx=5)
#Italics Button
Italics_button = Button(toolbar_frame,text="Italics",command=Italics_it)
Italics_button.grid(row=0 , column=1,padx=5)

#Undo redo buttons
undo_button = Button(toolbar_frame,text="Undo",command=my_text.edit_undo)
undo_button.grid(row=0 , column=2,padx=5)
redo_button = Button(toolbar_frame,text="Redo",command=my_text.edit_redo)
redo_button.grid(row=0 , column=3,padx=5)

# Text Color
color_text_button = Button(toolbar_frame,text="Text Color",command=text_color)
color_text_button.grid(row=0,column=4,padx=5)




root.mainloop()