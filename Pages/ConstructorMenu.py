import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import Pages.Settings as settings

class ConstructorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        driverMenubg = Image.open("./Assests/constructorMenu.jpg")
        self.driverMenubgImage = ImageTk.PhotoImage(driverMenubg.copy().resize((settings.WIDTH, settings.HEIGHT)))

        self.driverMenuCanvas= ctk.CTkCanvas(self, width= settings.WIDTH, height= settings.HEIGHT, bd=0, highlightthickness=0)
        self.driverMenuCanvas.create_image( 0, 0, image = self.driverMenubgImage, anchor = "nw")
        
        qualifyingButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Qualification", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorQualifying"))
        qualifyingButton.place(x=70, y=130)
        
        raceButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Race", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorRace"))
        raceButton.place(x=70, y=200)

        championshipButton = ctk.CTkButton(self.driverMenuCanvas, text="Predict Constructor Championship", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorChampionship"))
        championshipButton.place(x=70, y=270)
        
        mainMenuButton = ctk.CTkButton(self.driverMenuCanvas, text="Main Menu", width=360, height=50, border_width=0, corner_radius=2, fg_color="#d90000", bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, hover_color="#820903", command=lambda: controller.show_frame("MenuPage"))
        mainMenuButton.place(x=70, y=400)
        
        self.driverMenuCanvas.create_text(settings.WIDTH/2, 30, text="F1 Predict Constructor Menu", fill="#d90000", font=('Calibri 32 bold'))
        self.driverMenuCanvas.create_text(settings.WIDTH/4, 590, text=settings.APPDETAILS, fill="#d90000", font=('Calibri 11 bold'))
        self.driverMenuCanvas.pack(side="top", fill = "both", expand = True)

    