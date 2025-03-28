import reflex as rx

def header() -> rx.Component:
  return rx.vstack(
    rx.avatar(fallback="FT", color_scheme="crimson", size="8")
  )