from tkinter import *
import random

root = Tk()
root.title('Cards')
# root.icontbitmap('~/projects/cards')
root.geometry('900x500')
root.configure(background='green')

#shuffle the cards

def shuffle():
  #Define deck
  suits = ["diamonds", "clubs", "hearts", "spades"]
  values = range(2, 15)
  #11 = jack, 12=Queen, 13, Kings, 14 = Ace
  
  global deck
  deck = []
  
  for suit in suits:
    for value in values:
      deck.append(f'{value}_of_{suit}')
  

  
  #Create players
  
  global dealer, player
  dealer= []
  player = []
  
  #Grab a random Card
  
  card = random.choice(deck)
  #Remove Card from Deck
  deck.remove(card)
  #Append Card to Dealer List
  dealer.append(card)
  #output Card to Screen
  dealer_label.config(text=card)
  
  card = random.choice(deck)
  #Remove Card from Deck
  deck.remove(card)
  #Append Card to Dealer List
  player.append(card)
  #output Card to Screen
  player_label.config(text=card)
  
  root.title(f'Cards -{len(deck)}')

#Deal out cards
def deal_cards():
  try:
    # Get the Dealer Card
    card = random.choice(deck)
    #Remove Card from Deck
    deck.remove(card)
    #Append Card to Dealer List
    dealer.append(card)
    #output Card to Screen
    dealer_label.config(text=card)
  
    #Get the player card
    card = random.choice(deck)
    #Remove Card from Deck
    deck.remove(card)
    #Append Card to Dealer List
    player.append(card)
    #output Card to Screen
    player_label.config(text=card)
    
    root.title(f'Cards -{len(deck)}')
  
  except:
     root.title(f'Cards - No Cards in Deck')


my_frame= Frame(root, bg='green')
my_frame.pack(pady=20)

# Create Frames for Cards

dealer_frame = LabelFrame(my_frame, text='Dealer', bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text= 'Player', bd=0)
player_frame.grid(row=0, column=1, ipadx=20)


#put cards in frame
dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

#Create buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14), command=shuffle)
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14), command =deal_cards)
card_button.pack(pady=20)

root.mainloop()