import reflex as rx

def link_button(text: str, color: str) -> rx.Component:
  return rx.button(
    text,
    size="3",
    variant="solid",
    color_scheme=color,
    radius="small"
  )