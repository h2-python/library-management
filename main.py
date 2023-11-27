# modulos necesarios
import flet as ft

import routes
from map_views import Route2View as R2V

from controls import ControlReference

def salir(page):
    page.window_close()


def main(page: ft.Page):
    # Translate the page.title to English
    page.title = "Library Management"

    page.theme_mode = "dark"

    # add the page to a general controller
    ControlReference.add_control_reference("page", page)
    R2V.init_map(page)

    # The navbar of the application
    bar = ft.AppBar(
        leading=ft.Icon(ft.icons.BOOK),
        leading_width=40,
        title=ft.Text("Library Manager"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        text="Exit", checked=False, on_click=lambda _: salir(page)
                    ),
                ]
            ),
        ],
    )

    # function that runs every time the route changes
    def route_change(route):
        page.views.clear()

        page.views.append(R2V.get_view4route(routes.ROOT_PATH, bar)) # Home view
        
        if route.route == routes.ADD_BOOK_PATH:
            page.views.append(R2V.get_view4route(routes.ADD_BOOK_PATH, bar)) # Add book view
        elif route.route == routes.EDIT_BOOK_PATH:
            page.views.append(R2V.get_view4route(routes.EDIT_BOOK_PATH, bar)) # Edit book view
        elif route.route == routes.VIEW_BOOK_PATH:
            page.views.append(R2V.get_view4route(routes.VIEW_BOOK_PATH, bar)) # View book view
        
        page.update() # Refresh the page with the new view

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # cuando cambie la ruta se ejecuta estan funciones
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
