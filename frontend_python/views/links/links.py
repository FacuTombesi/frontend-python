import reflex as rx

def links() -> rx.Component:
  return rx.vstack(
    rx.avatar(fallback="FT", color_scheme="crimson", size="8"),
    rx.text("Mini-Projects"),
    rx.text("Welcome to the Mini-projects hub.")
  )