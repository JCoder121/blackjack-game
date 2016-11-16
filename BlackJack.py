from Tkinter import *
import time
import sys
import random
import Queue
from random import shuffle

#establish deck
deck = [(i+1) for i in range(52)]
shuffle(deck)
print deck


#Global variables
bWidth = 800
bHeight = 400
HouseMoney = 1000000
p_Money = 100
temp = 0
betval = 0
Pic_file_path = 'C:\Python27\Jeff_home\Games\Pictures\Gif\\'
list_Comp = []
list_You = []


file_list = ['gif_CardBack.gif',
             'gif_d_ace.gif', 'gif_d_two.gif', 'gif_d_three.gif', 'gif_d_four.gif', 'gif_d_five.gif', 'gif_d_six.gif','gif_d_seven.gif',
             'gif_d_eight.gif','gif_d_nine.gif','gif_d_ten.gif','gif_d_jack.gif','gif_d_queen.gif','gif_d_king.gif',
             
             'gif_s_ace.gif', 'gif_s_two.gif', 'gif_s_three.gif', 'gif_s_four.gif', 'gif_s_five.gif', 'gif_s_six.gif','gif_s_seven.gif',
             'gif_s_eight.gif','gif_s_nine.gif','gif_s_ten.gif','gif_s_jack.gif','gif_s_queen.gif','gif_s_king.gif',

             'gif_h_ace.gif', 'gif_h_two.gif', 'gif_h_three.gif', 'gif_h_four.gif', 'gif_h_five.gif', 'gif_h_six.gif','gif_h_seven.gif',
             'gif_h_eight.gif','gif_h_nine.gif','gif_h_ten.gif','gif_h_jack.gif','gif_h_queen.gif','gif_h_king.gif',             

             'gif_c_ace.gif', 'gif_c_two.gif', 'gif_c_three.gif', 'gif_c_four.gif', 'gif_c_five.gif', 'gif_c_six.gif','gif_c_seven.gif',
             'gif_c_eight.gif','gif_c_nine.gif','gif_c_ten.gif','gif_c_jack.gif','gif_c_queen.gif','gif_c_king.gif',        
             ] 
            
root = Tk()
board = Canvas(root, width=bWidth, height=bHeight)
board.create_line(0, bHeight/2, bWidth, bHeight/2)
board.configure(background = '#277714')
root.configure(background = 'blue')
betdisplay = board.create_text(55,300, text ="Place bet", font = ('Arial', 15))

ePlayerMoney = Entry(root)
ePlayerMoney.grid(row = 25, column = 20)
ePlayerMoney.insert(0, "Player: " + str(p_Money))

def Bet():
    global betval, betdisplay
    global p_Money
    global ePlayerMoney
    board.delete(betdisplay)
    betval = betval+10
    p_Money = p_Money - 10
    ePlayerMoney.delete(0, END)
    ePlayerMoney.insert(0, "Player: " + str(p_Money))
    if p_Money <= 0:
        BetBtn.config(state = 'disabled')
    betdisplay = board.create_text(55,300, text ="Bet: $" + str(betval), font = ('Arial',15))

def Deal():
    global list_Comp, list_You
    global t_Comp, t_You
    global you_image, comp_image
    global temp_You, temp_Comp
    global Pic_file_path, file_list

    card_x = 165

    House_secret = deck.pop(0)
    list_Comp.append(House_secret)
    comp_image = PhotoImage(file=(Pic_file_path + file_list[0]) )
    t_Comp = board.create_image(165,42, anchor = NW, image=comp_image)
    
    temp_Comp = deck.pop(0)
    list_Comp.append(temp_Comp)
    comp_image2 = PhotoImage(file=(Pic_file_path + file_list[temp_Comp]) )
    t_Comp = board.create_image(165+85,42, anchor = NW, image=comp_image2)
##    
##    temp_You = deck.pop(0)
##    list_You.append(temp_You)
##    you_image = PhotoImage(file=(Pic_file_path + file_list[temp_You]) )
##    t_You = board.create_image(250,255, anchor = NW, image=you_image)
##
##    
##    temp_You = deck.pop(0)
##    list_You.append(temp_You)
##    you_image2 = PhotoImage(file=(Pic_file_path + file_list[temp_You]) )
##    t_You = board.create_image(card_x + 85,255, anchor = NW, image=you_image)

    board.update()
    print "list_house_card", list_Comp
    print "list_you_card", list_You

#cards

eYouCards = Entry(root)
eCompCards = Entry(root)
eTurns = Entry(root)

you_image = PhotoImage(file=(Pic_file_path + file_list[0]) )
comp_image = PhotoImage(file=(Pic_file_path + file_list[26]) )
t_You = board.create_image(165,255, anchor = NW, image=comp_image)
t_Comp = board.create_image(165,42, anchor = NW, image=you_image)

#add button commands later
DealBtn = Button(root, text = "Deal", command = Deal)
HitBtn = Button(root, text = "Hit")
StayBtn = Button(root, text = "Stay")
BetBtn = Button(root, text = "Bet $10", command = Bet)

#words
board.create_text(400, 200, text='Beware, money will be lost here!',
font=('Helvetica', 30))

eHouseMoney = Entry(root)
eHouseMoney.grid(row = 25, column = 20)
eHouseMoney.pack()
eHouseMoney.insert(0, "House: " + str(HouseMoney))

board.pack()

HitBtn.pack()
StayBtn.pack()
BetBtn.pack()
DealBtn.place(bordermode=OUTSIDE, height = 40, width = 40, x= 600, y =300)
BetBtn.place(bordermode=OUTSIDE, height=40, width=50, x = 540, y = 300)
HitBtn.place(bordermode=OUTSIDE, height=40, width=40, x = 650, y = 300)
StayBtn.place(bordermode=OUTSIDE, height=40, width=40, x = 700, y = 300)
ePlayerMoney.pack()

root.mainloop()
