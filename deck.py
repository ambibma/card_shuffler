from tkinter import *

root = Tk()
root.title('Cards')
# root.icontbitmap('~/projects/cards')
root.geometry('900x500')
root.configure(background='green')


my_frame= Frame(root, bg='green')
my_frame.pack(pady=20)

# Create Frames for Cards

dealer_frame = LabelFrame(my_frame, text='Dealer', bd=0)
dealer_frame.grid(row=0, column=0, padx=20, ipadx=20)

player_frame = LabelFrame(my_frame, text= 'Player', bd=0)
player_frame.grid(row=0, column=0, ipadx=20)


#put cards in frame

dealer_label = Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = Label(player_frame, text='')
player_label.pack(pady=20)

#Create buttons
shuffle_button = Button(root, text="Shuffle Deck", font=("Helvetica", 14))
shuffle_button.pack(pady=20)

card_button = Button(root, text="Get Cards", font=("Helvetica", 14))
card_button.pack(pady=20)

root.mainloop()