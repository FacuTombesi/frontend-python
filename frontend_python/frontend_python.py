import reflex as rx
from frontend_python.components.navbar import navbar
from frontend_python.components.footer import footer
from frontend_python.views.header.header import header
from frontend_python.views.links.links import links
import frontend_python.styles.styles as styles

# Class that manages the states of the website
class State(rx.State):
    pass

# Function that renders the components of the page
# CSS styles are applied like this and are written with _ instead of - as in traditional CSS
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.stack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                direction="column",
                align="center",
                margin_y=styles.Spacer.BIG.value
            ),
        ),
        footer()
    )

app = rx.App()
app.add_page(index) # Add the page created above