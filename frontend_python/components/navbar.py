import reflex as rx

def navbar() -> rx.Component:
  return rx.stack(
    rx.text(
      "<ftombesi/>",
      height="40px"
    ),
    position="sticky",
    bg="purple",
    padding_x="16px",
    padding_y="4px",
    z_index="999",
    align="center"
  )