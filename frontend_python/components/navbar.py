import reflex as rx

def navbar() -> rx.Component:
  return rx.stack(
    rx.text(
      "<ftombesi/>"
    ),
    position="sticky",
    bg="purple",
    padding_x="16px",
    padding_y="16px",
    z_index="999",
    align="center"
  )