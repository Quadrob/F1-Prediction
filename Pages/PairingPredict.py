import tkinter as tk
import customtkinter as ctk
import Pages.Settings as settings
import DB.dataPreperation as data
import ML.predict as predict
import queue
from threading import Thread
import pandas as pd


resultsElements = []

def leavePage(controller):
    for element in resultsElements:
        try:
            element.destroy()
        except:
            print()
        
    controller.show_frame("DriverTeamPairingPage")


def updateVar(canvas, sliderVal, var, label, labelMessage):
    var.set(sliderVal)
    label.configure(text=labelMessage + str(var.get()))
    canvas.update_idletasks()


def submitDriver(canvas, driverVar):
    for element in resultsElements:
        try:
            element.destroy()
        except:
            print()
    loadingLabel = ctk.CTkLabel(canvas, text="Loading...", bg_color='#035b99', text_font=('Calibri', 16, 'bold'))
    loadingLabel.place(x=680, y=250)
    canvas.update_idletasks()
    q = queue.Queue()
    driver = driverVar.get() if driverVar.get() else 'None'
    
    if (driver != 'None'):
        Thread(target=predict.predictDriverPairing(q), daemon=True).start()
        results = q.get()
        results = pd.DataFrame(results)
        raceResults = results[(results['driver'] == str(driver))]
        loadingLabel.destroy()

        headingLabel = ctk.CTkLabel(canvas, text="Results of Predicted Driver / Constructor Combination:", fg_color='#035b99', text_font=('Calibri', 24, 'bold'))
        headingLabel.place(x=510, y=70)
        driverLabel = ctk.CTkLabel(canvas, text=("Driver: " + str(driver)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        driverLabel.place(x=450, y=180)
        predictLabel = ctk.CTkLabel(canvas, text=("Predicted Constructor: " + str(raceResults['predicted'].values[0])), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        predictLabel.place(x=450, y=300)
        resultsElements.extend([headingLabel, driverLabel, predictLabel])
        driverVar.set(None)
    else:
        loadingLabel.destroy()
        invalidLabel = ctk.CTkLabel(canvas, text="Please select a value from the dropdown?", bg_color='#d90000', text_font=('Calibri', 16, 'bold'))
        invalidLabel.place(x=570, y=250)
        canvas.update_idletasks()
        invalidLabel.after(3000, invalidLabel.destroy())


def submitChampionship(canvas, driverVar, seasonVar, pointsVar, winsVar):
    for element in resultsElements:
        try:
            element.destroy()
        except:
            print()
    loadingLabel = ctk.CTkLabel(canvas, text="Loading...", bg_color='#035b99', text_font=('Calibri', 16, 'bold'))
    loadingLabel.place(x=680, y=250)
    canvas.update_idletasks()
    q = queue.Queue()
    season = seasonVar.get() if seasonVar.get() else 'None'
    driver = driverVar.get() if driverVar.get() else 'None'
    points = pointsVar.get() if pointsVar.get() else 'None'
    wins = winsVar.get() if winsVar.get() else 'None'
    
    if (driver != 'None' and season != 'None' and points != 'None' and wins != 'None'):
        Thread(target=predict.predictDriverChampion(q, driver, season, points, wins), daemon=True).start()
        results = q.get()
        results = pd.DataFrame(results)
        raceResults = results[(results['driver'] == str(driver))]
        loadingLabel.destroy()

        headingLabel = ctk.CTkLabel(canvas, text="Results of Predicted Championship:", fg_color='#035b99', text_font=('Calibri', 24, 'bold'))
        headingLabel.place(x=510, y=70)
        seasonLabel = ctk.CTkLabel(canvas, text=("Season: " + str(season)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        seasonLabel.place(x=450, y=140)
        driverLabel = ctk.CTkLabel(canvas, text=("Driver: " + str(driver)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        driverLabel.place(x=450, y=180)
        pointsLabel = ctk.CTkLabel(canvas, text=("Points: " + str(points)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        pointsLabel.place(x=450, y=220)
        winsLabel = ctk.CTkLabel(canvas, text=("Wins: " + str(wins)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        winsLabel.place(x=450, y=260)        
        predictLabel = ctk.CTkLabel(canvas, text=("Predicted Championship Postion: " + str(raceResults['predicted'].values[0])), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        predictLabel.place(x=450, y=300)
        resultsElements.extend([headingLabel, seasonLabel, driverLabel, pointsLabel, winsLabel, predictLabel])
        seasonVar.set(None)
        driverVar.set(None)
    else:
        loadingLabel.destroy()
        invalidLabel = ctk.CTkLabel(canvas, text="Please select a value from the dropdown?", bg_color='#d90000', text_font=('Calibri', 16, 'bold'))
        invalidLabel.place(x=570, y=250)
        canvas.update_idletasks()
        invalidLabel.after(3000, invalidLabel.destroy())


class DriverPairing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.raceCanvas= ctk.CTkCanvas(self, width= settings.WIDTH, height= settings.HEIGHT, bd=0, highlightthickness=0)
        self.raceCanvas.configure(bg="#2b2a2a")
        
        driverVar = ctk.StringVar(value="None")
        driverOptions = data.getCurrentDrivers()
        driverLabel = ctk.CTkLabel(self.raceCanvas, text="Select a Driver:        ", text_font=('Calibri', 14, 'bold'))
        driverLabel.place(x=30, y=60)
        driverDropdown = ctk.CTkOptionMenu(self.raceCanvas, width=320, height=35, corner_radius=6, text_font=('Calibri', 14), variable=driverVar, values=driverOptions)
        driverDropdown.place(x=30, y=90)

        driversMenuButton = ctk.CTkButton(self.raceCanvas, text="Predict Result", width=150, height=40, border_width=0, corner_radius=6, fg_color="#03a82f", bg_color="#2b2a2a", text_font=('Calibri', 14, 'bold'), hover=True, hover_color="#00751f", command=lambda: submitDriver(self.raceCanvas, driverVar))
        driversMenuButton.place(x=200, y=500)
        
        driversMenuButton = ctk.CTkButton(self.raceCanvas, text="Pairing Menu", width=150, height=40, border_width=0, corner_radius=6, fg_color="#d90000", bg_color="#2b2a2a", text_font=('Calibri', 14, 'bold'), hover=True, hover_color="#820903", command=lambda: leavePage(controller))
        driversMenuButton.place(x=30, y=500)
        
        self.raceCanvas.create_text(settings.WIDTH/2, 30, text="F1 Predict Best Team For Driver", fill="#d90000", font=('Calibri 32 bold'))
        self.raceCanvas.create_text(settings.WIDTH/4, 590, text=settings.APPDETAILS, fill="#d90000", font=('Calibri 11 bold'))
        self.raceCanvas.pack(side="top", fill = "both", expand = True)


class ConstructorPairing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.championshipCanvas= ctk.CTkCanvas(self, width= settings.WIDTH, height= settings.HEIGHT, bd=0, highlightthickness=0)
        self.championshipCanvas.configure(bg="#2b2a2a")
        
        driverVar = ctk.StringVar(value="None")
        driverOptions = data.getCurrentDrivers()
        driverLabel = ctk.CTkLabel(self.championshipCanvas, text="Select a Driver:        ", text_font=('Calibri', 14, 'bold'))
        driverLabel.place(x=30, y=60)
        driverDropdown = ctk.CTkOptionMenu(self.championshipCanvas, width=320, height=35, corner_radius=6, text_font=('Calibri', 14), variable=driverVar, values=driverOptions)
        driverDropdown.place(x=30, y=90)

        seasonVar = ctk.StringVar(value="None")
        seasons = list(range(1950, 2050))
        seasonOptions = []
        for season in reversed(seasons): 
            seasonOptions.append(str(season))
        seasonLabel = ctk.CTkLabel(self.championshipCanvas, text="Select a Season:      ", text_font=('Calibri', 14, 'bold'))
        seasonLabel.place(x=30, y=140)
        seasonDropdown = ctk.CTkOptionMenu(self.championshipCanvas, width=320, height=35, corner_radius=6, text_font=('Calibri', 14), variable=seasonVar, values=seasonOptions)
        seasonDropdown.place(x=30, y=170)
        
        pointsVar = ctk.IntVar(value=0)
        pointsLabel = ctk.CTkLabel(self.championshipCanvas, text="Select Driver Points for Saeson:     " + str(pointsVar.get()), text_font=('Calibri', 14, 'bold'))
        pointsLabel.place(x=30, y=220)
        pointsSlider = ctk.CTkSlider(master=self.championshipCanvas, variable=pointsVar, width=320, height=30, from_=0, to=1000, number_of_steps=1000, command=lambda value: updateVar(self.championshipCanvas, value, pointsVar, pointsLabel, "Select Driver Points for Season:    "))
        pointsSlider.place(x=30, y=250)
        
        winVar = ctk.IntVar(value=0)
        winLabel = ctk.CTkLabel(self.championshipCanvas, text="Select Driver Wins for Season:    " + str(winVar.get()), text_font=('Calibri', 14, 'bold'))
        winLabel.place(x=30, y=300)
        winSlider = ctk.CTkSlider(master=self.championshipCanvas, variable=winVar, width=320, height=30, from_=0, to=30, number_of_steps=30, command=lambda value: updateVar(self.championshipCanvas, value, winVar, winLabel, "Select Driver Wins for Season:    "))
        winSlider.place(x=30, y=330)

        driversMenuButton = ctk.CTkButton(self.championshipCanvas, text="Predict Result", width=150, height=40, border_width=0, corner_radius=6, fg_color="#03a82f", bg_color="#2b2a2a", text_font=('Calibri', 14, 'bold'), hover=True, hover_color="#00751f", command=lambda: submitChampionship(self.championshipCanvas, driverVar, seasonVar, pointsVar, winVar))
        driversMenuButton.place(x=200, y=500)
        
        driversMenuButton = ctk.CTkButton(self.championshipCanvas, text="Drivers Menu", width=150, height=40, border_width=0, corner_radius=6, fg_color="#d90000", bg_color="#2b2a2a", text_font=('Calibri', 14, 'bold'), hover=True, hover_color="#820903", command=lambda: leavePage(controller))
        driversMenuButton.place(x=30, y=500)
        
        self.championshipCanvas.create_text(settings.WIDTH/2, 30, text="F1 Predict Drivers Championship", fill="#d90000", font=('Calibri 32 bold'))
        self.championshipCanvas.create_text(settings.WIDTH/4, 590, text=settings.APPDETAILS, fill="#d90000", font=('Calibri 11 bold'))
        self.championshipCanvas.pack(side="top", fill = "both", expand = True)
