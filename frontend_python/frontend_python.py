import reflex as rx

# Class that manages the states of the website
class State(rx.State):
    pass

# Function that renders the components of the page
def index() -> rx.Component:
    return rx.text("Hello world!")

app = rx.App()
app.add_page(index) # Add the page created above