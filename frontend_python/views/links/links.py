import reflex as rx
from frontend_python.components.link_button import link_button

def links() -> rx.Component:
  return rx.vstack(
    link_button("Calculator", "gray"),
    link_button("Snake Game", "grass"),
    link_button("Weather App", "crimson"),
    link_button("Budget Tracker", "purple")
  )