import reflex as rx

def header() -> rx.Component:
  return rx.stack(
    rx.avatar(fallback="FT", color_scheme="crimson", size="8"),
    rx.text("Mini-Projects"),
    rx.text("Welcome to the Mini-projects hub."),
    direction="column",
    align="center"
  )