import reflex as rx

def link_button(text: str, color: str, url: str) -> rx.Component:
  return rx.link(
    rx.button(
      text,
      size="3",
      variant="solid",
      color_scheme=color,
      radius="small",
      width="100%"
    ),
    href=url,
    is_external=True,
    width="100%"
  )