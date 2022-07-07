# Final Culminating
# Instructions
# Samantha Mac
# ICS2O1

import tkinter

def show_instruction():
    # Main window
    instruction_window = tkinter.Tk()
    instruction_window.title('Sam\'s Cua Cá Cọp Setup')
    # Setup frame
    instruction_window_frame = tkinter.Frame(instruction_window)
    instruction_window_frame.pack(padx=40, pady=(20,0))

    # HEADER FRAME
    title_frame = tkinter.Frame(instruction_window_frame)
    title_frame.pack()
    # Title
    title_label = tkinter.Label(title_frame, text='Sam\'s Cua Cá Cọp Instructions',\
                                fg='#c92e20', font='-weight bold -size 24')
    # Pack
    title_label.pack()

    
    # INSTRUCTIONS FRAME
    instruction_text_frame = tkinter.Frame(instruction_window_frame)
    instruction_text_frame.pack(pady=15)

    # Instructions
    instruction_text = tkinter.StringVar(instruction_text_frame)
    # Concatenate w/ line breaks
    instruction_text.set('Welcome to Sam\'s Cua Cá Cọp! This game is a modification of Bầu Cua Cá Cọp,' + '\n' +
                          'a traditional Vietnamese game played during têt (Vietnamese New Year). The' + '\n' +
                          'game board is divided in six sections symbolic to Vietnam: Water Buffalo,' + '\n' +
                          'Lotus, Pho, Coffee, Rice, and Wine Jug. Get ready for a game of fun :D' + '\n\n' +
                          '⭐️ Objective ⭐' + '\n' +
                          'Have a higher balance than the dealer and stay out of debt' + '\n\n' +
                          '🎲️ How To Play 🎲️' + '\n' +
                          '1. You will be given 10 tokens to begin.' + '\n' +
                          '2. At the start of each round, you may place a bet of any amount (within your' + '\n' +
                          'balance) on any number of the six sections.' + '\n' +
                          '3. Two number dice will be rolled. Each number corresponds to a symbol.' + '\n' +
                          '4. If a die lands on a section you betted on, you earn back twice your original ' + '\n' +
                          'bet.' + '\n' +
                          '5. If two dice land on a section you betted on, you earn back three times your ' + '\n' +
                          'original bet.' + '\n' +
                          '6. Losing bets are collected by the dealer. Winning bets are deducted from the dealer.' + '\n\n' +
                          '🧧 Lucky Die 🧧' + '\n' +
                          'The lucky die has add-ons that can affect your balance.' + '\n' +
                          '• Tax Police: 50% of your earnings in that round are deducted.' + '\n' +
                          '• Red Pocket: Your earnings in that round are doubled' + '\n' +
                          '• Cha-ching: You earn 5 tokens.' + '\n' +
                          '• Robbery: You lose 2 tokens.')

    instruction_label = tkinter.Label(instruction_text_frame, textvariable=instruction_text, justify='left')
    # Pack
    instruction_label.pack()

    # BUTTON FRAME
    button_frame = tkinter.Frame(instruction_window_frame)
    button_frame.pack(anchor='w', pady=25)
    
    # Buttons
    back_button = tkinter.Button(button_frame, text='Back', command=instruction_window.destroy)
    # Pack buttons
    back_button.pack(side='left')

    # Main loop
    tkinter.mainloop()
