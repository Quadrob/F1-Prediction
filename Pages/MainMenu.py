import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import Pages.Settings as settings

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        menubg = Image.open("./Assests/menu.jpg")
        self.menubgImage = ImageTk.PhotoImage(menubg.copy().resize((settings.WIDTH, settings.HEIGHT)))

        self.menuCanvas = ctk.CTkCanvas(self, width= settings.WIDTH, height= settings.HEIGHT, bd=0, highlightthickness=0)
        self.menuCanvas.create_image( 0, 0, image = self.menubgImage, anchor = "nw")
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Predict Driver", width=360, height=50, border_width=0, corner_radius=10, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverPage"))
        buttonQuit.place(x=70, y=130)
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Predict Constructor", width=360, height=50, border_width=0, corner_radius=10, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("ConstructorPage"))
        buttonQuit.place(x=70, y=200)
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Best Driver Team Pairing", width=360, height=50, border_width=0, corner_radius=10, bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, command=lambda: controller.show_frame("DriverTeamPairingPage"))
        buttonQuit.place(x=70, y=270)
        
        buttonQuit = ctk.CTkButton(self.menuCanvas, text="Quit", width=360, height=50, border_width=0, corner_radius=10, fg_color="#d90000", bg_color="#132236", text_font=('Calibri', 16, 'bold'), hover=True, hover_color="#820903", command=lambda: controller.exitApp())
        buttonQuit.place(x=70, y=400)
        
        self.menuCanvas.create_text(settings.WIDTH/2, 30, text="F1 Predict Menu", fill="#d90000", font=('Calibri 32 bold'))
        self.menuCanvas.create_text(settings.WIDTH/4, 590, text=settings.APPDETAILS, fill="#d90000", font=('Calibri 11 bold'))
        self.menuCanvas.pack(side="top", fill = "both", expand = True)
