import tkinter as tk
import math
import time

# --- PROJE GEREKLİ ALGORİTMA MANTIĞI ---
PLAYER = 'X'
AI = 'O'
minimax_call_count = 0
alphabeta_call_count = 0


# (is_winner, is_board_full, get_available_moves,
#  minimax, find_best_move_minimax,
#  alphabeta, find_best_move_alphabeta fonksiyonları

# --- ALGORİTMA KODLARI ---
def is_winner(board, player):
    return ((board[7] == player and board[8] == player and board[9] == player) or
            (board[4] == player and board[5] == player and board[6] == player) or
            (board[1] == player and board[2] == player and board[3] == player) or
            (board[7] == player and board[4] == player and board[1] == player) or
            (board[8] == player and board[5] == player and board[2] == player) or
            (board[9] == player and board[6] == player and board[3] == player) or
            (board[7] == player and board[5] == player and board[3] == player) or
            (board[9] == player and board[5] == player and board[1] == player))


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def get_available_moves(board):
    moves = []
    for i, move in enumerate(board):
        if move == ' ' and i != 0: moves.append(i)
    return moves


def minimax(current_board, depth, is_maximizing_player):
    global minimax_call_count
    minimax_call_count += 1
    if is_winner(current_board, AI): return 10 - depth
    if is_winner(current_board, PLAYER): return depth - 10
    if is_board_full(current_board): return 0
    if is_maximizing_player:
        best_score = -math.inf
        for move in get_available_moves(current_board):
            current_board[move] = AI
            score = minimax(current_board, depth + 1, False)
            current_board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(current_board):
            current_board[move] = PLAYER
            score = minimax(current_board, depth + 1, True)
            current_board[move] = ' '
            best_score = min(score, best_score)
        return best_score


def find_best_move_minimax(board):
    global minimax_call_count
    minimax_call_count = 0
    start_time = time.perf_counter()
    best_score = -math.inf
    best_move = 0
    for move in get_available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    end_time = time.perf_counter()
    return best_move, minimax_call_count, (end_time - start_time) * 1000


def alphabeta(current_board, depth, alpha, beta, is_maximizing_player):
    global alphabeta_call_count
    alphabeta_call_count += 1
    if is_winner(current_board, AI): return 10 - depth
    if is_winner(current_board, PLAYER): return depth - 10
    if is_board_full(current_board): return 0
    if is_maximizing_player:
        best_score = -math.inf
        for move in get_available_moves(current_board):
            current_board[move] = AI
            score = alphabeta(current_board, depth + 1, alpha, beta, False)
            current_board[move] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha: break
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(current_board):
            current_board[move] = PLAYER
            score = alphabeta(current_board, depth + 1, alpha, beta, True)
            current_board[move] = ' '
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha: break
        return best_score


def find_best_move_alphabeta(board):
    global alphabeta_call_count
    alphabeta_call_count = 0
    start_time = time.perf_counter()
    best_score = -math.inf
    best_move = 0
    for move in get_available_moves(board):
        board[move] = AI
        score = alphabeta(board, 0, -math.inf, math.inf, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    end_time = time.perf_counter()
    return best_move, alphabeta_call_count, (end_time - start_time) * 1000


# --- ALGORİTMA KODLARI BİTTİ ---


# --- "UYGULAMA" BÖLÜMÜ ---

class TicTacToeGUI:
    # --- Renk ve Font Tanımları---
    COLOR_BG = "#2E2E2E"
    COLOR_GRID_BG = "#252525"
    COLOR_BUTTON = "#3E3E3E"
    COLOR_BUTTON_HOVER = "#4A4A4A"
    COLOR_BUTTON_DISABLED = "#333333"
    COLOR_TEXT = "#E0E0E0"
    COLOR_X = "#3498DB"
    COLOR_O = "#E74C3C"
    COLOR_ACCENT = "#F39C12"

    FONT_BUTTON = ('Segoe UI', 32, 'bold')
    FONT_INFO = ('Segoe UI', 11)
    FONT_STATUS = ('Segoe UI', 14, 'bold')
    FONT_RESET = ('Segoe UI', 12, 'bold')

    def __init__(self, root):
        self.root = root
        self.root.title("Minimax vs Alfa-Beta - Tic Tac Toe")
        self.root.geometry("450x650")
        self.root.configure(bg=self.COLOR_BG)

        self.board = [' '] * 10
        self.buttons = {}

        # --- Durum Etiketi ---
        self.status_label = tk.Label(root, text="Sıra sizde (X)",
                                     font=self.FONT_STATUS,
                                     bg=self.COLOR_BG, fg=self.COLOR_TEXT,
                                     pady=20)
        self.status_label.pack()

        # --- Oyun Alanı (Izgara) Çerçevesi ---
        self.frame_board = tk.Frame(root, bg=self.COLOR_GRID_BG)
        self.frame_board.pack()

        grid_map = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        for i, index in enumerate(grid_map):
            row = i // 3
            col = i % 3
            button = tk.Button(self.frame_board, text=' ',
                               font=self.FONT_BUTTON,
                               bg=self.COLOR_BUTTON,
                               fg=self.COLOR_TEXT,
                               width=5, height=2,
                               relief=tk.FLAT, borderwidth=0,
                               activebackground=self.COLOR_BUTTON_HOVER,
                               activeforeground=self.COLOR_TEXT,
                               command=lambda idx=index: self.on_button_click(idx))

            button.grid(row=row, column=col, padx=5, pady=5)
            button.bind("<Enter>", self.on_button_enter)
            button.bind("<Leave>", self.on_button_leave)
            self.buttons[index] = button

        # --- Karşılaştırma Bölümü ---
        self.comparison_frame = tk.Frame(root, pady=20, bg=self.COLOR_BG)
        self.comparison_frame.pack()

        tk.Label(self.comparison_frame,
                 text="--- PERFORMANS KARŞILAŞTIRMASI ---",
                 font=self.FONT_STATUS,
                 bg=self.COLOR_BG, fg=self.COLOR_ACCENT).pack(pady=5)

        self.minimax_label = tk.Label(self.comparison_frame,
                                      text="Minimax: (Düğüm: 0, Süre: 0.00 ms)",
                                      font=self.FONT_INFO, anchor='w',
                                      bg=self.COLOR_BG, fg=self.COLOR_TEXT)
        self.minimax_label.pack(fill='x', padx=20)

        self.alphabeta_label = tk.Label(self.comparison_frame,
                                        text="Alfa-Beta: (Düğüm: 0, Süre: 0.00 ms)",
                                        font=self.FONT_INFO, anchor='w',
                                        bg=self.COLOR_BG, fg=self.COLOR_TEXT)
        self.alphabeta_label.pack(fill='x', padx=20)

        # --- Yeniden Başlatma Butonu ---
        self.reset_button = tk.Button(root, text="Yeniden Başlat",
                                      font=self.FONT_RESET,
                                      command=self.reset_game,
                                      bg=self.COLOR_ACCENT, fg=self.COLOR_GRID_BG,
                                      relief=tk.FLAT, borderwidth=0,
                                      activebackground="#F5B041",
                                      activeforeground=self.COLOR_GRID_BG,
                                      pady=10)
        self.reset_button.pack(pady=20, fill='x', padx=50)

    # --- Buton Hover Efektleri (Aynı) ---
    def on_button_enter(self, event):
        button = event.widget
        if button['state'] == 'normal':
            button.config(bg=self.COLOR_BUTTON_HOVER)

    def on_button_leave(self, event):
        button = event.widget
        if button['state'] == 'normal':
            button.config(bg=self.COLOR_BUTTON)

    def on_button_click(self, index):
        if self.board[index] == ' ' and self.status_label['text'].startswith("Sıra"):
            self.update_board(index, PLAYER)
            if self.check_game_over():
                return
            self.status_label.config(text="AI (O) düşünüyor...", fg=self.COLOR_TEXT)
            self.root.after(100, self.ai_move)

    def ai_move(self):
        # 1. Minimax'ı çalıştır
        _, minimax_calls, minimax_time = find_best_move_minimax(self.board.copy())

        # 2. Alfa-Beta'yı çalıştır
        ai_move_index, alphabeta_calls, alphabeta_time = find_best_move_alphabeta(self.board.copy())

        # 3. Sonuçları etiketlere yazdır
        self.minimax_label.config(
            text=f"Minimax:   (Düğüm: {minimax_calls:,} | Süre: {minimax_time:.2f} ms)")
        self.alphabeta_label.config(
            text=f"Alfa-Beta: (Düğüm: {alphabeta_calls:,} | Süre: {alphabeta_time:.2f} ms)")

        self.update_board(ai_move_index, AI)

        if self.check_game_over():
            return

        self.status_label.config(text="Sıra sizde (X)", fg=self.COLOR_TEXT)

    def update_board(self, index, player):
        self.board[index] = player
        player_color = self.COLOR_X if player == PLAYER else self.COLOR_O
        self.buttons[index].config(text=player,
                                   state='disabled',
                                   disabledforeground=player_color,
                                   bg=self.COLOR_BUTTON_DISABLED)

    # --- DEĞİŞEN ANA FONKSİYONLAR ---

    def check_game_over(self):
        """
        Oyunun bitip bitmediğini kontrol eder ve sonucu
        doğrudan 'status_label'a yazar.
        """
        if is_winner(self.board, PLAYER):
            # Pop-up yerine etiketi güncelle:
            self.status_label.config(text="Kazandınız (X)!", fg=self.COLOR_X)
            self.disable_all_buttons(self.COLOR_X)
            return True
        elif is_winner(self.board, AI):
            # etiketi güncelle:
            self.status_label.config(text="AI Kazandı (O)!", fg=self.COLOR_O)
            self.disable_all_buttons(self.COLOR_O)
            return True
        elif is_board_full(self.board):
            # etiketi güncelle:
            self.status_label.config(text="Oyun Berabere!", fg=self.COLOR_TEXT)
            self.disable_all_buttons()
            return True
        return False

    def disable_all_buttons(self, winner_color=None):
        for button in self.buttons.values():
            button.config(state='disabled')
            if winner_color and button['text'] != ' ':
                button.config(bg=winner_color, disabledforeground=self.COLOR_TEXT)

    def reset_game(self):
        """Oyunu sıfırlar."""
        self.board = [' '] * 10
        for button in self.buttons.values():
            button.config(text=' ', state='normal', bg=self.COLOR_BUTTON)

        # Durum etiketinin metnini ve rengini sıfırla
        self.status_label.config(text="Sıra sizde (X)", fg=self.COLOR_TEXT)

        self.minimax_label.config(text="Minimax: (Düğüm: 0, Süre: 0.00 ms)")
        self.alphabeta_label.config(text="Alfa-Beta: (Düğüm: 0, Süre: 0.00 ms)")


# --- Uygulamayı Başlat ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()