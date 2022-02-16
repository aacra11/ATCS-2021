import random

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [["-","-","-"],["-","-","-"],["-","-","-"]]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print("To play Tic Tac Toe, the two players should take turn placing their pieces,")
        print("with Player X goes first, then Player O. The goal is to get 3 in a row, in any direction.")

    def print_board(self):
        # TODO: Print the board
        print("\t0\t1\t2")
        for i in range(len(self.board)):
            print(str(i)+"\t"+str(self.board[i][0])+"\t"+str(self.board[i][1])+"\t"+str(self.board[i][2]))

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        if self.board[row][col] == "-":
            return True
        return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        goodMove = False
        while goodMove == False:
            row = int(input("Enter a Row:"))
            col = int(input("Enter a Column:"))
            if self.is_valid_move(row, col):
                self.place_player(player, row, col)
                goodMove = True
            else:
                print("Please Enter a Valid Move.")

    def take_random_turn(self, player):
        taken = True
        while taken == True:
            num1 = random.randint(0,2)
            num2 = random.randint(0,2)
            if self.is_valid_move(num1,num2):
                self.place_player(player, num1, num2)
                taken = False

    def take_turn(self, player,depth):
        # TODO: Simply call the take_manual_turn function
        self.print_instructions()
        self.print_board()
        print("It is Player " + player + "'s turn.")
        if player == 'X':
            self.take_manual_turn(player)
        else:
            self.take_minimax_turn(player,depth)

    def check_col_win(self, player):
        # TODO: Check col win
        for i in range(len(self.board)):
            if self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i] and self.board[0][i] == player:
                return True
        return False

    def check_row_win(self, player):
        # TODO: Check row win
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][0] == player:
                return True
        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True
        elif self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_col_win(player) or self.check_row_win(player) or self.check_diag_win(player):
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        full = True
        for row in self.board:
            for val in row:
                if val == '-':
                    full = False
        if self.check_win('X') == False and self.check_win('O') == False and full == True:
            return True
        return False

    def minimax(self, player, depth):
        if self.check_win('O'):
            return (10,None,None)
        elif self.check_win('X') :
            return (-10,None,None)
        elif self.check_tie() or depth == 0:
            return (0,None,None)

        opt_row = -1
        opt_col = -1

        if player == 'O':
            best = -100
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.is_valid_move(i, j):
                        self.place_player(player, i, j)
                        score = self.minimax('X', depth - 1)[0]
                        if best < score:
                            best = score
                            opt_row = i
                            opt_col = j
                        self.place_player('-', i, j)
            return (best, opt_row, opt_col)

        if player == 'X':
            worst = 100
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.is_valid_move(i, j):
                        self.place_player(player, i, j)
                        score = self.minimax('O', depth - 1)[0]
                        if worst > score:
                            worst = score
                            opt_row = i
                            opt_col = j
                        self.place_player('-', i, j)
            return (worst, opt_row, opt_col)


    def take_minimax_turn(self,player,depth):
        score, row, col = self.minimax(player,depth)
        self.place_player(player,row,col)
        self.print_board()

    def play_game(self):
        # TODO: Play game
        cont = True
        players = ['X','O']
        num = 0
        while cont == True:
            player = players[num]
            self.take_turn(player,2)
            if self.check_tie() == True:
                print("Tie")
                cont = False
            elif self.check_win(player) == True:
                print(player + " wins")
                cont = False
            else:
                num = (num+1)%2


