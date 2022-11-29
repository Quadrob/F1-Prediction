import DB.Database as Database
import DB.dataPreperation as data
import pandas as pd
import numpy as np
import tkinter as tk
import customtkinter as ctk
from tkinter import font as tkfont 
from PIL import Image, ImageTk
import Pages.Settings as settings
from Pages.MainMenu import MenuPage
from Pages.DriverMenu import DriverPage
from Pages.ConstructorMenu import ConstructorPage
from Pages.PairingMenu import DriverTeamPairingPage
from Pages.DriverPredict import *
from Pages.ConstructorPredict import *
from Pages.PairingPredict import *
from threading import Thread


def splashLoader():    
    # Get the prepared dataframe to perform predictions with
    print("Loading...")
    settings.FINALDATAFRAME = data.dataPreperation()
    settings.CIRCUITCOUNTRYDICT = data.getAllCircuitsAndCountry()
    data.dataframeLogger(settings.FINALDATAFRAME)


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)        
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry(str(settings.WIDTH) + "x" + str(settings.HEIGHT))
        settings.centerWindow(self, settings.WIDTH, settings.HEIGHT)
        self.title("F1 Predict Beta")
        self.iconbitmap("./Assests/F1-logo.ico")
        self.config(bg="#2b2a2a")
        self.resizable(False,False)
        self.withdraw()

        # Create the splash screen
        splashThread = Thread(target=splashLoader, daemon=True)
        splashThread.start()
        splash = ctk.CTkToplevel(self)
        splash.geometry("300x500")
        splash.overrideredirect(True)
        settings.centerWindow(splash, 300, 500)
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
        
        for Frame in (MenuPage, DriverPage, ConstructorPage, DriverTeamPairingPage, 
                      DriverQualifying, DriverRace, DriverChampionship, ConstructorQualifying, 
                      ConstructorRace, ConstructorChampionship, ConstructorPairing, DriverPairing):
            page_name = Frame.__name__
            frame = Frame(parent=container, controller=self)
            self.frames[page_name] = frame
            if 'MenuPage' in str(Frame):
                self.show_frame("MenuPage")

        self.show_frame("MenuPage") 

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def exitApp(self):
        self.destroy()


if __name__ == "__main__":
    # Set global configurations
    pd.set_option('max_columns', None)
    np.set_printoptions(precision=5)
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = App()
    app.mainloop()
    
    # Close db connections
    Database.disconnectFromDatabase()
