import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter
        
    # we want all players to get their next move given a game.
    def get_move(self, tictactoe):
        pass   
    
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # using inheritance to copy the properties of the main base player(Parent)
        
    def get_move(self, tictactoe):
        square = random.choice(tictactoe.available_moves())
        return square
    
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, tictactoe):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # we are going to check that this is a coorect value by trying to cast it to an 
            # integer and if its not, then we say its invalid
            # if that spot is nt available on the board we say invalid
            try:
                val = int(square)
                if val not in tictactoe.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
                
            except ValueError:
                print ('Invalid square. Try again')
                
        return val