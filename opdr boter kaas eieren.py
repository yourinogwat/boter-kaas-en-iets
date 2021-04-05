import random
from bke import start, EvaluationAgent, can_win, is_winner

class MyRandomAgent(EvaluationAgent):
                    def evaluate(self, board, my_symbol, opponent_symbol):
                        return random.randint(1,500)
                    
class A_God(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[0] == my_symbol:
            getal = getal + 2
        if board[2] == my_symbol:
            getal = getal + 2
        if board[6] == my_symbol:
            getal = getal + 2
        if board[8] == my_symbol:
            getal = getal + 2
        if board[4] == my_symbol:
            getal = getal + 6
        if can_win(board, my_symbol):
            getal = getal + 10
        if is_winner(board, opponent_symbol):
            getal = getal - 10000
        if is_winner(board, my_symbol):
            getal = getal + 11000
        return getal
    
God = A_God()    
stupid = MyRandomAgent()
start(player_o=God,player_x=stupid)