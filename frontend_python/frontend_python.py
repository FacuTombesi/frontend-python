import reflex as rx
from frontend_python.components.navbar import navbar
from frontend_python.views.header.header import header

# Class that manages the states of the website
class State(rx.State):
    pass

# Function that renders the components of the page
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header()
    )

app = rx.App()
app.add_page(index) # Add the page created above