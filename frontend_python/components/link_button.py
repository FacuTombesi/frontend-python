import reflex as rx

def link_button(text: str, color: str, url: str) -> rx.Component:
  return rx.link(
    rx.button(
      text,
      color_scheme=color,
      radius="small",
      size="3",
      variant="solid"
    ),
    href=url,
    is_external=True,
    width="100%"
  )