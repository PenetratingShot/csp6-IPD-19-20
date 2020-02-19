####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#idea 2
team_name = 'E2'
strategy_name = 'Betray every 3 rounds'
strategy_description = 'Collude, then alternate.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.

    Since we only get our previous history, we change check if this round is the third round by adding 1 to the length of our history and checking if it is divisible by 3
    if len(my_history) + 1 % 3 == 0:
      betray
    else:
      collude
    '''
    
    if len(my_history)%2 == 0:
        return 'c'
    else:
        return 'b'
    