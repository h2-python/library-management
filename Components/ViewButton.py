from flet import *
from control_reference import ControlReference

# stores requeridas para este componente: EditButton
from Store.BooksStore import BookStore

control_map = ControlReference.return_control_reference()


def get_input_data(e):
    BookStore["state"]["bookSelected"] = None  # se deselecciona el libro seleccionado
    control_map["page"].go("/")


# main class
class ViewButton(UserControl):
    def __init__(self, page=None):
        super().__init__()
        self.page = page

    def view_button_instance(self):
        ControlReference.add_control_reference("ViewButton", self)

    def build(self):
        self.view_button_instance()

        return ElevatedButton(
            text="Aceptar",
            width=400,
            style=ButtonStyle(padding=20),
            on_click=get_input_data,
        )
