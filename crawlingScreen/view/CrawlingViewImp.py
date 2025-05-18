
from core.view import CoreUI
from crawlingScreen.domain.contract.CrawlingView import CrawlingView


class CrawlingViewImp(CrawlingView):

    def show_title(self):
        CoreUI.clean_screen()
        CoreUI.draw_terminal_border()
        CoreUI.print_full_screen_horizontal_line(2)
        CoreUI.print_centered_text("Crawling... ", 3)
        CoreUI.print_full_screen_horizontal_line(4)

    def ask_client_api_key(self):
        return CoreUI.print_input(6, 5, "Spider api-key: ")

    def ask_url_to_crawl(self):
        return CoreUI.print_input(7, 5, "Url to crawl: ")

    def ask_white_list(self):
        return CoreUI.print_input(8, 5, "White-list separated by comas or leave it blank: ")

    def show_crawling(self, url):
        CoreUI.clean_screen()
        CoreUI.draw_terminal_border()
        CoreUI.print_full_screen_horizontal_line(2)
        CoreUI.print_centered_text(f"Crawling \033[31m{url}\033[0m", 3)
        CoreUI.print_full_screen_horizontal_line(4)
        CoreUI.print_text(6, 5, "\033[1mCrawling in progress...\033[0m Please wait while we gather the data.")
        CoreUI.print_text(7, 5, "This process may take \033[1ma few moments\033[0m depending on the website's size")
        CoreUI.print_text(8, 5, "\033[1mResults will be displayed shortly.\033[0m Thank you for your patience.")
        CoreUI.print_text(10, 5, "\033[1m\033[32mWorking...!\033[0m")

    def show_costs(self, total_cost):
        return CoreUI.print_input(10, 5, f"Operation completed! Total cost: \033[1m${total_cost}\033[0m. Click enter to \033[1m\033[32mcontinue\033[0m")