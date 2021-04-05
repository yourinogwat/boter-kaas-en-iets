import random
from bke import start, EvaluationAgent

class MyRandomAgent(EvaluationAgent):
                    def evaluate(self, board, my_symbol, opponent_symbol):
                        return random.randint(1,500)
                    
            
stupid = MyRandomAgent()
start(player_o=stupid,player_x=stupid)