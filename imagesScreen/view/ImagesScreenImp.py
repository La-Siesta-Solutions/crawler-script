from core.view import CoreUI
from imagesScreen.domain.contract.ImagesScreen import ImagesScreen


class ImagesScreenImp(ImagesScreen):

    def show_title(self):
        CoreUI.clean_screen()
        CoreUI.draw_terminal_border()
        CoreUI.print_full_screen_horizontal_line(2)
        CoreUI.print_centered_text("Managing Images", 3)
        CoreUI.print_full_screen_horizontal_line(4)

    def show_images_text(self, images_amount):
        CoreUI.print_text(6, 5, f"We have found \033[1m\033[32m{len(images_amount)} images\033[0m.")
        return CoreUI.print_input(7, 5, f"Would you like to process them now using \033[1mAWSTextExtract\033[0m? \033[1m[Y][N]\033[0m ")

    def ask_amazon_access_key(self):
        return CoreUI.print_input(9, 5, "Amazon \033[1mAccess Key\033[0m: ")

    def ask_amazon_secret_key(self):
        return CoreUI.print_input(10, 5, "Amazon \033[1mSecret Access Key\033[0m: ")

    def ask_amazon_region_name(self):
        return CoreUI.print_input(11, 5, "Amazon \033[1mregion name\033[0m: ")

    def show_images_processing_disclaimer(self, images_amount):
        CoreUI.print_text(13, 5, f"Processing \033[1m{len(images_amount)} images\033[0m with TextExtract can take \033[1msome time\033[0m.")
        CoreUI.print_text(14, 5,"Please be patient while the script analyzes \033[1meach image\033[0m.\n")
        CoreUI.print_text(15, 5, "The duration depends on the \033[1mnumber and complexity\033[0m of the files.")

    def show_processing_result(self, images_amount, images_processed):
        CoreUI.print_text(17, 5, f"Operation completed! \033[1m{images_processed} images\033[0m out of {len(images_amount)} processed.")
        CoreUI.print_input(18, 5, "Click enter to \033[1m\033[32mcontinue\033[0m ")