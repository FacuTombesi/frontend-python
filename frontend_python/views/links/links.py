import reflex as rx
from frontend_python.components.link_button import link_button

def links() -> rx.Component:
  return rx.vstack(
    link_button(),
    rx.button(
      "Calculator",
      size="3",
      variant="solid",
      color_scheme="gray",
      radius="small"
    ),
    rx.button(
      "Snake Game",
      size="3",
      variant="solid",
      color_scheme="grass",
      radius="small"
    ),
    rx.button(
      "Weather App",
      size="3",
      variant="solid",
      color_scheme="crimson",
      radius="small"
    ),
    rx.button(
      "Budget Tracker",
      size="3",
      variant="solid",
      color_scheme="purple",
      radius="small"
    ),
  )