from flet import *
from control_reference import ControlReference

# componentes requeridos para esta vista: AddBook
from Components.AddBookForm import AddBookForm

control_map = ControlReference.return_control_reference()


# clase principal
class AddBookView(UserControl):
    def __init__(self, page=None):
        self.page = page
        super().__init__()

    # añadimos vista al controlador
    def add_book_view_instance(self):
        ControlReference.add_control_reference("AddBookView", self)

    def build(self):
        self.add_book_view_instance()
        addBookForm = AddBookForm(self.page)
        return Column(
            controls=[
                ElevatedButton("Volver", on_click=lambda _: self.page.go("/")),
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[addBookForm],
                ),
            ]
        )
