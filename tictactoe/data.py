class TictactoeData:
    def __init__(self):
        self.__board = self.__create_board()
        self.__player1_score = 0
        self.__player2_score = 0
        self.__current_turn = "O"

    def __create_board(self):
        board = []
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append("")
            board.append(temp)
        return board

    def get_current_turn(self):
        return self.__current_turn

    def set_piece(self, x, y):
        piece_set = self.__current_turn
        self.__board[y][x] = self.__current_turn
        self._switch_turns()
        return piece_set

    def get_last_turn(self):
        if self.__current_turn == "O":
            return "X"
        else:
            return "O"

    def get_player1_score(self):
        return self.__player1_score

    def add_player1_score(self):
        self.__player1_score += 1

    def add_player2_score(self):
        self.__player2_score += 1

    def get_player2_score(self):
        return self.__player2_score

    def _switch_turns(self):
        if self.__current_turn == "O":
            self.__current_turn = "X"
        else:
            self.__current_turn = "O"

    def reset_board(self):
        self.__board = self.__create_board()
        self.__current_turn = "O"

    def reset_score(self):
        self.__player1_score = 0
        self.__player2_score = 0
        self.__current_turn = "O"

    def get_board(self):
        return self.__board