from tkinter import *
import webbrowser

class MyApp:
    def __init__(self, parent):
        self.myParent = parent
        self.myContainer1 = LabelFrame(parent, text="HULK Engine")
        self.myContainer2 = Frame(parent)
        self.myContainer1.grid()
        self.myContainer2.grid()
        

        self.label1 = Message(self.myContainer1, text="")
        
        self.label1.pack()

        self.entryVariable = StringVar()
        self.textbox = Entry(self.myContainer1)
        self.textbox.pack(side=TOP)
        self.textbox.bind("<Return>",self.submitclick)
        self.textbox.focus_set()

        self.label2 = Label(self.myContainer1)
        self.label2["text"] =""
        self.label2.pack(side=BOTTOM)

        self.label3 = Message(self.myContainer1, text="")
        self.label3.pack()
        

        self.button1 = Button(self.myContainer2)
        self.button1["text"]= "Go"
        self.button1.pack(side=BOTTOM)
        self.button1.bind("<Button-1>", self.submitclick)
        textbox=self.textbox

        self.button2 = Button(self.myContainer2)
        self.button2["text"] = "Mail"
        self.button2.pack(side=BOTTOM)
        self.button2.bind("<Button-1>", self.getmail)

        
    def submitclick(self, event):

        browser_path = '/usr/bin/firefox %s'
        textin = self.textbox.get()
        webbrowser.get(browser_path).open("http://www.google.ca/search?q="+textin)
        
        self.myParent.destroy()
        
    def getmail(self, event):
        browser_path = '/usr/bin/firefox %s'
        webbrowser.get(browser_path).open("https://login.live.com")
        self.myParent.destroy()



root = Tk()
myapp = MyApp(root)
root.title('Search')
root.mainloop()