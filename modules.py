# Final Culminating
# Modules
# Samantha Mac
# ICS2O1

# Get outcome of die 1
# Pass arguments from main file
def get_die1(die1, buffalo_num, lotus_num, pho_num, coffee_num, rice_num):
    # If die value == die value of section
    # assign icon and word outcome
    if die1 == buffalo_num:
        die1_icon = '🐃'
        die1_outcome = 'Water Buffalo'
    elif die1 == lotus_num:
        die1_icon = '🪷'
        die1_outcome = 'Lotus'
    elif die1 == pho_num:
        die1_icon = '🍜'
        die1_outcome = 'Pho'
    elif die1 == coffee_num:
        die1_icon = '☕️'
        die1_outcome = 'Coffee'
    elif die1 == rice_num:
        die1_icon = '🍚'
        die1_outcome = 'Rice'
    else:
        die1_icon = '🍶'
        die1_outcome = 'Wine Jug'

    # Return vars
    return die1_icon, die1_outcome

def get_die2(die2, buffalo_num, lotus_num, pho_num, coffee_num, rice_num):
    if die2 == buffalo_num:
        die2_icon = '🐃'
        die2_outcome = 'Water Buffalo'
    elif die2 == lotus_num:
        die2_icon = '🪷'
        die2_outcome = 'Lotus'
    elif die2 == pho_num:
        die2_icon = '🍜'
        die2_outcome = 'Pho'
    elif die2 == coffee_num:
        die2_icon = '☕️'
        die2_outcome = 'Coffee'
    elif die2 == rice_num:
        die2_icon = '🍚'
        die2_outcome = 'Rice'
    else:
        die2_icon = '🍶'
        die2_outcome = 'Wine Jug'

    return die2_icon, die2_outcome

def get_die3(die3):
    if die3 == 1:
        die3_icon = '👮‍♀️'
        die3_outcome = 'Tax Police (0.5x Earnings)'
    elif die3 == 2:
        die3_icon = '🤑'
        die3_outcome = 'Lottery (2x Earnings)'
    elif die3 == 3:
        die3_icon ='🧧'
        die3_outcome = 'Red Pocket (+5)'
    elif die3 == 4:
        die3_icon = '🥷'
        die3_outcome = 'Robbery️ (-2)'
    else:
        die3_icon = '❔'
        die3_outcome = 'No Add-On'

    return die3_icon, die3_outcome


