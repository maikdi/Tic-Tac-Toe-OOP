from tictactoe.ui import TictactoeUI
from tictactoe.data import TictactoeData
import random, abc


class TictactoeService:

    def __init__(self):
        self.__data = TictactoeData()
        self.__ui = TictactoeUI(self)
        self.__bot = TictacMinimax(self, "X")

    def get_current_turn(self):
        return self.__data.get_current_turn()

    def get_board(self):
        return self.__data.get_board()

    def set_piece(self, x, y):
        piece_set = self.__data.set_piece(x, y)
        return piece_set

    def bot_move(self):
        board = self.__data.get_board()
        i, j = self.__bot.next_move()
        if i is not None:
            while board[i][j] != "":
                i, j = self.__bot.next_move()
            self.__ui._buttons[i][j].invoke()

    def reset_game(self):
        self.__data.reset_board()

    def new_game(self):
        self.__data.reset_board()
        self.__data.reset_score()

    def get_player1_score(self):
        return self.__data.get_player1_score()

    def get_player2_score(self):
        return self.__data.get_player2_score()

    def check_winning_condition(self):
        board = self.__data.get_board()
        horizontal = self.__check_horizontal(board)
        vertical = self.__check_vertical(board)
        diag = self.__check_diag(board)
        if horizontal is not None:
            return horizontal
        if vertical is not None:
            return vertical
        if diag is not None:
            return diag
        return None

    def return_winner(self):
        winner = self.check_winning_condition()
        if winner is not None:
            return winner
        if self.check_draw():
            return " "

    def __check_horizontal(self, board):
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != "":
                return board[i][0]
        return None

    def __check_vertical(self, board):
        for i in range(3):
            if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != "":
                return board[0][i]
        return None

    def __check_diag(self, board):
        if board[1][1] == "":
            return None
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        elif board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
        else:
            return None

    def add_winner_score(self):
        last_turn = self.__data.get_last_turn()
        if last_turn == "X":
            self.__data.add_player2_score()
        else:
            self.__data.add_player1_score()

    def check_draw(self):
        board = self.__data.get_board()
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    return False
        return True

    def show(self):
        self.__ui.mainloop()


class AbstractTicTacBot(abc.ABC):
    @abc.abstractmethod
    def __init__(self, service, side):
        self.__side = side
        self.__service = service

    def next_move(self):
        pass


class TictacRandomBot(AbstractTicTacBot):
    def __init__(self, service, side):
        super().__init__(service, side)
        self.__side = side
        self.service = service

    def next_move(self):
        if not self.service.check_draw():
            return random.randint(0, 2), random.randint(0, 2)


class TictacMinimax(AbstractTicTacBot):
    def __init__(self, service, side):
        super().__init__(service, side)
        self.__side = side
        self.__service = service

    def next_move(self):
        board = self.__service.get_board()
        best_score = -999
        best_move = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = self.__side
                    score = self.__minimax(board, False,-999,999,0)
                    board[i][j] = ""
                    if score >= best_score:
                        best_score = score
                        best_move = i, j
        return best_move

    def __minimax(self, board, isMaximizing,alpha,beta,depth):
        scores = {
            "X": 1,
            "O": -1,
            " ": 0,
        }
        result = self.__service.return_winner()
        if result != None:
            if depth == 0:
                return scores[result]
            else:
                return scores[result]/depth

        if isMaximizing:
            best_score = -999
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = self.__side
                        score = self.__minimax(board, False,alpha,beta,depth+1)
                        best_score = max(best_score, score)
                        alpha = max(alpha,best_score)
                        board[i][j] = ""
                        if beta <= alpha:
                            break
                if beta<=alpha:
                    break
            return best_score

        else:
            best_score = 999
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.__minimax(board, True,alpha,beta,depth+1)
                        best_score = min(best_score, score)
                        board[i][j] = ""
                        beta = min(beta,best_score)
                        if beta<=alpha:
                            break
                if  beta<=alpha:
                    break
            return best_score
