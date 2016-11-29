# Use Tkinter for python 2, tkinter for python 3
import Tkinter as tk
import time, sys, random
from random import shuffle


#establish deck
deck = [(i+1) for i in range(52)]
shuffle(deck)
print deck

#Global variables
Pic_file_path = '/Users/jeffrey/Documents/Python27/AllCards/'
#Pic_file_path = 'C:\Users\Bill\Documents\GitHub_Python\Pictures\gif\\'

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
        bWidth = 1050
        bHeight = 400
        self.HouseMoney = 1000000
        self.p_Money = 100
        self.betval = 0
        self.list_card = []
        self.list_image = []
        self.list_you_val=[]
        self.list_comp_val=[]
        self.hit_cnt = 0
        self.start_card_x = 165
        offset = 200
        
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
        self.board.create_text(500, 200, text='Beware, money will be lost here!',
        font=('Helvetica', 30))
        
        # Buttons
        self.DealBtn = tk.Button(self, text = "Deal", command = self.Deal)
        self.HitBtn = tk.Button(self, text = "Hit", command = self.Hit)
        self.StayBtn = tk.Button(self, text = "Stay",command = self.Stay)
        self.BetBtn = tk.Button(self, text = "Bet $10", command = self.Bet)
        self.ResBtn = tk.Button(self, text = "Restart", command =self.Res)

        # Pack and placement
        self.eHouseMoney.pack()
        self.board.pack()
        self.HitBtn.pack()
        self.StayBtn.pack()
        self.BetBtn.pack()
        self.ResBtn.pack()
        self.DealBtn.place(bordermode=tk.OUTSIDE, height = 30, width = 50, x= 600+offset, y =300)
        self.BetBtn.place(bordermode=tk.OUTSIDE, height=30, width=70, x = 520+offset, y = 300)
        self.HitBtn.place(bordermode=tk.OUTSIDE, height=30, width=50, x = 660+offset, y = 300)
        self.StayBtn.place(bordermode=tk.OUTSIDE, height=30, width=50, x = 720+offset, y = 300)
        self.ResBtn.place(bordermode=tk.OUTSIDE, height=30, width=70, x = 780+offset, y = 300)
        self.ePlayerMoney.pack()

    def Bet(self):        
        self.betval = self.betval + 10
        self.p_Money = self.p_Money - 10
        
        self.ePlayerMoney.delete(0, tk.END)
        self.ePlayerMoney.insert(0, "Player: " + str(self.p_Money))
        if self.p_Money <= 0:
            self.BetBtn.config(state = 'disabled')
            
        self.board.delete(self.betdisplay)    
        self.betdisplay = self.board.create_text(55,300, text ="Bet: $" + str(self.betval), font = ('Arial',15))

    def Draw_Card(self, card_num, pos_x, pos_y):
        self.card_image = tk.PhotoImage(file=(Pic_file_path + file_list[card_num]) )
        self.l_card = self.board.create_image(pos_x,pos_y, anchor = tk.NW, image=self.card_image)
        self.list_card.append(self.l_card)
        self.list_image.append(self.card_image)
        self.board.update()

    def Deal(self):
        global deck, list_Comp, list_You
        card_x = self.start_card_x
        
        self.BetBtn.config(state = 'disabled')
        self.DealBtn.config(state = 'disabled')
        self.House_secret = deck.pop(0)
        list_Comp.append(self.House_secret)
        self.Draw_Card(0, card_x, 42)
                
        temp_Comp = deck.pop(0)
        list_Comp.append(temp_Comp)
        self.Draw_Card(temp_Comp, card_x+85, 42)
        
        temp_You = deck.pop(0)
        list_You.append(temp_You)
        self.Draw_Card(temp_You, card_x, 255)
            
        temp_You = deck.pop(0)
        list_You.append(temp_You)
        self.Draw_Card(temp_You, card_x+85, 255)
        self.board.update()

        self.Check_blackjack_bust()

    def Hit(self):
        global deck, list_Comp, list_You
        self.hit_cnt = self.hit_cnt + 1
        t_card = deck.pop(0)
        list_You.append(t_card)        
        self.Draw_Card(t_card, (self.start_card_x + 85 + 85*self.hit_cnt), 255)
        self.Check_blackjack_bust()

    def Hit_Comp(self):
        global deck, list_Comp
        self.hit_cnt = 0
        self.hit_cnt = self.hit_cnt + 1
        x_card = deck.pop(0)
        list_Comp.append(x_card)
        self.Draw_Card(x_card, (self.start_card_x + 85 + 85*self.hit_cnt), 42)        

    def Stay(self):
        self.HitBtn.config(state = 'disabled')
        self.Draw_Card(self.House_secret, self.start_card_x, 42)
        isDone = self.Check_blackjack_bust()

        #step 1, if PC already BlackJack or bust, then exit
        if isDone:
            return

        #step 2: if PC <17, keep hit pc, while check BlackJack/bust
        while self.comp_total < 17:
            self.Hit_Comp()
            isDone = self.Check_blackjack_bust()
            if isDone:
                return
            time.sleep(1)

        #step 3: now PC>=17, but <21, do final judge
        self.Finaljudge() 

    # expect three result, 1=PC win, 2=Player win BlackJack, 3=Player win normal, 0=tie
    def Roundover(self, result):
        global list_Comp, list_You
        print "list_house_card", list_Comp
        print "list_you_card", list_You
        print "list_you_val, and total", self.list_you_val, self.you_total
        print "list_c_val, and total", self.list_comp_val, self.comp_total

        if result == 'TIE':
            self.p_Money = self.betval + self.p_Money
            print result+"PUSH."
            self.board.create_text(800,350, text='TIE! PUSH.', font=('Helvetica', 30)) 

        elif result == 'HOUSE_BLACK_JACK':
            self.HouseMoney = self.betval + self.HouseMoney
            print result
            self.board.create_text(800,350, text='HOUSE_BLACK_JACK, YOU LOSE!!', font=('Helvetica', 30)) 

        elif result == 'PLAY_BLACK_JACK':
            self.p_Money = (2.5*self.betval) + self.p_Money
            self.HouseMoney = self.HouseMoney - (1.5*self.betval)
            print result
            self.board.create_text(800,350, text='PLAY_BLACK_JACK, YOU WIN!!', font=('Helvetica', 30)) 

        elif result == 'PLAY_BUST':
            self.HouseMoney = self.betval + self.HouseMoney
            print result
            self.board.create_text(800,350, text='PLAY_BUST, YOU LOSE!!', font=('Helvetica', 30)) 

        elif result == 'HOUSE_BUST':
            self.p_Money = self.p_Money + (2*self.betval)
            self.HouseMoney = self.HouseMoney - self.betval
            print result
            self.board.create_text(800, 350, text='HOUSE_BUST, YOU WIN!!', font=('Helvetica', 30)) 

        elif result == 'PLAY_WIN_NORMAL':
            self.p_Money = self.p_Money + (2*self.betval)
            self.HouseMoney = self.HouseMoney - self.betval
            print result
            self.board.create_text(800, 350, text='YOU WIN!!', font=('Helvetica', 30)) 

        elif result == 'HOUSE_WIN_NORMAL':
            self.HouseMoney = self.betval + self.HouseMoney
            print result
            self.board.create_text(800, 350, text='YOU LOST!!', font=('Helvetica', 30))

        else:
            print "ERR: don't understand ", result

        #update money, take out bet_val
        self.betval = 0
        self.ePlayerMoney.delete(0, tk.END)
        self.eHouseMoney.delete(0, tk.END)
        self.ePlayerMoney.insert(0, "Player: " + str(self.p_Money))
        self.eHouseMoney.insert(0, "House: " + str(self.HouseMoney))
        #Round is over, disable buttons
        self.BetBtn.config(state = 'disabled')
        self.DealBtn.config(state = 'disabled')
        self.HitBtn.config(state = 'disabled')
        self.StayBtn.config(state = 'disabled')

    def Check_blackjack_bust(self): 
        self.Convert_hand(True)
        self.Calc_hand()

        # check for the win, BlackJack
        if self.you_total == 21 and self.comp_total < 21:
            self.Roundover('PLAY_BLACK_JACK')
            return True
            
        elif self.you_total > 21:
            #Computer wins because you busted
            self.Roundover('PLAY_BUST')
            return True

        elif self.comp_total == 21 and self.you_total < 21:
            #Computer gets BlackJack, flip card
            self.Draw_Card(self.House_secret, self.start_card_x, 42)           
            self.Roundover('HOUSE_BLACK_JACK')
            return True

        # Not blackjack or bust yet
        else:
            return False

    def Finaljudge(self):
        self.Draw_Card(self.House_secret, self.start_card_x, 42)

        if self.comp_total > 21 and self.you_total <= 21:
            #Computer busted            
            self.Roundover('HOUSE_BUST')

        elif self.you_total < self.comp_total:
            self.Roundover('HOUSE_WIN_NORMAL')
            
        elif self.you_total > self.comp_total:
            self.Roundover('PLAY_WIN_NORMAL')      

        elif self.you_total == self.comp_total:
            self.Roundover('TIE')            

        else:
            print "MISSED SOMETHING"

    #take in card number, return Blackjack value of card
    def Convert_card(self, c_number, isUseAasA):
        aa = c_number % 13
        if aa == 0:
            return 10
        elif aa >= 10:
            return 10
        elif aa >= 2 and aa <=9:
            return aa
        # let take care A:    
        if isUseAasA == True:
            return 11
        else: 
            return 1

    def Convert_hand(self, isUseAasA):
        global list_Comp, list_You
        self.list_you_val = []
        self.list_comp_val = []
        for item in list_You:
            xx = self.Convert_card(item, isUseAasA)
            self.list_you_val.append(xx)
        for item in list_Comp:
            yy = self.Convert_card(item, isUseAasA)
            self.list_comp_val.append(yy)    
    
    def Calc_hand(self):
        self.comp_total = 0
        self.you_total = 0
        for item in self.list_you_val:
            self.you_total = self.you_total + item
        for item in self.list_comp_val:
            self.comp_total = self.comp_total + item
            
    def Res(self):
        global list_You, list_Comp
        self.hit_cnt = 0            
        self.HitBtn.config(state = 'normal')
        self.DealBtn.config(state = 'normal')
        self.StayBtn.config(state = 'normal')
        self.BetBtn.config(state = 'normal')

        # clear picture
        for item in self.list_image:
            self.board.delete(item)
        for item in self.list_card:
            self.board.delete(item)

        # clear money
        self.betval = 0    
        list_You = []
        list_Comp = []
        self.list_you_val = []
        self.list_comp_val = []
        self.list_card = []
        self.list_image = []


    def quit(self):
        sys.exit()        

if __name__ == "__main__":
    root = tk.Tk() 
    BlackJack(root).pack(side="top", fill="both", expand=True)

    BlackJack.p_Money = 200   
    root.mainloop()
