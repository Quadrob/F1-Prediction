import DB.Database as Database
import DB.dataPreperation as data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import customtkinter as ctk
import tkinter.ttk as ttk
from tkinter import font as tkfont 
from PIL import Image, ImageTk
import time
import io
from regression import *
from classification import *
from dateutil.relativedelta import *
from sklearn.preprocessing import StandardScaler
from threading import Thread

# Global Variables
appDetails = "© 2022 Copyright. All Rights Reserved.\tCreated by: Robert Zeelie.\tVersion: 0.0.1"
finalDataframe = pd.DataFrame()
WIDTH, HEIGHT = 1100, 600


def splashLoader():    
    # Get the prepared dataframe to perform predictions with
    global finalDataframe 
    # finalDataframe = data.dataPreperation()
    # data.dataframeLogger(finalDataframe)


def centerWindow(window: tk.Tk, width, height):
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    x = w / 2 - width / 2
    y = h / 2 - height / 2
    window.geometry("%dx%d+%d+%d" % ((width, height) + (x, y)))


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry(str(WIDTH) + "x" + str(HEIGHT))
        centerWindow(self, WIDTH, HEIGHT)
        self.title("F1 Predict Beta")
        self.iconbitmap("./Assests/F1-logo.ico")
        self.resizable(False,False)
        self.withdraw()

        # Create the splash screen
        splashThread = Thread(target=splashLoader, daemon=True)
        splashThread.start()
        splash = ctk.CTkToplevel(self)
        splash.geometry("300x500")
        splash.overrideredirect(True)
        centerWindow(splash, 300, 500)
        bg = Image.open("./Assests/splash.png")
        bgImage = ImageTk.PhotoImage(bg.copy().resize((300, 500)))
        splashLabel = ctk.CTkLabel(splash, image=bgImage)
        splashLabel.pack(fill='both', expand=True)

        while splashThread.is_alive():
            self.update()

        splash.destroy()
        
        # Show the main window
        self.deiconify()
        self.focus_force()
        
        # the container is where we'll stack a bunch of frames on top of each other, then the one we want visible will be raised above the others
        container = ctk.CTkFrame(self, bg_color="#132236")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        
        for Frame in (MenuPage, DriverPage, ConstructorPage):
            page_name = Frame.__name__
            frame = Frame(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def exitApp(self):
        self.destroy()


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        menubg = Image.open("./Assests/menu.jpg")
        self.menubgImage = ImageTk.PhotoImage(menubg.copy().resize((WIDTH, HEIGHT)))

        self.menuCanvas= ctk.CTkCanvas(self, width= WIDTH, height= HEIGHT, bd=0, highlightthickness=0)
        self.menuCanvas.create_image( 0, 0, image = self.menubgImage, anchor = "nw")
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Predict Driver", width=360, height=50, border_width=0, corner_radius=10, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverPage"))
        buttonQuit.place(x=70, y=150)
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Predict Constructor", width=360, height=50, border_width=0, corner_radius=10, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorPage"))
        buttonQuit.place(x=70, y=230)
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Quit", width=360, height=50, border_width=0, corner_radius=10, fg_color="#d90000", bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, hover_color="#820903", command=lambda: controller.exitApp())
        buttonQuit.place(x=70, y=390)
        
        self.menuCanvas.create_text(WIDTH/2, 30, text="F1 Predict Menu", fill="#d90000", font=('Calibri 32 bold'))
        self.menuCanvas.create_text(WIDTH/4, 590, text=appDetails, fill="#d90000", font=('Calibri 11 bold'))
        self.menuCanvas.pack(side="top", fill = "both", expand = True)


class DriverPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        driverMenubg = Image.open("./Assests/driverMenu.jpg")
        self.driverMenubgImage = ImageTk.PhotoImage(driverMenubg.copy().resize((WIDTH, HEIGHT)))

        self.driverMenuCanvas= ctk.CTkCanvas(self, width= WIDTH, height= HEIGHT, bd=0, highlightthickness=0)
        self.driverMenuCanvas.create_image( 0, 0, image = self.driverMenubgImage, anchor = "nw")
        
        qualifyingButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Qualification", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorPage"))
        qualifyingButton.place(x=70, y=130)
        
        raceButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Race", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorPage"))
        raceButton.place(x=70, y=200)

        championshipButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Driver Championship", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorPage"))
        championshipButton.place(x=70, y=270)
        
        mainMenuButton = ctk.CTkButton(self.driverMenuCanvas, text="Main Menu", width=360, height=50, border_width=0, corner_radius=2, fg_color="#d90000", bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, hover_color="#820903", command=lambda: controller.show_frame("MenuPage"))
        mainMenuButton.place(x=70, y=400)
        
        self.driverMenuCanvas.create_text(WIDTH/2, 30, text="F1 Predict Drivers Menu", fill="#d90000", font=('Calibri 32 bold'))
        self.driverMenuCanvas.create_text(WIDTH/4, 590, text=appDetails, fill="#d90000", font=('Calibri 11 bold'))
        self.driverMenuCanvas.pack(side="top", fill = "both", expand = True)

        
class ConstructorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        driverMenubg = Image.open("./Assests/constructorMenu.jpg")
        self.driverMenubgImage = ImageTk.PhotoImage(driverMenubg.copy().resize((WIDTH, HEIGHT)))

        self.driverMenuCanvas= ctk.CTkCanvas(self, width= WIDTH, height= HEIGHT, bd=0, highlightthickness=0)
        self.driverMenuCanvas.create_image( 0, 0, image = self.driverMenubgImage, anchor = "nw")
        
        qualifyingButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Qualification", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverPage"))
        qualifyingButton.place(x=70, y=130)
        
        raceButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Race", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverPage"))
        raceButton.place(x=70, y=200)

        championshipButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Constructor Championship", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverPage"))
        championshipButton.place(x=70, y=270)
        
        mainMenuButton = ctk.CTkButton(self.driverMenuCanvas, text="Main Menu", width=360, height=50, border_width=0, corner_radius=2, fg_color="#d90000", bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, hover_color="#820903", command=lambda: controller.show_frame("MenuPage"))
        mainMenuButton.place(x=70, y=400)
        
        self.driverMenuCanvas.create_text(WIDTH/2, 30, text="F1 Predict Constructor Menu", fill="#d90000", font=('Calibri 32 bold'))
        self.driverMenuCanvas.create_text(WIDTH/4, 590, text=appDetails, fill="#d90000", font=('Calibri 11 bold'))
        self.driverMenuCanvas.pack(side="top", fill = "both", expand = True)
        

if __name__ == "__main__":
    # Set global configurations
    Database.connectToDatabase()
    pd.set_option('max_columns', None)
    np.set_printoptions(precision=5)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()
    
    # Close db connections
    Database.disconnectFromDatabase()
