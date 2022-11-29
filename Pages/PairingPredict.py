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
        driverResults = q.get()
        driverResults = pd.DataFrame(driverResults)
        driverPos = driverResults[(driverResults['driver'] == str(driver))]
        q.queue.clear()

        Thread(target=predict.predictConstructorPairing(q), daemon=True).start()
        constructorResults = q.get()
        constructorResults = pd.DataFrame(constructorResults)
        bestConstructor = constructorResults.iloc[int(driverPos['predicted']) - 1]
        loadingLabel.destroy()

        headingLabel = ctk.CTkLabel(canvas, text="Results of Predicted Driver / Constructor Combination:", fg_color='#035b99', text_font=('Calibri', 22, 'bold'))
        headingLabel.place(x=400, y=70)
        driverLabel = ctk.CTkLabel(canvas, text=("For Driver: " + str(driver)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        driverLabel.place(x=450, y=140)
        predictLabel = ctk.CTkLabel(canvas, text=("The best Constructor would be: " + str(bestConstructor['constructor'])), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        predictLabel.place(x=450, y=200)
        resultsElements.extend([headingLabel, driverLabel, predictLabel])
        driverVar.set(None)
    else:
        loadingLabel.destroy()
        invalidLabel = ctk.CTkLabel(canvas, text="Please select a value from the dropdown?", bg_color='#d90000', text_font=('Calibri', 16, 'bold'))
        invalidLabel.place(x=570, y=250)
        canvas.update_idletasks()
        invalidLabel.after(3000, invalidLabel.destroy())


def submitConstructor(canvas, constructorVar):
    for element in resultsElements:
        try:
            element.destroy()
        except:
            print()
    loadingLabel = ctk.CTkLabel(canvas, text="Loading...", bg_color='#035b99', text_font=('Calibri', 16, 'bold'))
    loadingLabel.place(x=680, y=250)
    canvas.update_idletasks()
    q = queue.Queue()
    constructor = constructorVar.get() if constructorVar.get() else 'None'
    
    if (constructor != 'None'):
        Thread(target=predict.predictConstructorPairing(q), daemon=True).start()
        constructorResults = q.get()
        constructorResults = pd.DataFrame(constructorResults)
        constructorPos = constructorResults[(constructorResults['constructor'] == str(constructor))]
        q.queue.clear()
        
        Thread(target=predict.predictDriverPairing(q), daemon=True).start()
        driverResults = q.get()
        driverResults = pd.DataFrame(driverResults)
        firstDriver = driverResults.iloc[int(constructorPos.index[0])]
        secondDriver = driverResults.iloc[int(constructorPos.index[1])]
        loadingLabel.destroy()

        headingLabel = ctk.CTkLabel(canvas, text="Results of Predicted Driver / Constructor Combination:", fg_color='#035b99', text_font=('Calibri', 22, 'bold'))
        headingLabel.place(x=400, y=70)
        constructorLabel = ctk.CTkLabel(canvas, text=("For Constructor: " + str(constructor)), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        constructorLabel.place(x=450, y=140)
        predictLabel = ctk.CTkLabel(canvas, text=("The best Drivers would be: "), fg_color='#035b99', text_font=('Calibri', 16, 'bold'))
        predictLabel.place(x=450, y=200) 
        firstLabel = ctk.CTkLabel(canvas, text=("First Driver: " + str(firstDriver['driver'])), fg_color='#035b99', text_font=('Calibri', 14, 'bold'))
        firstLabel.place(x=450, y=270) 
        secondLabel = ctk.CTkLabel(canvas, text=("Second Driver: " + str(secondDriver['driver'])), fg_color='#035b99', text_font=('Calibri', 14, 'bold'))
        secondLabel.place(x=750, y=270) 
        resultsElements.extend([headingLabel, constructorLabel, firstLabel, secondLabel])
        constructorVar.set(None)
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

        self.qualifyingCanvas= ctk.CTkCanvas(self, width= settings.WIDTH, height= settings.HEIGHT, bd=0, highlightthickness=0)
        self.qualifyingCanvas.configure(bg="#2b2a2a")

        constructorVar = ctk.StringVar(value="None")
        constructorOptions = data.getCurrentConstructors()
        constructorLabel = ctk.CTkLabel(self.qualifyingCanvas, text="Select a Constructor:        ", text_font=('Calibri', 14, 'bold'))
        constructorLabel.place(x=30, y=60)
        constructorDropdown = ctk.CTkOptionMenu(self.qualifyingCanvas, width=320, height=35, corner_radius=6, text_font=('Calibri', 14), variable=constructorVar, values=constructorOptions)
        constructorDropdown.place(x=30, y=90)        

        constructorsMenuButton = ctk.CTkButton(self.qualifyingCanvas, text="Predict Result", width=150, height=40, border_width=0, corner_radius=6, fg_color="#03a82f", bg_color="#2b2a2a", text_font=('Calibri', 13, 'bold'), hover=True, hover_color="#00751f", command=lambda: submitConstructor(self.qualifyingCanvas, constructorVar))
        constructorsMenuButton.place(x=200, y=500)
        
        constructorsMenuButton = ctk.CTkButton(self.qualifyingCanvas, text="Pairing Menu", width=150, height=40, border_width=0, corner_radius=6, fg_color="#d90000", bg_color="#2b2a2a", text_font=('Calibri', 13, 'bold'), hover=True, hover_color="#820903", command=lambda: leavePage(controller))
        constructorsMenuButton.place(x=30, y=500)
        
        self.qualifyingCanvas.create_text(settings.WIDTH/2, 30, text="F1 Predict Best Drivers for Constructor", fill="#d90000", font=('Calibri 32 bold'))
        self.qualifyingCanvas.create_text(settings.WIDTH/4, 590, text=settings.APPDETAILS, fill="#d90000", font=('Calibri 11 bold'))
        self.qualifyingCanvas.pack(side="top", fill = "both", expand = True)
