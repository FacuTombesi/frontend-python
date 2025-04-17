import reflex as rx

def title(text: str) -> rx.Component:
  return rx.heading(
    text,
    size="lg",
    width="100%"
  )