"""
Tic Tac Toe Game
"""
class TicTacToe():
    def __init__(self):
        pass

if __name__ == '__main__':
    while True:
        try:
            val = int(raw_input("Please enter an integer: "))
        except:
            print "Looks like you didnt enter an integer. Try Again"
        else:
            print "That is an integer"
            break

        print val
