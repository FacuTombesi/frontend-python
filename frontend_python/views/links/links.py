import reflex as rx
from frontend_python.components.link_button import link_button

def links() -> rx.Component:
  return rx.vstack(
    link_button("Calculator", "gray", "https://ftcalculator.vercel.app/"),
    link_button("Snake Game", "grass", "https://ftsnakegame.vercel.app/"),
    link_button("Weather App", "crimson", "https://ftweatherapp.vercel.app/"),
    link_button("Budget Tracker", "purple", "https://ftbudgettracker.vercel.app/")
  )