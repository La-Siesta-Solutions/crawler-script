from core.view import CoreUI


def show_title():
    CoreUI.draw_terminal_border()
    CoreUI.print_full_screen_horizontal_line(2)
    CoreUI.print_centered_text("LA SIESTA CRAWLER v0.1", 3)
    CoreUI.print_full_screen_horizontal_line(4)

def show_introduction():
    CoreUI.print_text(6, 5, "# \033[31mAttention!\033[0m Before starting to crawl, \033[1mreview\033[0m the site's \033[1m'robots.txt'\033[0m and \033[1mterms of service\033[0m.")
    CoreUI.print_text(7, 5, "# \033[1mRespect\033[0m exclusion directives and avoid \033[1moverloading\033[0m the server with excessive requests.")
    CoreUI.print_text(8, 5, "# \033[1mMisuse\033[0m of the extracted information can have \033[1mlegal consequences.\033[0m")

def ask_enter_to_start():
    return CoreUI.print_input(10, 5, "Press enter to continue...")
