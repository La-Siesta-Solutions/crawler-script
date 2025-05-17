import os
import shutil


def draw_terminal_border():
    cols, rows = shutil.get_terminal_size()
    horizontal = "─" * (cols - 2)
    vertical = "│"
    top = f"┌{horizontal}┐"
    bottom = f"└{horizontal}┘"
    os.system("clear" if os.name == "posix" else "cls")
    print(top)
    for _ in range(rows - 3):
        print(f"{vertical}{' ' * (cols - 2)}{vertical}")
    print(bottom)

def print_full_screen_horizontal_line(position):
    cols, _ = shutil.get_terminal_size()
    line_length = cols - 4
    line = "-" * line_length
    text_lines = line.split("\n")
    for i, txt in enumerate(text_lines):
        print(f"\033[{position + i};3H{txt}", end="", flush=True)

def print_centered_text(text, position):
    cols, _ = shutil.get_terminal_size()
    available_space = cols - 4
    spaces = (available_space - len(text)) // 2
    print(f"\033[{position};{3 + spaces}H{text}", end="", flush=True)

def print_text(row, col, text):
    print(f"\033[{row};{col}H{text}", end="", flush=True)

def print_input(row, col, text):
    print(f"\033[{row};{col}H{text}", end="", flush=True)
    return input()

def hide_cursor():
    rows, _ = shutil.get_terminal_size()
    print(f"\033[{rows};1H", end="", flush=True)

def clean_screen():
    os.system("clear")