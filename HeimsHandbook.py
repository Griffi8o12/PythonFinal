"""
Program: HeimsHandbook.py
Author: Caelan Griffith
Date: 11/21/18
"""
import json
import requests

from tkinter import *
import tkinter as tk
root = tk.Tk()
class gui(Frame):
    def __init__(self):
        Frame.__init__(self)
        master = Tk()
        self.grid()
        self._UserIn = StringVar()
        self._summonerName = (str(input("Enter your summoner name :")))
        self._URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + self._summonerName + "?api_key=RGAPI-80b73fe0-54e7-4192-8d26-61ef4d8502f2"
        print(self._URL)
        response = requests.get(self._URL)
        summonerJSON = response.json()

        self._ID = summonerJSON['id']
        self._ID = (str(self._ID))
        self._Level = summonerJSON['summonerLevel']
        self._Level = (str(self._Level))
        
        #Champion Health Points#
        self._champHP = Label(master, text = "HP:", font = ("Helvetica", 16))
        self._champHP.grid(row = 2, column = 0)

        self._champHP_VAL = Label(master, text = "-", font = ("Helvetica", 16))
        self._champHP_VAL.grid(row = 2, column = 1)

        #Champion Mana Points#
        self._champMana = Label(master, text = "Mana:", font = ("Helvetica", 16))
        self._champMana.grid(row = 3, column = 0)

        self._champMana_VAL = Label(master, text = "-", font = ("Helvetica", 16))
        self._champMana_VAL.grid(row = 3, column = 1)
        
        #Champion Movement Speed#
        self._champMoveSpeed = Label(master, text = "Move Speed:", font = ("Helvetica" , 16))
        self._champMoveSpeed.grid(row = 7, column = 0)

        self._champMoveSpeed_VAL = Label(master, text = "-", font = ("Helvetica", 16))
        self._champMoveSpeed_VAL.grid(row = 7, column = 1)
        
        #Champion Aromor#
        self._champArmor = Label(master, text = "Armor:", font = ("Helvetica", 16))
        self._champArmor.grid(row = 5, column = 0)

        self._champArmor_VAL = Label(master, text = "-", font = ("Helvetica", 16))
        self._champArmor_VAL.grid(row = 5, column = 1)
        
        #Champion Magic Resist#
        self._champMagRes = Label(master, text = "Magic Resist:", font = ("Helvetica", 16))
        self._champMagRes.grid(row = 6, column = 0)

        self._champMagRes_VAL = Label(master, text = "-" , font = ("Helvetica",16))
        self._champMagRes_VAL.grid(row = 6, column=  1)
        
        #Champion Attack Damage#
        self._champAD = Label(master, text = "AD:", font = ("Helvetica" , 16))
        self._champAD.grid(row = 4, column = 0)

        self._champAD_VAL = Label(master, text = "-", font = ("Helvetica",16))
        self._champAD_VAL.grid(row = 4 ,column = 1)

        #Summoner Name#
        self._name = Label(master, text = "Summoner: " + self._summonerName, font = ("Helvetica", 16))
        self._name.grid(row = 0, column = 0)

        #Summoner Level#
        self._sumLevel = Label(master, text = "Level: " + self._Level, font = ("Helvetica", 16), justify = LEFT)
        self._sumLevel.grid(row = 1, column = 0)

        #Entry Field#
        self._EntityEntry = Entry(master, bg = "#5BC8AD", bd = 29, insertwidth = 4, width = 24,
                                  font = ("Helvetica", 16), textvariable = self._UserIn)
        self._EntityEntry.grid(row = 2, column = 4)

        #Entry Field Button#
        self._EntityEntry_Button = Button(master, text='Search', command = self.getChampionData)
        self._EntityEntry_Button.grid(row = 2, column = 5)

        #Q#
        self._Q = Label(master, text = "Q:", wraplength = 200, font = ("Helvetica", 10), justify = RIGHT)
        self._Q.grid(row = 3, column = 3)

        #W#
        self._W = Label(master, text = "W: ", wraplength = 200, font = ("Helvetica", 10), justify = RIGHT)
        self._W.grid(row = 5, column = 3)

        #E#
        self._E = Label(master, text = "E: ", wraplength = 200, font = ("Helvetica", 10), justify = RIGHT)
        self._E.grid(row = 3, column = 4)

        #Ult#
        self._R = Label(master, text = "R: ", wraplength = 200, font = ("Helvetica", 10), justify = RIGHT)
        self._R.grid(row = 5, column = 4)

        #Passive#
        self._Passive = Label(master, text = "P: ", wraplength = 200, font = ("Helvetica", 10), justify = RIGHT)
        self._Passive.grid(row = 6, column = 3)

    def getChampionData(self):
        self._URL = "https://ddragon.leagueoflegends.com/cdn/8.15.1/data/en_US/championFull.json"
        print(self._URL)
        response = requests.get(self._URL)
        championJSON = response.json()

        SearchEntry = self._EntityEntry.get()
        #Store Champion data into variables#
        self._championHP = championJSON['data'][SearchEntry]['stats']['hp']
        self._championMana = championJSON['data'][SearchEntry]['stats']['mp']
        self._championMoveS = championJSON['data'][SearchEntry]['stats']['movespeed']
        self._championArmor = championJSON['data'][SearchEntry]['stats']['armor']
        self._championMagRes = championJSON['data'][SearchEntry]['stats']['spellblock']
        self._championAD = championJSON['data'][SearchEntry]['stats']['attackdamage']

        #Update stat lables#
        self._champHP_VAL.config(text = self._championHP)
        self._champMana_VAL.config(text = self._championMana)
        self._champMoveSpeed_VAL.config(text = self._championMoveS)
        self._champArmor_VAL.config(text = self._championArmor)
        self._champMagRes_VAL.config(text = self._championMagRes)
        self._champAD_VAL.config(text = self._championAD)
        
        #Store Champion abilities into variables#
        self._ChampQ = championJSON['data'][SearchEntry]['spells'][0]['description']
        self._ChampW = championJSON['data'][SearchEntry]['spells'][1]['description']
        self._ChampE = championJSON['data'][SearchEntry]['spells'][2]['description']
        self._ChampR = championJSON['data'][SearchEntry]['spells'][3]['description']
        self._ChampP = championJSON['data'][SearchEntry]['passive']['description']

        #Update the ability lables#
        self._Q.config(text = "Q: " + self._ChampQ)
        self._W.config(text = "W: " + self._ChampW)
        
        self._E.config(text = "E: " + self._ChampE)
        self._R.config(text = "R: " + self._ChampR)
        self._Passive.config(text = "P: " + self._ChampP)
def main():
    gui()
if __name__ == "__main__":
    main()
