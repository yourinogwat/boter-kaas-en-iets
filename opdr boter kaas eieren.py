import random
from bke import start, EvaluationAgent

class MyRandomAgent(EvaluationAgent):
                    def evaluate(self, board, my_symbol, opponent_symbol):
                        return random.randint(1,500)
                    
class A_God(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if board[4] == my_symbol:
            getal = getal + 6
        return getal
    
God = A_God()    
stupid = MyRandomAgent()
start(player_o=God,player_x=stupid)