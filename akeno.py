from tkinter.ttk import *
from tkinter import *
from map import *
from pics import *
from lahing import*


class Kaart(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master=None,bg="black")
        self.bind_all("<Key>",self.press)
        self.pack()
        self.createwidgets()
        self.refmap()

    def press(self,e):
        key = e.keysym

        if key == "Left" or key=="a":
            self.left()
        elif key == "Right" or key=="d":
            self.right()
        elif key == "Up" or key=="w":
            self.up()
        elif key == "Down" or key=="s":
            self.down()
        elif key == "Escape":
            self.quit()

    def refmap(self):
        self.Kaart=out()
        for row in range(11):
            for element in range(11):
                if "K" in self.Kaart[row][element]:
                    self.photoall=self.kaardil.index(self.Kaart[row][element].strip("K"))
                    self.Kaart[row][element]=Label(self,bg="black",image=self.photokangelane).grid(column=element,row=row,sticky=(N,S,W,E))
                else:
                    i=self.kaardil.index(self.Kaart[row][element])
                    self.Kaart[row][element]=Label(self,bg="black",image=self.kaardil[i+1]).grid(column=element,row=row,sticky=(N,S,W,E))

    def createwidgets(self):

        self.photokangelane=PhotoImage(file=get_pic(hero.gender))#TO CHANGE
        self.kaardil=["T",PhotoImage(file=get_pic("T")),"B",PhotoImage(file=get_pic("B")),"H",PhotoImage(file=get_pic("H")),"M",PhotoImage(file=get_pic("M")),"#",PhotoImage(file=get_pic("#")),".",PhotoImage(file=get_pic("."))]
        self.photoblank=PhotoImage(file=get_pic(" "))
        self.photor=PhotoImage(file=get_pic("R"))
        self.photoq=PhotoImage(file=get_pic("Q"))
        self.photol=PhotoImage(file=get_pic("L"))
        self.photou=PhotoImage(file=get_pic("U"))
        self.photod=PhotoImage(file=get_pic("D"))
        self.photohe=PhotoImage(file=get_pic(str(hero.pot)))
        self.photoat=PhotoImage(file=get_pic("a"))
        self.photode=PhotoImage(file=get_pic("d"))
        self.photowep=PhotoImage(file=get_pic(hero.W.name))
        self.photoarm=PhotoImage(file=get_pic(hero.A.name))
        style=Style()
        style.configure("SD",background="black")
        self.Name=Label(self,bg="black",fg="Red",text=hero.name).grid(column=11,row=0,columnspan=3,sticky=(N,S,W,E))
        self.wep=Label(self,bg="black",image=self.photowep).grid(column=11,row=6,sticky=(N,S,W,E))
        self.arm=Label(self,bg="black",image=self.photoarm).grid(column=11,row=5,sticky=(N,S,W,E))
        self.wepinf=Label(self,bg="black",fg="red",text=hero.W.name+"\n damage- "+str(hero.W.mindam)+"-"+str(hero.W.maxdam)+"\n"+"critical chance:- "+str(hero.W.crit)).grid(column=12,row=6,columnspan=2,sticky=(N,S,W,E))
        self.arminf=Label(self,bg="black",fg="red",text=hero.A.name+"\n defence- "+str(hero.A.defence)).grid(column=12,row=5,columnspan=2,sticky=(N,S,W,E))
        self.blank1=Label(self,bg="black",image=self.photoblank).grid(column=11,row=10,sticky=(N,S,W,E))
        self.blank2=Label(self,bg="black",image=self.photoblank).grid(column=11,row=8,sticky=(N,S,W,E))
        self.blank3=Label(self,bg="black",image=self.photoblank).grid(column=13,row=8,sticky=(N,S,W,E))
        self.Right=Button(self,bg="black",image=self.photor,relief=FLAT,command=self.right,width=50,height=50).grid(column=13,row=9,sticky=(N,S,W,E))
        self.Quit=Button(self,bg="black",relief=FLAT,image=self.photoq, command=self.quit,width=50,height=50).grid(column=13,row=10,sticky=(N,S,W,E))
        self.Left=Button(self,bg="black",relief=FLAT,image=self.photol,command=self.left,width=50,height=50).grid(column=11,row=9,sticky=(N,S,W,E))
        self.Up=Button(self,bg="black",relief=FLAT,image=self.photou,command=self.up,width=50,height=50).grid(column=12,row=8,sticky=(N,S,W,E))
        self.Down=Button(self,bg="black",relief=FLAT,image=self.photod,command=self.down,width=50,height=50).grid(column=12,row=10,sticky=(N,S,W,E))
        self.Defend=Button(self,bg="black",relief=FLAT,image=self.photode,command=self.defend).grid(column=12,row=7,sticky=(N,S,W,E))
        self.Attack=Button(self,bg="black",relief=FLAT,image=self.photoat,command=self.attack).grid(column=11,row=7,sticky=(N,S,W,E))
        self.Heal=Button(self,bg="black",relief=FLAT,image=self.photohe,command=self.heal).grid(column=13,row=7,sticky=(N,S,W,E))
        self.elud=Label(self,bg="black",fg="red",text=(hero.hp,"/100")).grid(row=1,column=11,sticky=(N,W,S,E))
        self.eludebar=Progressbar(self,value=hero.hp).grid(row=1,column=12,columnspan=2,sticky=(N,W,S,E))
    def up(self):
        UP()
        self.refmap()
    def down(self):
        DOWN()
        self.refmap()
    def right(self):
        RIGHT()
        self.refmap()
    def left(self):
        LEFT()
        self.refmap()
    def attack(self):
        print("ATTACK")
    def defend(self):
        print("DEFEND")
    def heal(self):
        print("HEAL")
    def press(self,e):
        key = e.keysym

        if key == "Left" or key=="a":
            self.left()
        elif key == "Right" or key=="d":
            self.right()
        elif key == "Up" or key=="w":
            self.up()
        elif key == "Down" or key=="s": 
            self.down()
        elif key == "Escape":
            self.quit()
    def update(self):
        self.refmap()
class Tiitel(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master=None,bg="black")
        self.bind_all("<Key>",self.press)
        self.pack()
        self.ok=False
        self.createwidgets()
    def createwidgets(self):
        self.nimekast=Label(self,text="Name:",fg="red",bg="black").grid(column=0,row=0)
        self.nimi=StringVar()
        Entry(self,textvariable=self.nimi,fg="red",bg="black").grid(column=1,row=0)
        self.sex=StringVar()
        Radiobutton(self,text="F",variable=self.sex,value="f",fg="red",bg="black").grid(column=0,row=1)
        Radiobutton(self,text="M",variable=self.sex,value="m",fg="red",bg="black").grid(column=1,row=1)
        self.mapnr=StringVar()
        Radiobutton(self,text="Map nr. 1",variable=self.mapnr,value="map1.txt",fg="red",bg="black").grid(column=0,row=2)
        Radiobutton(self,text="Map nr. 2",variable=self.mapnr,value="map2.txt",fg="red",bg="black").grid(column=1,row=2)
        self.cont=Button(self,text="CONTINUE",command=self.check,fg="red",bg="black").grid(column=0,row=3)
    def press(self,e):
        key = e.keysym
        if key=="Return":
            self.check()
    def check(self):
        if self.sex.get()!="" and self.mapnr.get()!="":
            global hero
            loo_kaart(self.mapnr.get())
            hero=char(self.nimi.get(),self.sex.get())
            self.quit()

        
root=Tk()
root.title("Something Dungeon")
aken1=Tiitel(root)
aken1.mainloop()
aken1.destroy()
aken2=Kaart(root)
aken2.mainloop()
root.destroy()
