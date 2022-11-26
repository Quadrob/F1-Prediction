import pandas as pd

# Global Variables
global APPDETAILS
global FINALDATAFRAME
global WIDTH
global HEIGHT
global CIRCUITCOUNTRYDICT

# Populate Global Variables
APPDETAILS = "© 2022 Copyright. All Rights Reserved.\tCreated by: Robert Zeelie.\tVersion: 0.0.1"
FINALDATAFRAME = pd.DataFrame()
WIDTH, HEIGHT = 1100, 600
CIRCUITCOUNTRYDICT = pd.DataFrame()

# Generl Functiond
def centerWindow(window, width, height):
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    x = w / 2 - width / 2
    y = h / 2 - height / 2
    window.geometry("%dx%d+%d+%d" % ((width, height) + (x, y)))


