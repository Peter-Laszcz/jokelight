import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from winsound import *
import sys
LARGEFONT = ("Verdana", 35)

global userid
global faces
global tags
bool = False
class tkinterApp(tk.Tk):


    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, signed_in, program_options, about, history):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage

class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='white')
        startbutton = Image.open("getstarted1.png")
        welcomeimg = Image.open("starwelcome1.png")


        wimg = welcomeimg.resize((360, 60))
        loadwimg = ImageTk.PhotoImage(wimg)
        img = startbutton.resize((240, 30))
        loadimage = ImageTk.PhotoImage(img)
        # label of frame Layout 2

        label = tk.Label(self, image = loadwimg, border = '0')
        label.image = loadwimg
        label.place(relx=0.5, rely=0.4, anchor='center')
        # putting the grid in its place by using
        # grid
        #label.grid(row=0, column=4, padx=10, pady=10)



        button1 = tk.Button(self, image = loadimage, bg = 'white', border ='0', cursor = 'hand2',
                             command=lambda: [controller.show_frame(Page1)])
        button1.image = loadimage
        button1.place(relx=0.5, rely=0.5, anchor='center')

        openofflight = Image.open("offbulb.jpg")

        resizeofflight = openofflight.resize((450, 530))

        loadofflight = ImageTk.PhotoImage(resizeofflight)


        lightlabel = tk.Label(self, image=loadofflight, bg='white', border='0')
        lightlabel.image = loadofflight
        lightlabel.place(relx=0.5, rely=0.5, anchor='center')
        lightlabel.lower()

        # putting the button in its place by
        # using grid
        #button1.grid(row=1, column=1, padx=10, pady=10)






# second window frame page1
class Page1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='white')
        enterimg = Image.open("enter.png")
        signinimg = Image.open("signin.png")
        eimg = enterimg.resize((270, 50))
        simg = signinimg.resize((250, 50))
        loadenter = ImageTk.PhotoImage(eimg)
        loadsignin = ImageTk.PhotoImage(simg)

        label = tk.Label(self, image=loadenter, bg='white', border='0')
        label.image = loadenter
        label.place(relx=0.5, rely=0.32, anchor='center')

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Skip",
                             command=lambda: controller.show_frame(signed_in))


        # putting the button in its place
        # by using grid
        button1.grid(row=1, column=1, padx=10, pady=10)
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self, show="*")
        self.e1.place(relx=0.5, rely=0.4, anchor='center')
        self.e2.place(relx=0.5, rely=0.48, anchor='center')



        signbutton = tk.Button(self, image=loadsignin, command=lambda:self.login_clicked(controller), bg='white', border ='0', cursor = 'hand2')
        signbutton.image = loadsignin
        signbutton.place(relx=0.5, rely=0.58, anchor='center')

        createimg = Image.open("create.png")
        cimg = createimg.resize((160, 25))
        loadcreate = ImageTk.PhotoImage(cimg)
        createlabel = tk.Label(self, image = loadcreate, bg = 'white', border = '0')
        createlabel.image = loadcreate
        createlabel.place(relx=0.5, rely=0.65, anchor='center')

    def login_clicked(self, controller):
        username = self.e1.get()
        password = self.e2.get()
        if username == "hacker":
            PlaySound('LBT.wav', SND_FILENAME)
        if username == "admin" and password == "homunculus":
            userid = username
            controller.show_frame(signed_in)

        else:
            messagebox.showerror("Error", "Incorrect username or password")




class signed_in(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='white')
        openmenu = Image.open("jokemenu1.png")
        openhistory = Image.open("history3.png")
        openrunprog = Image.open("program3.png")
        resizemenu = openmenu.resize((400, 65))
        resizehistory = openhistory.resize((300, 40))
        resizerunprog = openrunprog.resize((300, 40))
        loadmenu = ImageTk.PhotoImage(resizemenu)
        loadhistory = ImageTk.PhotoImage(resizehistory)
        loadrunprog = ImageTk.PhotoImage(resizerunprog)

        openlight = Image.open("bulb.jpg")
        resizelight = openlight.resize((450,530))
        loadlight = ImageTk.PhotoImage(resizelight)
        lightlabel = tk.Label(self, image = loadlight, bg='white', border='0')
        lightlabel.image = loadlight
        lightlabel.place(relx=0.5, rely=0.5, anchor='center')
        lightlabel.lower()

        menulabel = tk.Label(self, image = loadmenu, bg = 'white', border = '0')
        menulabel.image = loadmenu
        menulabel.place(relx=0.5, rely=0.4, anchor='center')

        historybutton = tk.Button(self, image=loadhistory, command = lambda : controller.show_frame(history),bg = 'white', border = '0', cursor = 'hand2')
        historybutton.image = loadhistory
        historybutton.place(relx=0.5, rely=0.65, anchor='center')

        runprogbutton = tk.Button(self,image=loadrunprog, command = lambda : controller.show_frame(program_options), bg = 'white', border = '0', cursor = 'hand2')
        runprogbutton.image = loadrunprog
        runprogbutton.place(relx=0.5, rely=0.75, anchor='center')

        openabout = Image.open("about.png")
        resizeabout = openabout.resize((300, 40))
        loadabout = ImageTk.PhotoImage(resizeabout)
        aboutlabel = tk.Button(self, image=loadabout, command = lambda : controller.show_frame(about), bg='white', border='0', cursor='hand2')
        aboutlabel.image = loadabout
        aboutlabel.image = loadabout
        aboutlabel.place(relx=0.5, rely=0.55, anchor='center')

        opensignout = Image.open("signout.png")
        resizesignout = opensignout.resize((170, 45))
        loadsignout = ImageTk.PhotoImage(resizesignout)
        signoutbutton = tk.Button(self, image=loadsignout, command=lambda: controller.show_frame(StartPage), bg='white',
                                  border='0', cursor='hand2')
        signoutbutton.image = loadsignout
        signoutbutton.place(relx=0.19, rely=0.94, anchor='center')

class program_options(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='white')
        openoptions = Image.open("options3.png")
        opentags = Image.open("tags.png")
        openfaces = Image.open("faces.png")
        openrun = Image.open("run.png")
        resizeoptions = openoptions.resize((130, 50))
        resizetags = opentags.resize((70, 25))
        resizefaces = openfaces.resize((45, 20))
        resizerun = openrun.resize((120, 40))
        loadoptions = ImageTk.PhotoImage(resizeoptions)
        loadtags = ImageTk.PhotoImage(resizetags)
        loadfaces = ImageTk.PhotoImage(resizefaces)
        loadrun = ImageTk.PhotoImage(resizerun)

        optionslabel = tk.Label(self, image = loadoptions, bg = 'white', border = '0')
        optionslabel.image = loadoptions
        #optionslabel.place(relx=0.5, rely=0.3, anchor='center')

        tick1 = tk.Checkbutton(self, image = loadtags, bg = 'white', border = '0', cursor = 'hand2')
        tick1.image = loadtags
        tick1.place(relx=0.38, rely=0.48, anchor='w')
        tick2 = tk.Checkbutton(self, image = loadfaces, bg = 'white', border = '0', cursor = 'hand2')
        tick2.image = loadfaces
        tick2.place(relx=0.38, rely=0.53, anchor='w')
        openbox = Image.open("rectangle2.png")
        resizebox = openbox.resize((150, 70))
        loadbox = ImageTk.PhotoImage(resizebox)
        boxlabel = tk.Label(self, image = loadbox, bg = 'white', border = '0')
        boxlabel.image = loadbox
        boxlabel.place(relx=0.5, rely=0.51, anchor='center')
        boxlabel.lower()

        opencloud = Image.open("cloud4.png")
        resizecloud = opencloud.resize((500, 450))
        loadcloud = ImageTk.PhotoImage(resizecloud)
        cloudlabel = tk.Label(self, image = loadcloud, bg = 'white', border = '0')
        cloudlabel.image = loadcloud
        cloudlabel.place(relx=0.51, rely=0.37, anchor='center')
        cloudlabel.lower()

        runlabel = tk.Label(self, image = loadrun, bg = 'white', border = '0', cursor = 'hand2')
        runlabel.image = loadrun
        runlabel.place(relx=0.5, rely=0.64, anchor='center')

        openback = Image.open("back.png")
        resizeback = openback.resize((70, 30))
        loadback = ImageTk.PhotoImage(resizeback)
        backbutton = tk.Button(self, image=loadback, command=lambda: controller.show_frame(signed_in), bg='white',
                               border='0', cursor='hand2')
        backbutton.image = loadback
        backbutton.place(relx=0.5, rely=0.95, anchor='center')



class about(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='white')

        openabout = Image.open("aboutcontent.png")
        resizeabout = openabout.resize((500, 500))
        loadabout = ImageTk.PhotoImage(resizeabout)
        aboutlabel = tk.Label(self, image = loadabout, bg = 'white', border = '0')
        aboutlabel.image = loadabout
        aboutlabel.place(relx=0.5, rely=0.47, anchor='center')

        openback = Image.open("back.png")
        resizeback = openback.resize((70, 30))
        loadback = ImageTk.PhotoImage(resizeback)
        backbutton = tk.Button(self, image = loadback, command = lambda : controller.show_frame(signed_in), bg = 'white', border = '0', cursor = 'hand2')
        backbutton.image = loadback
        backbutton.place(relx=0.5, rely=0.95, anchor='center')

class history(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, background='white')

        openhistorypage = Image.open("historypage.png")
        resizehistory = openhistorypage.resize((500, 500))
        loadhistory = ImageTk.PhotoImage(resizehistory)
        historylabel = tk.Label(self, image = loadhistory, bg = 'white', border = '0')
        historylabel.image = loadhistory
        historylabel.place(relx=0.5, rely=0.52, anchor='center')
        openback = Image.open("back.png")
        resizeback = openback.resize((70, 30))
        loadback = ImageTk.PhotoImage(resizeback)
        backbutton = tk.Button(self, image = loadback, command = lambda : controller.show_frame(signed_in), bg = 'white', border = '0', cursor = 'hand2')
        backbutton.image = loadback
        backbutton.place(relx=0.5, rely=0.95, anchor='center')

# Driver Code
app = tkinterApp()
app.geometry("500x500")
app.configure(background='white')
icon1 = Image.open("icon.png")
img = ImageTk.PhotoImage(icon1)
app.title("Joke Light")
app.iconbitmap(default="icon.ico")


app.mainloop()
