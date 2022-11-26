import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import Pages.Settings as settings
import DB.dataPreperation as data


class DriverTeamPairingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        pairingMenubg = Image.open("./Assests/pairingMenu.jpg")
        self.pairingMenubgImage = ImageTk.PhotoImage(pairingMenubg.copy().resize((settings.WIDTH, settings.HEIGHT)))

        self.pairingMenuCanvas= ctk.CTkCanvas(self, width= settings.WIDTH, height= settings.HEIGHT, bd=0, highlightthickness=0)
        self.pairingMenuCanvas.create_image( 0, 0, image = self.pairingMenubgImage, anchor = "nw")        
        
        driverButton = ctk.CTkButton(self.pairingMenuCanvas, text="Best Team for a Driver", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverPage"))
        driverButton.place(x=70, y=130)
        
        teamButton = ctk.CTkButton(self.pairingMenuCanvas, text="Best Driver for a Team", width=360, height=50, border_width=0, corner_radius=2, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorPage"))
        teamButton.place(x=70, y=200)
        
        mainMenuButton = ctk.CTkButton(self.pairingMenuCanvas, text="Main Menu", width=360, height=50, border_width=0, corner_radius=2, fg_color="#d90000", bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, hover_color="#820903", command=lambda: controller.show_frame("MenuPage"))
        mainMenuButton.place(x=70, y=400)
        
        self.pairingMenuCanvas.create_text(settings.WIDTH/2, 30, text="F1 Driver & Team Pairing", fill="#d90000", font=('Calibri 32 bold'))
        self.pairingMenuCanvas.create_text(settings.WIDTH/4, 590, text=settings.APPDETAILS, fill="#d90000", font=('Calibri 11 bold'))
        self.pairingMenuCanvas.pack(side="top", fill = "both", expand = True)
