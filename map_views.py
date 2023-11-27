import flet as ft

import routes
from Views.Home import HomeView
from Views.AddBook import AddBookView
from Views.EditBook import EditBookView
from Views.ViewBook import ViewBookView

class Route2View:
    route2view = {}

    @classmethod
    def init_map(cls, page):
        cls.route2view[routes.ROOT_PATH] = HomeView(page)
        cls.route2view[routes.ADD_BOOK_PATH] = AddBookView(page)
        cls.route2view[routes.EDIT_BOOK_PATH] = EditBookView(page)
        cls.route2view[routes.VIEW_BOOK_PATH] = ViewBookView(page)

    @classmethod
    def get_view4route(cls, route, navbar):
        return ft.View(route, [navbar, cls.route2view[route]], scroll=ft.ScrollMode.AUTO)

