# My first Python program!
# This was a basic tutorial from a friend who was teaching me how to code.  
# All code written by me, but supervised and instructed by tutor

import Tkinter as tk

class FFTA:

	def __init__(self, master):
		self.createOpeningFrame(master)
		self.statTable = {
			"Human" : {
				"Soldier" : {
				    "WepAtk": 8.5,
				    "WepDef": 8.5,
				    "HP": 8.5,
				    "MP": 1,
				    "MagPow": 6.5,
				    "MagDef": 7,
				    "Speed": 1,
				},
				"Paladin" : {
					"WepAtk": 8,
					"WepDef": 9,
					"HP": 7,
					"MP": 2.5,
					"MagPow": 7,
					"MagDef": 8.5,
					"Speed": 0,
				},
				"Fighter" : {
		            "WepAtk" : 9.5,
		            "WepDef" : 8,
		            "HP" : 7.5,
		            "MP" : 1,
		            "MagPow" : 5,
		            "MagDef" : 6.5,
		            "Speed" : 1.5,
		        },
		        "Archer" : {
		            "WepAtk" : 7.5,
		            "WepDef" : 7,
		            "HP" : 7,
		            "MP" : 1,
		            "MagPow" : 7.5,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "Hunter" : {
		            "WepAtk" : 8,
		            "WepDef" : 6.5,
		            "HP" : 6,
		            "MP" : 3,
		            "MagPow" : 6,
		            "MagDef" : 8,
		            "Speed" : 1,
		        },
		        "Thief" : {
		            "WepAtk" : 7.5,
		            "WepDef" : 7,
		            "HP" : 6.5,
		            "MP" : 1,
		            "MagPow" : 8,
		            "MagDef" : 6,
		            "Speed" : 1.5,
		        }, 
		        "Ninja" : {
		            "WepAtk" : 8,
		            "WepDef" : 7.5,
		            "HP" : 5.5,
		            "MP" : 2,
		            "MagPow" : 8,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "White Mage" : {
		            "WepAtk" : 6,
		            "WepDef" : 7,
		            "HP" : 6,
		            "MP" : 4,
		            "MagPow" : 8,
		            "MagDef" : 8,
		            "Speed" : 1,
		        },
		        "Black Mage" : {
		            "WepAtk" : 6.5,
		            "WepDef" : 6,
		            "HP" : 5,
		            "MP" : 4,
		            "MagPow" : 8,
		            "MagDef" : 9,
		            "Speed" : 1,
		        },
		        "Blue Mage" : {
		            "WepAtk" : 8,
		            "WepDef" : 8.5,
		            "HP" : 6.5,
		            "MP" : 3.5,
		            "MagPow" : 8,
		            "MagDef" : 9,
		            "Speed" : 1,
		        },
		        "Illusionist" : {
		            "WepAtk" : 6,
		            "WepDef" : 6,
		            "HP" : 5,
		            "MP" : 7.5,
		            "MagPow" : 9,
		            "MagDef" : 8,
		            "Speed" : 0,
		        }
		    },
		    "Bangaa" : {
		        "White Monk" : {
		            "WepAtk" : 8.5,
		            "WepDef" : 7.5,
		            "HP" : 6.5,
		            "MP" : 1.5,
		            "MagPow" : 8.5,
		            "MagDef" : 6.5,
		            "Speed" : 1.5,
		        },
		        "Warrior" : {
		            "WepAtk" : 9.5,
		            "WepDef" : 8.5,
		            "HP" : 9.5,
		            "MP" : 2,
		            "MagPow" : 6.5,
		            "MagDef" : 6.5,
		            "Speed" : 0.5,
		        },
		        "Defender" : {
		            "WepAtk" : 8.5,
		            "WepDef" : 9.5,
		            "HP" : 8.5,
		            "MP" : 1.5,
		            "MagPow" : 6.5,
		            "MagDef" : 7.5,
		            "Speed" : 0.5,
		        },
		        "Gladiator" : {
		            "WepAtk" : 9.5,
		            "WepDef" : 8.5,
		            "HP" : 8.5,
		            "MP" : 2.5,
		            "MagPow" : 6,
		            "MagDef" : 6.5,
		            "Speed" : 1.5,
		        },
		        "Bishop" : {
		            "WepAtk" : 7.5,
		            "WepDef" : 6.5,
		            "HP" : 6,
		            "MP" : 4.5,
		            "MagPow" : 8.5,
		            "MagDef" : 7.5,
		            "Speed" : 0.5,
		        },
		        "Templar" : {
		            "WepAtk" : 8.5,
		            "WepDef" : 9.5,
		            "HP" : 7.5,
		            "MP" : 3.5,
		            "MagPow" : 8.5,
		            "MagDef" : 7.5,
		            "Speed" : 0.5,
		        },
		        "Dragoon" : {
		            "WepAtk" : 9.5,
		            "WepDef" : 8.5,
		            "HP" : 8,
		            "MP" : 1.5,
		            "MagPow" : 5.5,
		            "MagDef" : 6.5,
		            "Speed" : 1.5,
		        }
		    },
		    "Viera" : {
		        "Archer" : {
		            "WepAtk" : 8,
		            "WepDef" : 6.5,
		            "HP" : 7.5,
		            "MP" : 1.5,
		            "MagPow" : 7.5,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "Sniper" : {
		            "WepAtk" : 9.5,
		            "WepDef" : 6.5,
		            "HP" : 6.5,
		            "MP" : 2.5,
		            "MagPow" : 7.5,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "Assassin" : {
		            "WepAtk" : 8.5,
		            "WepDef" : 6.5,
		            "HP" : 5,
		            "MP" : 5.5,
		            "MagPow" : 9,
		            "MagDef" : 7,
		            "Speed" : 2.5,
		        },
		        "Fencer" : {
		            "WepAtk" : 8.5,
		            "WepDef" : 8.5,
		            "HP" : 7.5,
		            "MP" : 1,
		            "MagPow" : 7.5,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "Elementalist" : {
		            "WepAtk" : 8,
		            "WepDef" : 7.5,
		            "HP" : 6.5,
		            "MP" : 4.5,
		            "MagPow" : 9,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "White Mage" : {
		            "WepAtk" : 6.5,
		            "WepDef" : 7.5,
		            "HP" : 6.5,
		            "MP" : 4,
		            "MagPow" : 8.5,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "Red Mage" : {
		            "WepAtk" : 8,
		            "WepDef" : 7.5,
		            "HP" : 6.5,
		            "MP" : 2.5,
		            "MagPow" : 8.5,
		            "MagDef" : 7.5,
		            "Speed" : 1.5,
		        },
		        "Summoner" : {
		            "WepAtk" : 6.5,
		            "WepDef" : 6.5,
		            "HP" : 6,
		            "MP" : 6.5,
		            "MagPow" : 10.5,
		            "MagDef" : 8.5,
		            "Speed" : 1,
		        }
		    },
		    "Nu Mou" : {
		        "White Mage" : {
		            "WepAtk" : 6,
		            "WepDef" : 7.5,
		            "HP" : 5.5,
		            "MP" : 5,
		            "MagPow" : 8.5,
		            "MagDef" : 8.5,
		            "Speed" : 1,
		        },
		        "Black Mage" : {
		            "WepAtk" : 6,
		            "WepDef" : 6.5,
		            "HP" : 5,
		            "MP" : 6,
		            "MagPow" : 9,
		            "MagDef" : 10,
		            "Speed" : .5,
		        },
		        "Time Mage" : {
		            "WepAtk" : 5,
		            "WepDef" : 6,
		            "HP" : 5,
		            "MP" : 3,
		            "MagPow" : 10,
		            "MagDef" : 10,
		            "Speed" : 1,
		        },
		        "Morpher" : {
		            "WepAtk" : 7,
		            "WepDef" : 8,
		            "HP" : 6.5,
		            "MP" : 2,
		            "MagPow" : 7,
		            "MagDef" : 8,
		            "Speed" : 1,
		        },
		        "Alchemist" : {
		            "WepAtk" : 5.5,
		            "WepDef" : 5.5,
		            "HP" : 6,
		            "MP" : 8.5,
		            "MagPow" : 9,
		            "MagDef" : 9.5,
		            "Speed" : .5,
		        },
		        "Sage" : {
		            "WepAtk" : 8,
		            "WepDef" : 7,
		            "HP" : 7,
		            "MP" : 8,
		            "MagPow" : 9,
		            "MagDef" : 7,
		            "Speed" : 0,
		        },
		        "Beast Master" : {
		            "WepAtk" : 8.5,
		            "WepDef" : 7.5,
		            "HP" : 7,
		            "MP" : 2,
		            "MagPow" : 7.5,
		            "MagDef" : 8.5,
		            "Speed" : 1,
		        },
		        "Illusionist" : {
		            "WepAtk" : 5,
		            "WepDef" : 6,
		            "HP" : 5,
		            "MP" : 7,
		            "MagPow" : 9,
		            "MagDef" : 8,
		            "Speed" : 0,
		        }
			},
			"Moogle" : {
		        "Animist" : {
		            "WepAtk" : 7.5,
		            "WepDef" : 8.5,
		            "HP" : 7.5,
		            "MP" : 2.5,
		            "MagPow" : 7,
		            "MagDef" : 9,
		            "Speed" : 1.5,
		        },
		        "Thief" : {
		            "WepAtk" : 7.5,
		            "WepDef" : 8,
		            "HP" : 6,
		            "MP" : 2,
		            "MagPow" : 6.5,
		            "MagDef" : 7,
		            "Speed" : 2,
		        },
		        "Juggler" : {
		            "WepAtk" : 8,
		            "WepDef" : 9.5,
		            "HP" : 6.5,
		            "MP" : 1,
		            "MagPow" : 6,
		            "MagDef" : 6,
		            "Speed" : 1,
		        },
		        "Knight" : {
		            "WepAtk" : 9,
		            "WepDef" : 9.5,
		            "HP" : 7,
		            "MP" : 3,
		            "MagPow" : 7,
		            "MagDef" : 8,
		            "Speed" : 1,
		        },
		        "Black Mage" : {
		            "WepAtk" : 6,
		            "WepDef" : 7.5,
		            "HP" : 5.5,
		            "MP" : 4.5,
		            "MagPow" : 8.5,
		            "MagDef" : 10,
		            "Speed" : 1.5,
		        },
		        "Time Mage" : {
		            "WepAtk" : 6,
		            "WepDef" : 8.5,
		            "HP" : 6,
		            "MP" : 3.5,
		            "MagPow" : 9,
		            "MagDef" : 9,
		            "Speed" : 1,
		        },
		        "Gunner" : {
		            "WepAtk" : 7,
		            "WepDef" : 9,
		            "HP" : 6.5,
		            "MP" : 1,
		            "MagPow" : 5,
		            "MagDef" : 8,
		            "Speed" : 1,
		        },
		        "Gadgeteer" : {
		            "WepAtk" : 8,
		            "WepDef" : 9.5,
		            "HP" : 7.5,
		            "MP" : 2.5,
		            "MagPow" : 8,
		            "MagDef" : 10.5,
		            "Speed" : 1,
		        }
			}
		}
		self.statList = ["WepAtk","WepDef","HP","MP","MagPow","MagDef","Speed"]
		self.currentStats = {}
		self.finalStats = {}

	def createOpeningFrame(self, master):
		self.openingFrame = tk.Frame(master)
		self.openingFrame.pack()

		self.openingText = tk.Label(self.openingFrame, text="Final Fantasy Tactics Advanced Leveler", font = ("Arial",14), pady = 10)
		self.openingText.grid(row=0)

		self.openingButton = tk.Button(self.openingFrame, text="Click Here to Start", command=lambda x=master: self.startNextWindow(x))
		self.openingButton.grid(row=2)

		self.blankLabel3 = tk.Label(self.openingFrame, text = "")
		self.blankLabel3.grid(row = 3)

	def startNextWindow(self, master):
		self.openingFrame.pack_forget()

		self.mainFrame = tk.Frame(master)
		self.mainFrame.pack()

		self.mainLabel = tk.Label(self.mainFrame, text="Final Fantasy Tactics Advanced Leveler", font = ("Arial",14))
		self.mainLabel.grid(row=0, column=0, columnspan= 7)

		self.statLabel = {}
		self.statEntry = {}
		i=0
		for row in range(4):
			for column in range(4):
				try:
					if column%2:
						self.statEntry[self.statList[i]] = tk.Entry(self.mainFrame, width = 7)
						self.statEntry[self.statList[i]].grid(row = row + 1, column = column + 1)
						i += 1					
					else:
						self.statLabel[self.statList[i]] = tk.Label(self.mainFrame, text=self.statList[i], width = 7, height = 2)
						self.statLabel[self.statList[i]].grid(row = row + 1, column = column + 1)
				except:
					pass

		self.raceVariable = self.statTable.keys()

		self.raceLabel = tk.Label(self.mainFrame, text = "Race:", width=7)
		self.raceLabel.grid(row = 1, column = 5)
		self.raceVar = tk.StringVar(self.mainFrame)
		self.raceVar.set('              ')
		self.raceMenu = tk.OptionMenu(self.mainFrame, self.raceVar, *self.statTable.keys())
		self.raceMenu.grid(row = 1, column = 6)

		self.classLabel = tk.Label(self.mainFrame, text = "Class:", width=7)
		self.classLabel.grid(row = 2, column = 5)
		self.classVar = tk.StringVar(self.mainFrame)
		self.classVar.set('              ')
		self.classMenu = tk.OptionMenu(self.mainFrame, self.classVar,'              ')
		self.classMenu.grid(row = 2, column = 6)

		self.raceVar.trace('w', self.updateMenu)

		self.pLevelsLabel = tk.Label(self.mainFrame, text = "Levels", width=7)
		self.pLevelsLabel.grid(row = 3, column = 5)
		self.pLevelsEntry = tk.Entry(self.mainFrame, width = 7)
		self.pLevelsEntry.grid(row = 3, column = 6)

		self.calculateButton = tk.Button(self.mainFrame, text = "Calculate", width=11, command=self.Calculate)
		self.calculateButton.grid(row = 4, column = 6, rowspan = 2)

		self.clearButton = tk.Button(self.mainFrame, text = "Clear", width=7, command=self.Clear)
		self.clearButton.grid(row = 4, column = 5, rowspan = 2)

		self.resetButton = tk.Button(self.mainFrame, text = "Reset", width=7, command=self.Reset)
		self.resetButton.grid(row = 4, column = 4, rowspan = 2)

		self.blankLabel = tk.Label(self.mainFrame, text = "")
		self.blankLabel.grid(row = 5)
		self.blankLabel2 = tk.Label(self.mainFrame, text = "     	")
		self.blankLabel2.grid(column = 7)

	def updateMenu(self,*args):
		
		self.classMenu['menu'].delete(0, tk.END)

		try:
			for Class in self.statTable[self.raceVar.get()].keys():
				self.classMenu['menu'].add_command(label = Class, command = lambda x = Class: self.classVar.set(x))
		except:
			pass

		self.classVar.set('              ')

	def Clear(self):

		for Stat in self.statList:
			self.statEntry[Stat].delete(0,tk.END)

		self.raceVar.set('              ')
		self.classVar.set('              ')
		self.pLevelsEntry.delete(0,tk.END)


		self.classMenu['menu'].delete(0, tk.END)

	def Calculate(self):

		for Stat in self.statList:
	
			self.currentStats[Stat] = float(self.statEntry[Stat].get())
			self.finalStats[Stat] = self.currentStats[Stat] + (float(self.pLevelsEntry.get()) * self.statTable[self.raceVar.get()][self.classVar.get()][Stat])
			self.statEntry[Stat].delete(0, tk.END)
			self.statEntry[Stat].insert(0, self.finalStats[Stat])

	def Reset(self):

		for Stat in self.statList:

			self.statEntry[Stat].delete(0, tk.END)
			try:
				self.statEntry[Stat].insert(0, self.currentStats[Stat])
			except:
				pass

root = tk.Tk()

ffta = FFTA(root)

root.mainloop()