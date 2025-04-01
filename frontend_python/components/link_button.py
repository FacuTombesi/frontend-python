import reflex as rx

def link_button() -> rx.Component:
  return rx.button(
    "Calculator",
    size="3",
    variant="solid",
    color_scheme="gray",
    radius="small"
  )