# Use Tkinter for python 2, tkinter for python 3
import Tkinter as tk
import time, sys, random
from random import shuffle


#establish deck
deck = [(i+1) for i in range(52)]
shuffle(deck)
print deck

#Global variables
#Pic_file_path = 'C:\Python27\Jeff_home\Games\Pictures\Gif\\'
Pic_file_path = 'C:\Python27\Jeff_home\Games\Pictures\Gif\\'

list_Comp = []
list_You = []

file_list = ['gif_CardBack.gif',
             'gif_h_ace.gif', 'gif_h_two.gif', 'gif_h_three.gif', 'gif_h_four.gif', 'gif_h_five.gif', 'gif_h_six.gif','gif_h_seven.gif',
             'gif_h_eight.gif','gif_h_nine.gif','gif_h_ten.gif','gif_h_jack.gif','gif_h_queen.gif','gif_h_king.gif',
             
             'gif_d_ace.gif', 'gif_d_two.gif', 'gif_d_three.gif', 'gif_d_four.gif', 'gif_d_five.gif', 'gif_d_six.gif','gif_d_seven.gif',
             'gif_d_eight.gif','gif_d_nine.gif','gif_d_ten.gif','gif_d_jack.gif','gif_d_queen.gif','gif_d_king.gif',
             
             'gif_s_ace.gif', 'gif_s_two.gif', 'gif_s_three.gif', 'gif_s_four.gif', 'gif_s_five.gif', 'gif_s_six.gif','gif_s_seven.gif',
             'gif_s_eight.gif','gif_s_nine.gif','gif_s_ten.gif','gif_s_jack.gif','gif_s_queen.gif','gif_s_king.gif',           

             'gif_c_ace.gif', 'gif_c_two.gif', 'gif_c_three.gif', 'gif_c_four.gif', 'gif_c_five.gif', 'gif_c_six.gif','gif_c_seven.gif',
             'gif_c_eight.gif','gif_c_nine.gif','gif_c_ten.gif','gif_c_jack.gif','gif_c_queen.gif','gif_c_king.gif',        
             ] 
    
class BlackJack(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        parent.title("BlackJack")

        # Initialize variables
        bWidth = 800
        bHeight = 400
        self.HouseMoney = 1000000
        self.p_Money = 100
        self.betval = 0
        
        # <create the rest of your GUI here>
        self.configure(background = 'blue')
        
        # Two money Entry, one for house, on for player
        self.ePlayerMoney = tk.Entry(self)
        self.ePlayerMoney.grid(row = 25, column = 20)
        self.ePlayerMoney.insert(0, "Player: " + str(self.p_Money))

        self.eHouseMoney = tk.Entry(self)
        self.eHouseMoney.grid(row = 25, column = 20)
        self.eHouseMoney.insert(0, "House: " + str(self.HouseMoney))

        # Main play board
        self.board = tk.Canvas(self, width=bWidth, height=bHeight)
        self.board.create_line(0, bHeight/2, bWidth, bHeight/2)
        self.board.configure(background = '#277714')
        self.betdisplay = self.board.create_text(55,300, text ="Place bet", font = ('Arial', 15))
        self.board.create_text(400, 200, text='Beware, money will be lost here!',
        font=('Helvetica', 30))
        
        # Buttons
        self.DealBtn = tk.Button(self, text = "Deal", command = self.Deal)
        self.HitBtn = tk.Button(self, text = "Hit")
        self.StayBtn = tk.Button(self, text = "Stay", command = self.Stay)
        self.BetBtn = tk.Button(self, text = "Bet $10", command = self.Bet)

        # Pack and placement
        self.eHouseMoney.pack()
        self.board.pack()
        self.HitBtn.pack()
        self.StayBtn.pack()
        self.BetBtn.pack()
        self.DealBtn.place(bordermode=tk.OUTSIDE, height = 40, width = 40, x= 600, y =300)
        self.BetBtn.place(bordermode=tk.OUTSIDE, height=40, width=50, x = 540, y = 300)
        self.HitBtn.place(bordermode=tk.OUTSIDE, height=40, width=40, x = 650, y = 300)
        self.StayBtn.place(bordermode=tk.OUTSIDE, height=40, width=40, x = 700, y = 300)
        self.ePlayerMoney.pack()

    def Deal(self):
        global deck, list_Comp, list_You
        card_x = 165
        
        self.BetBtn.config(state = 'disabled')
        self.House_secret = deck.pop(0)
        list_Comp.append(self.House_secret)
        self.comp_image = tk.PhotoImage(file=(Pic_file_path + file_list[0]) )
        self.t_Comp = self.board.create_image(card_x,42, anchor = tk.NW, image=self.comp_image)
        
        self.temp_Comp = deck.pop(0)
        list_Comp.append(self.temp_Comp)
        self.comp_image2 = tk.PhotoImage(file=(Pic_file_path + file_list[self.temp_Comp]) )
        self.t_Comp = self.board.create_image(card_x+85,42, anchor = tk.NW, image=self.comp_image2)
        
        self.temp_You = deck.pop(0)
        list_You.append(self.temp_You)
        self.you_image = tk.PhotoImage(file=(Pic_file_path + file_list[self.temp_You]) )
        self.t_You = self.board.create_image(card_x,255, anchor = tk.NW, image=self.you_image)
    
        self.temp_You = deck.pop(0)
        list_You.append(self.temp_You)
        self.you_image2 = tk.PhotoImage(file=(Pic_file_path + file_list[self.temp_You]) )
        self.t_You = self.board.create_image(card_x+85,255, anchor = tk.NW, image=self.you_image2)

        self.board.update()
        print "list_house_card", list_Comp
        print "list_you_card", list_You

    def Bet(self):        
        self.betval = self.betval + 10
        self.p_Money = self.p_Money - 10
        
        self.ePlayerMoney.delete(0, tk.END)
        self.ePlayerMoney.insert(0, "Player: " + str(self.p_Money))
        if self.p_Money <= 0:
            self.BetBtn.config(state = 'disabled')
            
        self.board.delete(self.betdisplay)    
        self.betdisplay = self.board.create_text(55,300, text ="Bet: $" + str(self.betval), font = ('Arial',15))

##    def Deal(self):
##        #Finish up


    def Stay(self):    
        #Finish
        self.HitBtn.config(state='disabled')
        self.StayBtn.config(state='disabled')
        

    def quit(self):
        sys.exit()        

if __name__ == "__main__":
    root = tk.Tk()
    BlackJack(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
