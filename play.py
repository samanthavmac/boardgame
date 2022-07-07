# Final Culminating
# Start Game
# Samantha Mac
# ICS2O1

import modules
import instructions
import tkinter
import tkinter.messagebox
import random

# Set strvar values to nothing
p_message = ''
die1_icon = '❔'
die1_outcome = ''
die2_icon = '❔'
die2_outcome = ''
die3_icon = '❔'
die3_outcome = ''
earning1 = ''
earning2 = ''

# Main function
def main():
    # Main window
    game_window = tkinter.Tk()
    game_window.title('Sam\'s Cua Cá Cọp Gameplay')
    # Main frame
    main_game_frame = tkinter.Frame(game_window)
    main_game_frame.pack(padx=40, pady=(20,0))

    ##
    # HEADER FRAME
    title_frame = tkinter.Frame(main_game_frame)
    title_frame.pack()
    # Title
    title_label = tkinter.Label(title_frame, text=('Sam\'s Cua Cá Cọp'),\
                                fg='#c92e20', font='-weight bold -size 32')

    # Button frame
    button_frame = tkinter.Frame(main_game_frame)
    button_frame.pack()
    # Buttons
    instruction_button = tkinter.Button(button_frame, text='How To Play', \
                                        command=instructions.show_instruction)
    quit_button = tkinter.Button(button_frame, text='Quit', \
                                 command=game_window.destroy)
    # Pack widgets
    title_label.pack()
    instruction_button.pack(side='left')
    quit_button.pack(side='left')

    ##   
    # SCORE FRAME
    score_frame = tkinter.Frame(main_game_frame)
    score_frame.pack(pady=(10,0))

    # Define starting balances
    p_balance = 10 # player
    d_balance = 25 # dealer

    # Player score
    player_frame = tkinter.Frame(score_frame)
    player_frame.pack(anchor='w', side='left')
    # Player score strvar
    p_balance_str = tkinter.StringVar(main_game_frame)
    p_balance_str.set(p_balance)
    # Message to update player strvar
    p_message_str = tkinter.StringVar(main_game_frame)
    p_message_str.set(p_message)
    # Player labels
    p_label = tkinter.Label(player_frame, text='🪙 Your Balance: ', \
                            font='-weight bold')
    p_score = tkinter.Label(player_frame, textvariable=p_balance_str, \
                            borderwidth=0.5, relief='solid', height=2, width=9)
    update_p = tkinter.Label(main_game_frame, textvariable=p_message_str)
    
    # Dealer score
    dealer_frame = tkinter.Frame(score_frame)
    dealer_frame.pack(anchor='w', side='left', padx=(10,0))
    # Dealer score strvar
    d_balance_str = tkinter.StringVar(main_game_frame)
    d_balance_str.set(d_balance)
    # Dealer labels
    d_label = tkinter.Label(dealer_frame, text='💰 Dealer\'s Balance: ', \
                            font='-weight bold')
    d_score = tkinter.Label(dealer_frame, textvariable=d_balance_str, \
                            borderwidth=0.5, relief='solid', height=2, width=9)

    # Pack widgets
    # Player
    p_label.pack(anchor='w', side='left')
    p_score.pack(side='left')
    update_p.pack()
    # Dealer
    d_label.pack(anchor='w', side='left')
    d_score.pack(side='left')


    ##
    # MIDDLE FRAME
    middle_frame = tkinter.Frame(main_game_frame)
    middle_frame.pack(pady=(20,0))
    # Left Frame
    col1 = tkinter.Frame(middle_frame)
    col1.pack(anchor='nw', side='left', padx=(0,20))
    # Right Frame
    col2 = tkinter.Frame(middle_frame)
    col2.pack(anchor='nw', side='left')

    ##
    # RB VALUE SELECTION
    # Selection frame
    selection_frame = tkinter.Frame(col1)
    selection_frame.pack()

    # Header
    selection_header = tkinter.Label(selection_frame, \
                                     text='Decide Your Fate', \
                                     font='-weight bold -size 18')
    selection_text = tkinter.Label(selection_frame, \
                                   text='Assign a die value to each section.\n')
    # Pack
    selection_header.pack(anchor='w')
    selection_text.pack(anchor='w')

    # Organize rbs into rows of 3
    # Row 1
    row1 = tkinter.Frame(selection_frame)
    row1.pack(anchor='w', pady=(0,10))
    # Row 2
    row2 = tkinter.Frame(selection_frame)
    row2.pack(anchor='w')

    # BUFFALO SELECT
    # Frame
    buffalo_select_frame = tkinter.Frame(row1, width=10)
    buffalo_select_frame.pack(anchor='w', side='left', padx=(0,20))
    # Header
    buffalo_select_label = tkinter.Label(buffalo_select_frame, text='Water Buffalo', \
                                         font='-weight bold', width=10, anchor='w')
    # Pack
    buffalo_select_label.pack()
    # Radio button variable
    buffalo_rb_value = tkinter.IntVar()
    buffalo_rb_value.set(1)
    # Radio buttons
    buffalo_rb1 = tkinter.Radiobutton(buffalo_select_frame, \
                                      text='1', variable=buffalo_rb_value, value=1)
    buffalo_rb2 = tkinter.Radiobutton(buffalo_select_frame, \
                                      text='2', variable=buffalo_rb_value, value=2)
    buffalo_rb3 = tkinter.Radiobutton(buffalo_select_frame, \
                                      text='3', variable=buffalo_rb_value, value=3)
    buffalo_rb4 = tkinter.Radiobutton(buffalo_select_frame, \
                                      text='4', variable=buffalo_rb_value, value=4)
    buffalo_rb5 = tkinter.Radiobutton(buffalo_select_frame, \
                                      text='5', variable=buffalo_rb_value, value=5)
    buffalo_rb6 = tkinter.Radiobutton(buffalo_select_frame, \
                                      text='6', variable=buffalo_rb_value, value=6)
    # Pack buttons
    buffalo_rb1.pack(anchor='w')
    buffalo_rb2.pack(anchor='w')
    buffalo_rb3.pack(anchor='w')
    buffalo_rb4.pack(anchor='w')
    buffalo_rb5.pack(anchor='w')
    buffalo_rb6.pack(anchor='w')

    # LOTUS SELECT
    # Frame
    lotus_select_frame = tkinter.Frame(row1)
    lotus_select_frame.pack(anchor='w', side='left', padx=(0,20))
    # Header
    lotus_select_label = tkinter.Label(lotus_select_frame, text='Lotus', \
                                       font='-weight bold', width=5, anchor='w')
    # Pack
    lotus_select_label.pack(anchor='w')
    # Radio button variable
    lotus_rb_value = tkinter.IntVar()
    lotus_rb_value.set(2)
    # Radio buttons
    lotus_rb1 = tkinter.Radiobutton(lotus_select_frame, \
                                    text='1', variable=lotus_rb_value, value=1)
    lotus_rb2 = tkinter.Radiobutton(lotus_select_frame, \
                                    text='2', variable=lotus_rb_value, value=2)
    lotus_rb3 = tkinter.Radiobutton(lotus_select_frame, \
                                    text='3', variable=lotus_rb_value, value=3)
    lotus_rb4 = tkinter.Radiobutton(lotus_select_frame, \
                                    text='4', variable=lotus_rb_value, value=4)
    lotus_rb5 = tkinter.Radiobutton(lotus_select_frame, \
                                    text='5', variable=lotus_rb_value, value=5)
    lotus_rb6 = tkinter.Radiobutton(lotus_select_frame, \
                                    text='6', variable=lotus_rb_value, value=6)
    # Pack buttons
    lotus_rb1.pack(anchor='w')
    lotus_rb2.pack(anchor='w')
    lotus_rb3.pack(anchor='w')
    lotus_rb4.pack(anchor='w')
    lotus_rb5.pack(anchor='w')
    lotus_rb6.pack(anchor='w')

    # PHO SELECT
    # Frame
    pho_select_frame = tkinter.Frame(row1)
    pho_select_frame.pack(anchor='w', side='left', padx=(0,20))
    # Header
    pho_select_label = tkinter.Label(pho_select_frame, text='Pho', font='-weight bold')
    # Pack
    pho_select_label.pack(anchor='w')
    # Radio button variable
    pho_rb_value = tkinter.IntVar()
    pho_rb_value.set(3)
    # Radio buttons
    pho_rb1 = tkinter.Radiobutton(pho_select_frame, \
                                  text='1', variable=pho_rb_value, value=1)
    pho_rb2 = tkinter.Radiobutton(pho_select_frame, \
                                  text='2', variable=pho_rb_value, value=2)
    pho_rb3 = tkinter.Radiobutton(pho_select_frame, \
                                  text='3', variable=pho_rb_value, value=3)
    pho_rb4 = tkinter.Radiobutton(pho_select_frame, \
                                  text='4', variable=pho_rb_value, value=4)
    pho_rb5 = tkinter.Radiobutton(pho_select_frame, \
                                  text='5', variable=pho_rb_value, value=5)
    pho_rb6 = tkinter.Radiobutton(pho_select_frame, \
                                  text='6', variable=pho_rb_value, value=6)
    # Pack buttons
    pho_rb1.pack(anchor='w')
    pho_rb2.pack(anchor='w')
    pho_rb3.pack(anchor='w')
    pho_rb4.pack(anchor='w')
    pho_rb5.pack(anchor='w')
    pho_rb6.pack(anchor='w')

    # COFFEE SELECT
    # Frame
    coffee_select_frame = tkinter.Frame(row2)
    coffee_select_frame.pack(anchor='w', side='left', padx=(0,20))
    # Header
    coffee_select_label = tkinter.Label(coffee_select_frame, text='Coffee',\
                                        font='-weight bold', width=10, anchor='w')
    # Pack
    coffee_select_label.pack(anchor='w')
    # Radio button variable
    coffee_rb_value = tkinter.IntVar()
    coffee_rb_value.set(4)
    # Radio buttons
    coffee_rb1 = tkinter.Radiobutton(coffee_select_frame, \
                                     text='1', variable=coffee_rb_value, value=1)
    coffee_rb2 = tkinter.Radiobutton(coffee_select_frame, \
                                     text='2', variable=coffee_rb_value, value=2)
    coffee_rb3 = tkinter.Radiobutton(coffee_select_frame, \
                                     text='3', variable=coffee_rb_value, value=3)
    coffee_rb4 = tkinter.Radiobutton(coffee_select_frame, \
                                     text='4', variable=coffee_rb_value, value=4)
    coffee_rb5 = tkinter.Radiobutton(coffee_select_frame, \
                                     text='5', variable=coffee_rb_value, value=5)
    coffee_rb6 = tkinter.Radiobutton(coffee_select_frame, \
                                     text='6', variable=coffee_rb_value, value=6)
    # Pack buttons
    coffee_rb1.pack(anchor='w')
    coffee_rb2.pack(anchor='w')
    coffee_rb3.pack(anchor='w')
    coffee_rb4.pack(anchor='w')
    coffee_rb5.pack(anchor='w')
    coffee_rb6.pack(anchor='w')

    # RICE SELECT
    # Frame
    rice_select_frame = tkinter.Frame(row2)
    rice_select_frame.pack(anchor='w', side='left', padx=(0,20))
    # Header
    rice_select_label = tkinter.Label(rice_select_frame, text='Rice', \
                                      font='-weight bold', width=5, anchor='w')
    # Pack
    rice_select_label.pack(anchor='w')
    # Radio button variable
    rice_rb_value = tkinter.IntVar()
    rice_rb_value.set(5)
    # Radio buttons
    rice_rb1 = tkinter.Radiobutton(rice_select_frame, \
                                   text='1', variable=rice_rb_value, value=1)
    rice_rb2 = tkinter.Radiobutton(rice_select_frame, \
                                   text='2', variable=rice_rb_value, value=2)
    rice_rb3 = tkinter.Radiobutton(rice_select_frame, \
                                   text='3', variable=rice_rb_value, value=3)
    rice_rb4 = tkinter.Radiobutton(rice_select_frame, \
                                   text='4', variable=rice_rb_value, value=4)
    rice_rb5 = tkinter.Radiobutton(rice_select_frame, \
                                   text='5', variable=rice_rb_value, value=5)
    rice_rb6 = tkinter.Radiobutton(rice_select_frame, \
                                   text='6', variable=rice_rb_value, value=6)
    # Pack buttons
    rice_rb1.pack(anchor='w')
    rice_rb2.pack(anchor='w')
    rice_rb3.pack(anchor='w')
    rice_rb4.pack(anchor='w')
    rice_rb5.pack(anchor='w')
    rice_rb6.pack(anchor='w')

    # WINE SELECT
    # Frame
    wine_select_frame = tkinter.Frame(row2)
    wine_select_frame.pack(anchor='w', side='left', padx=(0,20))
    # Header
    wine_select_label = tkinter.Label(wine_select_frame, \
                                      text='Wine Jug', font='-weight bold')
    # Pack
    wine_select_label.pack(anchor='w')
    # Radio button variable
    wine_rb_value = tkinter.IntVar()
    wine_rb_value.set(6)
    # Radio buttons
    wine_rb1 = tkinter.Radiobutton(wine_select_frame, \
                                   text='1', variable=wine_rb_value, value=1)
    wine_rb2 = tkinter.Radiobutton(wine_select_frame, \
                                   text='2', variable=wine_rb_value, value=2)
    wine_rb3 = tkinter.Radiobutton(wine_select_frame, \
                                   text='3', variable=wine_rb_value, value=3)
    wine_rb4 = tkinter.Radiobutton(wine_select_frame, \
                                   text='4', variable=wine_rb_value, value=4)
    wine_rb5 = tkinter.Radiobutton(wine_select_frame, \
                                   text='5', variable=wine_rb_value, value=5)
    wine_rb6 = tkinter.Radiobutton(wine_select_frame, \
                                   text='6', variable=wine_rb_value, value=6)
    # Pack buttons
    wine_rb1.pack(anchor='w')
    wine_rb2.pack(anchor='w')
    wine_rb3.pack(anchor='w')
    wine_rb4.pack(anchor='w')
    wine_rb5.pack(anchor='w')
    wine_rb6.pack(anchor='w')


    ##
    # BOARD
    # Main board frame
    board_frame = tkinter.Frame(col2)
    board_frame.pack(anchor='nw')

    # Labels
    board_header = tkinter.Label(board_frame, \
                                 text='Gameboard', font='-weight bold -size 18')
    board_text = tkinter.Label(board_frame, \
                               text=('Place your bet (integer value) in each field.' +
                               'To place no bet, enter 0.\n'))
    # Pack
    board_header.pack(anchor='w')
    board_text.pack(anchor='w')

    # Rows
    row1 = tkinter.Frame(board_frame)
    row2 = tkinter.Frame(board_frame)
    # Pack rows
    row1.pack()
    row2.pack()

    # Board sections/squares
    buffalo_frame = tkinter.Frame(row1, width=50, height=50, \
                                  borderwidth=0.5, relief='solid', bg='#0db895')
    lotus_frame = tkinter.Frame(row1, width=50, height=50, \
                                borderwidth=0.5, relief='solid', bg='#320db8')
    pho_frame = tkinter.Frame(row1, width=50, height=50, \
                              borderwidth=0.5, relief='solid', bg='#b8790d')
    coffee_frame = tkinter.Frame(row2, width=50, height=50, \
                                 borderwidth=0.5, relief='solid', bg='#b8320d')
    rice_frame = tkinter.Frame(row2, width=50, height=50, \
                               borderwidth=0.5, relief='solid', bg='#7fb80d')
    wine_frame = tkinter.Frame(row2, width=50, height=50, \
                               borderwidth=0.5, relief='solid', bg='#0d8db8')
    # Pack
    buffalo_frame.pack(side='left')
    lotus_frame.pack(side='left')
    pho_frame.pack(side='left')
    coffee_frame.pack(side='left')
    rice_frame.pack(side='left')
    wine_frame.pack(side='left')

    # Section con labels
    buffalo_icon = tkinter.Label(buffalo_frame, text='🐃', \
                                 font='-size 40', bg='#0db895')
    lotus_icon = tkinter.Label(lotus_frame, text='🪷', \
                               font='-size 40', bg='#320db8')
    pho_icon = tkinter.Label(pho_frame, text='🍜', \
                             font='-size 40', bg='#b8790d')
    coffee_icon = tkinter.Label(coffee_frame, text='☕️', \
                                font='-size 40', bg='#b8320d')
    rice_icon = tkinter.Label(rice_frame, text='🍚', \
                              font='-size 40', bg='#7fb80d')
    wine_icon = tkinter.Label(wine_frame, text='🍶', \
                              font='-size 40', bg='#0d8db8')
    # Pack icons
    buffalo_icon.pack(pady=(20,0))
    lotus_icon.pack(pady=(20,0))
    pho_icon.pack(pady=(20,0))
    coffee_icon.pack(pady=(20,0))
    rice_icon.pack(pady=(20,0))
    wine_icon.pack(pady=(20,0))

    # Section headers
    buffalo_title = tkinter.Label(buffalo_frame, text='Water Buffalo', \
                                  font='-weight bold -size 20', \
                                  fg='white', bg='#0db895')
    lotus_title = tkinter.Label(lotus_frame, text='Lotus', \
                                font='-weight bold -size 20', \
                                fg='white', bg='#320db8')
    pho_title = tkinter.Label(pho_frame, text='Pho', \
                              font='-weight bold -size 20', \
                              fg='white', bg='#b8790d')
    coffee_title = tkinter.Label(coffee_frame, text='Coffee', \
                                 font='-weight bold -size 20', \
                                 fg='white', bg='#b8320d')
    rice_title = tkinter.Label(rice_frame, text='Rice', \
                               font='-weight bold -size 20', \
                               fg='white', bg='#7fb80d')
    wine_title = tkinter.Label(wine_frame, text='Wine Jug', \
                               font='-weight bold -size 20', \
                               fg='white', bg='#0d8db8')
    # Pack headers
    buffalo_title.pack()
    lotus_title.pack()
    pho_title.pack()
    coffee_title.pack()
    rice_title.pack()
    wine_title.pack()

    # Section entries
    buffalo_entry = tkinter.Entry(buffalo_frame, width=10)
    lotus_entry = tkinter.Entry(lotus_frame, width=10)
    pho_entry = tkinter.Entry(pho_frame, width=10)
    coffee_entry = tkinter.Entry(coffee_frame, width=10)
    rice_entry = tkinter.Entry(rice_frame, width=10)
    wine_entry = tkinter.Entry(wine_frame, width=10)
    # Pack entries
    buffalo_entry.pack(padx=30, pady=(5,35))
    lotus_entry.pack(padx=30, pady=(5,35))
    pho_entry.pack(padx=30, pady=(5,35))
    coffee_entry.pack(padx=30, pady=(5,35))
    rice_entry.pack(padx=30, pady=(5,35))
    wine_entry.pack(padx=30, pady=(5,35))

    ##
    # OUTCOME FRAME
    outcome_frame = tkinter.Frame(main_game_frame)
    outcome_frame.pack(anchor='w', pady=(30))
    # Header
    outcome_title = tkinter.Label(outcome_frame, \
                                  text='Outcome for Last Round', \
                                  font='-weight bold -size 18')
    outcome_title.pack(anchor='w', pady=(0,20))
    # Create a row to place only dice
    # outcomes side by side
    outcome_row = tkinter.Frame(outcome_frame)
    outcome_row.pack()
    
    # DIE 1 OUTCOME
    die1_frame = tkinter.Frame(outcome_row, borderwidth=1, relief='solid')
    die1_frame.pack(side='left', padx=(0,20))
    # Strvars
    die1_icon_str = tkinter.StringVar(die1_frame)
    die1_icon_str.set(die1_icon)
    die1_str = tkinter.StringVar(die1_frame)
    die1_str.set(die1_outcome)
    # Label
    die1_icon_display = tkinter.Label(die1_frame, \
                                      textvariable=die1_icon_str, font='-size 80')
    die1_display = tkinter.Label(die1_frame, \
                                 textvariable=die1_str, font='-size 18')
    # Pack
    die1_icon_display.pack(padx=30)
    die1_display.pack(pady=(0,15))

    # DIE 2 OUTCOME
    die2_frame = tkinter.Frame(outcome_row, borderwidth=1, relief='solid')
    die2_frame.pack(side='left', padx=(0,20))
    # Strvars
    die2_icon_str = tkinter.StringVar(die2_frame)
    die2_icon_str.set(die2_icon)
    die2_str = tkinter.StringVar(die2_frame)
    die2_str.set(die2_outcome)
    # Label
    die2_icon_display = tkinter.Label(die2_frame, \
                                      textvariable=die2_icon_str, font='-size 80')
    die2_display = tkinter.Label(die2_frame, \
                                 textvariable=die2_str, font='-size 18')
    # Pack
    die2_icon_display.pack(padx=30)
    die2_display.pack(pady=(0,15))
    
    # DIE 3 OUTCOME
    die3_frame = tkinter.Frame(outcome_row, borderwidth=1, relief='solid')
    die3_frame.pack(side='left')
    # Strvars
    die3_icon_str = tkinter.StringVar(die3_frame)
    die3_icon_str.set(die3_icon)
    die3_str = tkinter.StringVar(die3_frame)
    die3_str.set(die3_outcome)
    # Label
    die3_icon_display = tkinter.Label(die3_frame, \
                                      textvariable=die3_icon_str, font='-size 80')
    die3_display = tkinter.Label(die3_frame, \
                                 textvariable=die3_str, font='-size 18')
    # Pack
    die3_icon_display.pack(padx=40)
    die3_display.pack(pady=(0,15), padx=20)

    # EARNINGS 
    earning_frame = tkinter.Frame(outcome_row)
    earning_frame.pack(side='left', padx=(15,0))
    
    # Individual frames to stack labels
    # Earnings (before lucky die) display
    earning1_frame = tkinter.Frame(earning_frame)
    earning1_frame.pack(padx=(15,0), anchor='w')
    # Strvars
    earning1_str = tkinter.StringVar(earning1_frame)
    earning1_str.set(earning1)
    # Labels
    earning1_label = tkinter.Label(earning1_frame, text='Earnings: ')
    earning1_display = tkinter.Label(earning1_frame, \
                                     textvariable=earning1_str)
    # Pack labels
    earning1_label.pack(side='left', anchor='w')
    earning1_display.pack(anchor='w', side='left')
    
    
    # Earnings (after lucky die) display
    earning2_frame = tkinter.Frame(earning_frame)
    earning2_frame.pack(padx=(15,0), anchor='w')
    # Strvars
    earning2_str = tkinter.StringVar(earning2_frame)
    earning2_str.set(earning2)
    # Labels
    earning2_label = tkinter.Label(earning2_frame, \
                                   text='Earnings (with Lucky die): ')
    earning2_display = tkinter.Label(earning2_frame, \
                                     textvariable=earning2_str)
    # Pack labels
    earning2_label.pack(side='left', anchor='w')
    earning2_display.pack(anchor='w', side='left')    

    # BUTTON COMMAND / CALCULATIONS
    def roll_die():
        # Must use to access var in
        # inner function
        nonlocal p_balance
        nonlocal d_balance

        # VALUE RETRIEVAL
        # Assign rb values to var
        # to solve scope issues
        buffalo_num = buffalo_rb_value.get()
        lotus_num = lotus_rb_value.get()
        pho_num = pho_rb_value.get()
        coffee_num = coffee_rb_value.get()
        rice_num = rice_rb_value.get()
        wine_num = wine_rb_value.get()
        # Convert entries to int
        buffalo_bet = int(buffalo_entry.get())
        lotus_bet = int(lotus_entry.get())
        pho_bet = int(pho_entry.get())
        coffee_bet = int(coffee_entry.get())
        rice_bet = int(rice_entry.get())
        wine_bet = int(wine_entry.get())
        
        # ROLL THREE DICE
        # Select random int
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,7)

        # VALIDATIONS
        # Validate die values
        # Sections can not have same die values
        if ((buffalo_num == lotus_num) or (buffalo_num == pho_num)\
            or (buffalo_num == coffee_num) or (buffalo_num == rice_num)\
            or (buffalo_num == wine_num) or (lotus_num == pho_num)\
            or (lotus_num == coffee_num) or (lotus_num == rice_num)\
            or (lotus_num == wine_num) or (pho_num == coffee_num)\
            or (pho_num == rice_num) or (pho_num == wine_num)\
            or (coffee_num == rice_num) or (coffee_num == wine_num)\
            or (rice_num == wine_num)):
                tkinter.messagebox.showinfo('RB Error', 'Error! A unique die ' +
                                            'value must be assigned to each section.')
        # Validate bet amounts
        elif ((buffalo_bet + lotus_bet + pho_bet + coffee_bet + rice_bet + wine_bet) > p_balance):
            tkinter.messagebox.showinfo('Bet Error', 'Error! Total bets can not ' +
                                        'exceed current balance.')

        # If validations are false
        # start calculations
        else:
            # OUTCOME DISPLAYS
            # Die 1
            # Assign vars to return vars of func
            die1_icon, die1_outcome = modules.get_die1(die1, buffalo_num, \
                                                       lotus_num, pho_num, \
                                                       coffee_num, rice_num)
            # Set string vars
            die1_icon_str.set(die1_icon)
            die1_str.set(die1_outcome)

            # Die 2
            # Assign vars to return vars of func
            die2_icon, die2_outcome = modules.get_die2(die2, buffalo_num,\
                                                       lotus_num, pho_num, \
                                                       coffee_num, rice_num)
            # Set stringvars
            die2_icon_str.set(die2_icon)
            die2_str.set(die1_outcome)

            # Die 3
            # Assign vars to return vars of func
            die3_icon, die3_outcome = modules.get_die3(die3)
            # Set stringvars
            die3_icon_str.set(die3_icon)
            die3_str.set(die3_outcome)

            # Set earnings of current round
            # to 0
            p_earning = 0
            
            # CALCULATE DIE 1&2
            # Buffalo score
            if (die1 == buffalo_num) and (die2 == buffalo_num):
                p_earning += (buffalo_bet * 2)
            elif (die1 != buffalo_num) and (die2 != buffalo_num):
                p_earning -= buffalo_bet
            else:
                p_earning += buffalo_bet

            # Lotus score
            if (die1 == lotus_num) and (die2 == lotus_num):
                p_earning += (lotus_bet * 2)
            elif (die1 != lotus_num) and (die2 != lotus_num):
                p_earning -= lotus_bet
            else:
                p_earning += lotus_bet

            # Pho score
            if (die1 == pho_num) and (die2 == pho_num):
                p_earning += (pho_bet * 2)
            elif (die1 != pho_num) and (die2 != pho_num):
                p_earning -= pho_bet
            else:
                p_earning += pho_bet

            # Coffee score
            if (die1 == coffee_num) and (die2 == coffee_num):
                p_earning += (coffee_bet * 2)
            elif (die1 != coffee_num) and (die2 != coffee_num):
                p_earning -= coffee_bet
            else:
                p_earning += coffee_bet

            # Rice score
            if (die1 == rice_num) and (die2 == rice_num):
                p_earning += (rice_bet * 2)
            elif (die1 != rice_num) and (die2 != rice_num):
                p_earning -= rice_bet
            else:
                p_earning += rice_bet

            # Wine score
            if (die1 == wine_num) and (die2 == wine_num):
                p_earning += (wine_bet * 2)
            elif (die1 != wine_num) and (die2 != wine_num):
                p_earning -= wine_bet
            else:
                p_earning += wine_bet

            # Display earnings before lucky die
            earning1_str.set(p_earning)

            # DIE 3 PT1
            # Tax Police
            if die3 == 1:
                # (+) earnings are halved
                if p_earning >= 0:
                    p_earning -= (p_earning // 2)
                # (-) earnings are doubled
                else:
                    p_earning -= (p_earning * -2)
            # Lottery
            elif die3 == 2:
                # (+) earnings are doubled
                if p_earning >= 0:
                    p_earning += p_earning
                # (-) earnings are halved
                else:
                    p_earning += (p_earning // -2)
            # Red pocket
            # Add 5 points to earnings
            elif die3 == 3:
                p_earning += 5
            # Robbery
            # Subtract 2 points from earnings
            elif die3 == 4:
                p_earning -= 2
            # If die 3 is from 5-7, no lucky die
            else:
                p_earning = p_earning * 1

            # Calc balances w/ lucky die
            p_balance += p_earning
            d_balance -= p_earning

            # Update strvars with new balances
            # Updated score
            p_balance_str.set(p_balance)
            d_balance_str.set(d_balance)
            # Updated player message
            earning2_str.set(p_earning)

            # Var for point difference of dealer and player
            difference = d_balance - p_balance

            # OUTCOME SCENARIOS UPDATES
            # Update player message based on score
            # Organized based on priority of display
            # Message for if player is about to win

            # LOSE (end game)
            while (p_balance <= 0):
                # Update player message
                p_message = ('You are bankrupt')
                # Set strvar to new value
                p_message_str.set(p_message)
                # Update tk
                # Must use for while loops
                # bc while loops disrupt the mainloop
                # and causes screen to freeze
                # if tk can not update
                game_window.update()
                # Display messagebox
                tkinter.messagebox.showinfo('Lose', ('You are bankrupt with debts of '\
                                                     + str(p_balance) + ' point(s).'))
                # Reset game
                act_reset()

            # WIN (end game)
            while (p_balance > d_balance) and (p_balance > 0):
                # Update player message
                p_message = ('You beat the dealer by ' + str(-1 * difference)\
                             + ' points.')
                # Set strvar to new value
                p_message_str.set(p_message)
                # Update tk
                game_window.update()
                # Display messagebox
                tkinter.messagebox.showinfo('Win', ('You win! You beat the dealer by '\
                                                    + str(-1 * difference) + ' points.'))
                # Reset game
                act_reset()

            # OTHER OUTCOMES
            # Player is about to win
            while (difference <= 10) and (difference >= 0) and (p_earning >= 0):
                # Update player message
                p_message = ('Almost there! Only ' + str(difference + 1)\
                             + ' more points to go.')
                # Set strvar to new value
                p_message_str.set(p_message)
                # Update tk
                game_window.update()
                
            # Player is about to lose
            while (p_balance <= 3) and (p_balance > 0):
                # Update player message
                p_message = ('Be careful! You are ' + str(p_balance)\
                             + ' points from bankruptcy.')
                # Set strvar to new value
                p_message_str.set(p_message)
                # Update tk
                game_window.update()
                
            # Player had negative earnings that round
            while (difference > 0) and (p_earning < 0) and (p_balance > 0):
                # Update player message
                p_message = ('Oh snap! Try to avoid negative earnings. '\
                             + str(difference + 1) + ' more points to go.')
                # Set strvar to new value
                p_message_str.set(p_message)
                # Update tk
                game_window.update()
                
            # Player has positive balance
            # but is not close to winning
            while (difference > 10) and (p_balance > 3) and (p_earning >= 0):
                # Update player message
                p_message = ('Keep it up! ' + str(difference + 1) + ' more points to go.')
                # Set strvar to new value
                p_message_str.set(p_message)
                # Update tk
                game_window.update()
    

    # Reset function
    def act_reset():
        # Increase scope of vars
        nonlocal p_balance
        nonlocal d_balance

        # Reset strvars values
        # Player message
        p_message = ''
        # Balances
        p_balance = 10
        # RESUBMIT: FIXED TYPE IN D_BALANCE
        d_balance = 25
        # Earnings
        p_earning = ''
        # Dice display
        die1_icon = '❔'
        die1_outcome = ''
        die2_icon = '❔'
        die2_outcome = ''
        die3_icon = '❔'
        die3_outcome = ''
        # Earning display
        earning1 = ''
        earning2 = ''

        # Message box to let player know
        # game restarted
        tkinter.messagebox.showinfo('Restart', 'The game has restarted.')

        # Set strvars to updated values
        # RESUBMIT: FIXED TYPO IN D_BALANCE
        while p_balance == 10 and d_balance == 25:
            # Player message
            p_message_str.set(p_message)
            # Score display
            p_balance_str.set(p_balance)
            d_balance_str.set(d_balance)
            # Dice display
            die1_icon_str.set(die1_icon)
            die1_str.set(die1_outcome)
            die2_icon_str.set(die2_icon)
            die2_str.set(die2_outcome)
            die3_icon_str.set(die3_icon)
            die3_str.set(die3_outcome)
            # Earnings display
            earning1_str.set(earning1)
            earning2_str.set(earning2)
            # Radio buttons
            buffalo_rb_value.set(1)
            lotus_rb_value.set(2)
            pho_rb_value.set(3)
            coffee_rb_value.set(4)
            rice_rb_value.set(5)
            wine_rb_value.set(6)
            # Update tk
            game_window.update()
            

    # BACK TO MAIN
    # Roll button frame
    roll_frame = tkinter.Frame(score_frame)
    roll_frame.pack(anchor='w', side='left', padx=(15,0))
    # Roll button
        # Can not pass any arguments in command
        # or else function runs before button
        # is pressed
    roll_button = tkinter.Button(roll_frame, text='Roll dice',\
                                 command=roll_die, width=10, height=2)
    # Pack
    roll_button.pack(anchor='w')

    # Restart button
    restart_button = tkinter.Button(button_frame, text='Restart',\
                                    command=act_reset)
    restart_button.pack()

    # Main loop
    tkinter.mainloop()

# Call main function
main()
