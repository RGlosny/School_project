def to_login(self):
    self.select_frame("login")


def to_register(self):
    self.select_frame("register")


def to_home(self):
    self.select_frame("home")


def to_book_offers(self):
    self.select_frame("book_offers")


def to_edit_account(self):
    self.select_frame("edit_account")


def to_my_borrows(self):
    self.select_frame("my_borrows")


def to_details(self, book=None):
    self.select_frame("details", book)


def to_add_book(self):
    self.select_frame("add_book")


def to_edit_book(self, book=None):
    self.select_frame("edit_book", book)


def to_return_book(self, borrow=None):
    self.select_frame("return_book", borrow)


def select_frame(self, frame, obj=None):
    if frame == "login":
        self.place_login_screen()
        self.remove_menu_bar()
    else:
        self.remove_login_screen()

    if frame == "register":
        self.place_register_screen()
        self.remove_menu_bar()
    else:
        self.remove_register_screen()

    if frame == "home":
        self.place_home_screen()
    else:
        self.remove_home_screen()

    if frame == "book_offers":
        self.place_book_offers_screen()
    else:
        self.remove_book_offers_screen()

    if frame == "edit_account":
        self.place_edit_account_screen()
    else:
        self.remove_edit_account_screen()

    if frame == "my_borrows":
        self.place_my_borrows_screen()
    else:
        self.remove_my_borrows_screen()

    if frame == "details":
        self.place_book_details_screen(obj)
    else:
        self.remove_book_details_screen()

    if frame == "add_book":
        self.place_add_book_screen()
    else:
        self.remove_add_book_screen()

    if frame == "edit_book":
        self.place_edit_book_screen(obj)
    else:
        self.remove_edit_book_screen()

    if frame == "return_book":
        self.place_return_book_screen(obj)
    else:
        self.remove_return_book_screen()
