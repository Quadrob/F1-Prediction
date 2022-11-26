import sqlite3


DATABASECONNECTION = None


def connectToDatabase():
    """Create a connection to the database"""
    global DATABASECONNECTION
    DATABASECONNECTION = sqlite3.connect('DB/F1_DB.db')
    print("Opened database connection!")


def disconnectFromDatabase():
    """Disconnect from an active connection to the database"""
    global DATABASECONNECTION
    if (DATABASECONNECTION != None):
        DATABASECONNECTION.close()
        DATABASECONNECTION = None
        print("Closing database connection!")
    else:
        print("There was no active connection to close.")

