import reflex as rx
from frontend_python.components.title import title

def header() -> rx.Component:
  return rx.stack(
    rx.avatar(fallback="FT", color_scheme="crimson", size="8"),
    title("MINI-PROJECTS"),
    rx.text("Welcome to the Mini-projects hub."),
    direction="column",
    align="center"
  )