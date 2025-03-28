import reflex as rx

# Class that manages the states of the website
class State(rx.State):
    pass

# Function that renders the components of the page
def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "<ftombesi/>",
            height="40px"
        ),
        position="sticky",
        bg="purple",
        padding_x="16px",
        padding_y="4px",
        z_index="999"
    )

app = rx.App()
app.add_page(index) # Add the page created above