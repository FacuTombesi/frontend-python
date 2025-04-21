import reflex as rx
from frontend_python.components.title import title

def header() -> rx.Component:
  return rx.stack(
    rx.avatar(fallback="FT", color_scheme="crimson", size="8"),
    title("mini-projects"),
    rx.text("Welcome to the mini-projects hub! All of my small projects and apps can be found here."),
    direction="column",
    align="center"
  )