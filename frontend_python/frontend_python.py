import reflex as rx
from frontend_python.components.navbar import navbar
from frontend_python.components.footer import footer
from frontend_python.views.header.header import header
from frontend_python.views.links.links import links

# Class that manages the states of the website
class State(rx.State):
    pass

# Function that renders the components of the page
def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer()
    )

app = rx.App()
app.add_page(index) # Add the page created above