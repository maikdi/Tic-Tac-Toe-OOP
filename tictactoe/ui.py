import tkinter as tk
from tkinter import ttk


class TictactoeUI:

    def __init__(self, service):
        self._root = tk.Tk()
        self._root.title("Board Games")
        self.__service = service
        self.__tabs = self.__create_tabs()
        self._game_window = self.__create_game_frame()
        self._buttons = self.__create_game_buttons()
        self._setting_frame = self.__create_setting_frame()
        self._score_frame = self.__create_score_frame()
        self._setting_buttons = self.__create_setting_buttons()
        self._score_board = self.__create_score_board()
        self._win_label = self.__create_win_announcement()
        self.__coming_soon()

    def __create_tabs(self):
        tab_control = ttk.Notebook(self._root)
        tab_1 = tk.Frame(tab_control)
        tab_2 = tk.Frame(tab_control)
        tab_control.add(tab_1, text = "Tic Tac Toe")
        tab_control.add(tab_2, text = "Others")
        tab_control.grid(row=0,column=0,sticky="snew")
        return tab_1,tab_2
    def __create_game_frame(self):
        game_window = tk.Frame(self.__tabs[0], borderwidth=2, relief="groove")
        game_window.grid(row=0, column=0, rowspan=2)
        return game_window

    def __create_score_frame(self):
        score_frame = tk.Frame(self.__tabs[0], borderwidth=2, relief="groove")
        score_frame.grid(row=0, column=1, sticky="n")
        return score_frame

    def __create_setting_frame(self):
        setting_frame = tk.Frame(self.__tabs[0], borderwidth=2, relief="groove")
        setting_frame.grid(row=1, column=1, sticky="n")
        # setting_frame.rowconfigure(0,weight=1)
        # setting_frame.columnconfigure(0,weight=1)
        return setting_frame

    def __create_game_buttons(self):
        # buttons = []
        # for row in range(3):
        #     temp = []
        #     for column in range(3):
        #         button = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
        #                     command=lambda: self.__game_pressed(y,x))
        #         temp.append(button)
        #         button.grid(row=row,column=column)
        #     buttons.append(temp)
        button1 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(0, 0))
        button2 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(0, 1))
        button3 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(0, 2))
        button4 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(1, 0))
        button5 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(1, 1))
        button6 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(1, 2))
        button7 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(2, 0))
        button8 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(2, 1))
        button9 = tk.Button(self._game_window, text="", font=("Comic Sans MS", 36), width=3,
                            command=lambda: self.__game_pressed(2, 2))
        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)
        button4.grid(row=1, column=0)
        button5.grid(row=1, column=1)
        button6.grid(row=1, column=2)
        button7.grid(row=2, column=0)
        button8.grid(row=2, column=1)
        button9.grid(row=2, column=2)

        return [[button1, button2, button3], [button4, button5, button6], [button7, button8, button9]]

    def __game_pressed(self, x, y):
        key_pressed = self.__service.set_piece(y, x)
        self._buttons[x][y].config(text=key_pressed)
        self._buttons[x][y]['state'] = "disabled"
        winner = self.__service.return_winner()
        if winner is not None and winner != " ":
            self._win_label.config(text="{} WINS!!!".format(key_pressed))
            self.__service.add_winner_score()
            self.__set_score()
            self.disable_game_buttons()
        elif winner == " ":
            self._win_label.config(text="DRAW")
            self.disable_game_buttons()
        if winner is None and self.__service.get_current_turn()=="X":
            self.__service.bot_move()


    def disable_game_buttons(self):
        for i in range(3):
            for button in self._buttons[i]:
                button['state'] = "disabled"

    def enable_game_buttons(self):
        for i in range(3):
            for button in self._buttons[i]:
                button['state'] = "normal"

    def __create_score_board(self):
        player1_label = tk.Label(self._score_frame, text="Player 1:", font=("Times New Roman", 16)).grid(row=0,
                                                                                                         column=0)
        player2_label = tk.Label(self._score_frame, text="Player 2:", font=("Times New Roman", 16)).grid(row=1,
                                                                                                         column=0)
        player1_score = tk.Label(self._score_frame, text=self.__service.get_player1_score(), bg="white", width=20,
                                 font=("Times New Roman", 16),
                                 relief="groove", borderwidth=2, anchor="w")
        player2_score = tk.Label(self._score_frame, text=self.__service.get_player2_score(), bg="white", width=20,
                                 font=("Times New Roman", 16),
                                 relief="groove", borderwidth=2, anchor="w")
        player1_score.grid(row=0, column=1)
        player2_score.grid(row=1, column=1)
        return player1_score, player2_score

    def __create_win_announcement(self):
        win_label = tk.Label(self._score_frame,text="",font=("Comic Sans MS",20))
        win_label.grid(row=2,column=0,columnspan=2)
        return win_label

    def __create_setting_buttons(self):
        new_game_button = tk.Button(self._setting_frame, text="New Game", font=("Comic Sans MS", 16), width=8,
                                    command=self.__new_game_clicked)
        reset_button = tk.Button(self._setting_frame, text="Reset", font=("Comic Sans MS", 16), width=8,
                                 command=self.__reset_clicked)
        exit_button = tk.Button(self._setting_frame, text="Exit", font=("Comic Sans MS", 16), width=8,
                                command=self._root.quit)
        new_game_button.grid(row=0, column=0)
        reset_button.grid(row=1, column=0)
        exit_button.grid(row=2, column=0)
        return new_game_button, reset_button, exit_button

    def __reset_clicked(self):
        self.__service.reset_game()
        for i in range(3):
            for j in range(3):
                self._buttons[i][j].config(text="")
        self._win_label.config(text="")
        self.enable_game_buttons()

    def __new_game_clicked(self):
        self.__service.new_game()
        for i in range(3):
            for j in range(3):
                self._buttons[i][j].config(text="")
        self._win_label.config(text="")
        self.__set_score()
        self.enable_game_buttons()

    def __set_score(self):
        self._score_board[0].config(text=self.__service.get_player1_score())
        self._score_board[1].config(text=self.__service.get_player2_score())

    def __coming_soon(self):
        tk.Label(self.__tabs[1],text="Updates Coming Soon!", font=("Gotham Narrow Ultra",36)).pack()
    def mainloop(self):
        self._root.mainloop()
