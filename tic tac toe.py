import tkinter as tk
from tkinter import messagebox
import win32gui
import win32con

# Fungsi untuk mengatur gaya jendela
def set_window_style(hwnd):
    # Menghilangkan tombol maximize (WS_MAXIMIZEBOX) ndak guna (gtw gwe dh lama ga cek ni file)
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    style = style & ~win32con.WS_MAXIMIZEBOX
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)

# Fungsi untuk mengecek kemenangan atau seri
def check_winner():
    for win_condition in winning_conditions:
        a, b, c = win_condition
        if buttons[a]['text'] == buttons[b]['text'] == buttons[c]['text'] != "":
            buttons[a].config(bg='green')
            buttons[b].config(bg='green')
            buttons[c].config(bg='green')
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[a]['text']} menang kontol!")
            restart_button.grid(row=4, columnspan=3)
            return

    if "" not in [button['text'] for button in buttons]:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        restart_button.grid(row=4, columnspan=3)

# Fungsiny untuk mengubah giliran pemain 
def change_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    turn_label.config(text=f"Player {current_player}'s turn")

# Fungsi untuk mengulang permainan / repeat the game
def restart_game():
    global current_player, game_active
    current_player = "X"
    game_active = True
    turn_label.config(text=f"Player {current_player}'s turn")
    restart_button.grid_remove()  # ngilangin tombol restart dari tampilan RAWRRR
    for button in buttons:
        button.config(text="", bg='white')

# Membuat jendela tkinter
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Inisialisasi variabel
current_player = "X"
game_active = True

# gawe/membuat label "nama mu"
author_label = tk.Label(root, text="Dibuat oleh (your name)", font=('normal', 12))
author_label.grid(row=0, columnspan=3, pady=(10, 0))

# Membuat tombol untuk setiap sel pada papan permainan
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=('normal', 20), width=5, height=2, command=lambda i=i: button_click(i))
    button.grid(row=(i // 3) + 1, column=i % 3)
    buttons.append(button)

# Daftar kondisi kemenangan
winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Label untuk menampilkan giliran pemain
turn_label = tk.Label(root, text=f"Player {current_player}'s turn", font=('normal', 16))
turn_label.grid(row=10, columnspan=3)

# Tombol untuk mengulang permainan (awalnya tidak ditampilkan)
restart_button = tk.Button(root, text="Restart Game", font=('normal', 16), command=restart_game)
restart_button.grid(row=11, columnspan=3)
restart_button.grid_remove()  # Menghilangkan tombol restart dari tampilan awal

# Dapatkan handle jendela aplikasi dan atur gaya jendela
app_name = "Tic-Tac-Toe"  # Ganti dengan judul jendela aplikasi Anda
hwnd = win32gui.FindWindow(None, app_name)

if hwnd:
    set_window_style(hwnd)
else:
    print(f"Jendela '{app_name}' tidak ditemukan.")


# Fungsi untuk menghandle klik pada tombol
def button_click(index):
    if buttons[index]['text'] == "" and game_active:
        buttons[index].config(text=current_player)
        check_winner()
        change_player()


root.mainloop()
