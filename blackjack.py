from Tkinter import *
import time
import sys

bSize = 400
HouseMoney = 1000000
PlayerMoney = 100

root = Tk()
board = Canvas(root, width=bSize, height=bSize)
board.create_line(0, bSize/2, bSize, bSize/2)

#shapes
board.create_polygon(10, 10, 100, 10, 100, 110, fill="yellow",
outline="black")

#words
board.create_text(200, 200, text='Beware, money will be lost here!',
font=('Helvetica', 20))

eHouseMoney = Entry(root)
eHouseMoney.grid(row = 25, column = 20)
eHouseMoney.pack()
eHouseMoney.insert(0, "House: " + str(HouseMoney))

board.pack()

ePlayerMoney = Entry(root)
ePlayerMoney.grid(row = 25, column = 20)
ePlayerMoney.pack()
ePlayerMoney.insert(0, "Player: " + str(PlayerMoney))


root.mainloop()
