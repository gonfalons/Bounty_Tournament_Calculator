def get_tournament_info():
    """
    gather all required information to build a tournament through user input
    """
    print("hint:\n \
    1. in some structures, such as progressive knockouts or bounty builders, a successful knockout\n \
    does not reward its full face-value. For example, a bounty builder may start with a $50 displayed bounty,\n \
    and if you knockout this player, you receive $25 cash. \n \
    2. Don't enter in currency symbols or decimals. $50 should be entered as 50.\n \
    ********************************************************************************")
    global my_tournament
    my_tournament = {}
    my_tournament['buyin'] = int(input('What is the tournament buy-in, in dollars?  $'))
    my_tournament['starting_chips'] = int(input('What is the starting stack? '))
    my_tournament['initial_bounty'] = int(input('What is the starting cash reward for a knockout?:  $'))
    my_tournament['structure'] = input('\
    What is the knockout structure? Enter the corresponding key...\n \
    if it is a [P]rogressive Knockout, enter [P]...\n \
    if it is a [B]ounty Builder, enter [B]...\n \
    if it is a [S]uper Knockout, enter [S]...\n \
    if it is a [T]urbo, or S[t]andard knockout, enter [T]...').upper()

    if my_tournament['structure'] == 'P' or my_tournament['structure'] == 'B':  # TODO: try/except
        print("PKO")
        my_tournament['displayed_bounty'] = int(input('What is the currently displayed bounty?:   $'))

    elif my_tournament['structure'].upper() == 'S':
        print("Super Knockout")
    elif my_tournament['structure'].upper() == 'T':
        print("Standard or Turbo knockout")
    else:
        print("Try again...")  # TODO: handle this
    # TODO: check for valid input
    return my_tournament


get_tournament_info()
