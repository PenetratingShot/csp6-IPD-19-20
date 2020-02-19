####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

#idea 3
team_name = 'E3'
strategy_name = 'Check retailiation'
strategy_description = '''\
Check if the opponent retaliates by betraying a random round and checking their reaction'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.

    Let's pick a random constant number and betray that round.
    If this is the round we're supposed to betray, then betray and end the function.
    If this is before the round we're testing, just ignore.
    If this is after the round we tested, then check if their history for that round is betray, and if so, update a variable or something to keep track of it
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.