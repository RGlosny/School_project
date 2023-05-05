from sqlalchemy import create_engine, Column, String, Boolean, Integer, \
    DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    email = Column("email", String, primary_key=True)
    name = Column("name", String)
    surname = Column("surname", String)
    password = Column("password", String)
    state = Column("state", String)
    city = Column("city", String)
    psc = Column("psc", String)
    is_admin = Column("is_admin", Boolean)

    def __init__(self, email, name, surname, password, state, city,
                 psc, is_admin):
        self.email = email
        self.name = name
        self.surname = surname
        self.password = password
        self.state = state
        self.city = city
        self.psc = psc
        self.is_admin = is_admin


class Book(Base):
    __tablename__ = "books"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String)
    author_name = Column("author_name", String)
    author_surname = Column("author_surname", String)
    language = Column("language", String)
    year = Column("year", Integer)
    isbn = Column("isbn", String)
    description = Column("description", String)
    availability = Column("availability", Boolean)

    def __init__(self, title, author_name, author_surname, language, year,
                 isbn, description):
        self.title = title
        self.author_name = author_name
        self.author_surname = author_surname
        self.language = language
        self.year = year
        self.isbn = isbn
        self.description = description
        self.availability = True


class Borrow(Base):
    __tablename__ = "borrows"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    customer_email = Column("customer_email", Integer,
                            ForeignKey("users.email"))
    book_id = Column("book_id", Integer, ForeignKey("books.id"))
    book_title = Column("book_title", String)
    status = Column("status", Boolean)
    date_from = Column("date_from", DateTime)
    date_to = Column("date_to", DateTime, nullable=True)

    def __init__(self, customer_email, book_id, book_title, status, date_from,
                 date_to=None):
        self.customer_email = customer_email
        self.book_id = book_id
        self.book_title = book_title
        self.status = status
        self.date_from = date_from
        self.date_to = date_to


engine = create_engine('sqlite:///mydb.db', echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
