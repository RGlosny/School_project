import customtkinter as ctk
from PIL import Image
from setup import APP_WIDTH, APP_HEIGHT, FONT
from classes import session, User


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x200")

        self.label = ctk.CTkLabel(self, text=text, font=(FONT, 20))
        self.label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


class App(ctk.CTk):
    from _login_screen import login_screen, place_login_screen, \
        remove_login_screen, move_to_register

    from _register_screen import register_screen, place_register_screen, \
        remove_register_screen, register_user, back_to_login

    from _home_screen import home_screen, place_home_screen, \
        remove_home_screen

    from _menu_bar import menu_bar, place_menu_bar, remove_menu_bar, sign_out

    from _book_offers_screen import book_offers_screen, \
        place_book_offers_screen, remove_book_offers_screen

    from _edit_account import edit_account_screen, place_edit_account_screen, \
        remove_edit_account_screen, save_changes_account

    from _my_borrows_screen import my_borrows_screen, place_my_borrows_screen,\
        remove_my_borrows_screen

    from _book_details import book_details_screen, place_book_details_screen,\
        remove_book_details_screen, details_to_issue, remove_issue, \
        issue_book, delete_book, delete_confirmation

    from _add_book import add_book_screen, place_add_book_screen,\
        remove_add_book_screen, add_book

    from _edit_book import edit_book_screen, place_edit_book_screen,\
        remove_edit_book_screen, save_changes

    from _return_book import return_book_screen, place_return_book_screen,\
        remove_return_book_screen, end_borrow

    from screen_selector import select_frame, to_home, to_login, to_register, \
        to_book_offers, to_edit_account, to_my_borrows, to_details, \
        to_add_book, to_edit_book, to_return_book

    def __init__(self):
        # define app
        super().__init__()
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        self.title("Book borrowing system")
        self.minsize(1400, 800)
        self.maxsize(1920, 1200)
        img1 = ctk.CTkImage(Image.open("books.webp"), size=(1920, 1080))
        self.bg = ctk.CTkLabel(master=self, image=img1, text="")
        self.bg.place(relx=0, rely=0)

        # connect to database
        self.session = session
        self.user = None

        # start app on login screen
        self.login_screen()
        self.register_screen()
        self.place_login_screen()

        # define rest of the screens
        self.book_offers_screen()
        self.edit_account_screen()
        self.book_details_screen()
        self.add_book_screen()
        self.edit_book_screen()
        self.return_book_screen()
        self.home_screen()
        self.toplevel_window = None

    def login_user(self):
        email = self.entry1.get()
        password = self.entry2.get()

        user = self.session.query(User).filter_by(email=email).first()
        if user is None:
            text = f"No user with email \'{email}\' is signed in."
            self.place_topwindow(text)
            return

        if user.password != password:
            text = "Incorrect password!"
            self.place_topwindow(text)
            return

        self.entry1.delete(0, ctk.END)
        self.entry2.delete(0, ctk.END)

        self.user = user  # set currently logged user
        self.menu_bar()
        self.remove_login_screen()
        self.place_home_screen()
        self.place_menu_bar()
        self.my_borrows_screen()

    def place_topwindow(self, text):
        if self.toplevel_window is None or \
                not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(text)
            self.toplevel_window.attributes("-topmost", True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
