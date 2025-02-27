from flet import *
from control_reference import ControlReference

# componentes requeridos para esta vista: EditBook
from Components.ViewBookForm import ViewBookForm

control_map = ControlReference.return_control_reference()


# clase principal
class ViewBookView(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    # añadimos vista al controlador
    def view_book_view_instance(self):
        ControlReference.add_control_reference("ViewBookView", self)

    def build(self):
        self.view_book_view_instance()
        viewBookForm = ViewBookForm(self.page)

        return Column(
            controls=[
                ElevatedButton("Volver", on_click=lambda _: self.page.go("/")),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[viewBookForm],
                ),
            ]
        )
