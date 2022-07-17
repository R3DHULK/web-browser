import webbrowser
from tkinter import *
from tkinter import ttk


def search_term():
    
    if(var2.get()==1):
        webbrowser.open("https://www.google.com/search?q="+Term.get(),new=2)
    if(var3.get()==1):
        webbrowser.open("https://www.youtube.com/results?search_query="+Term.get(),new=2)
    if(var4.get()==1):
        webbrowser.open("https://www.imdb.com/find?ref_=nv_sr_fn&q="+Term.get()+"&s=all",new=2)

root=Tk()
root.resizable(False, False)
root.title("HULK will search")  


Term = StringVar(root, value="")
Term_entry=ttk.Entry(root,textvariable=Term,width=50)
Term_entry.grid(row=0, column=1,padx=10, pady=10,sticky=W+E)
Term_entry.focus()

submit_button = ttk.Button(root,text="Submit",command=search_term)
submit_button.grid(row=0, column=2,padx=9, sticky=W+E)

check=Frame(root).grid(row=0,column=0,columnspan=3)

var2 = IntVar(root,value=0)
Checkbutton(check, text="Google", variable=var2).grid(row=0,column=4)

var3 = IntVar(root,value=0)
Checkbutton(check, text="Youtube", variable=var3).grid(row=0,column=5)

var4 = IntVar(root,value=0)
Checkbutton(check, text="IMDB", variable=var4).grid(row=0,column=6,padx=(0,30))

Term_entry.bind("<Return>", (lambda event: search_term()))

root.mainloop()