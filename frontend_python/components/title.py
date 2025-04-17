import reflex as rx
import frontend_python.styles.styles as styles

def title(text: str) -> rx.Component:
  return rx.heading(
    text,
    align="center",
    size="8",
    width="100%",
    padding_top=styles.Size.SMALL.value
  )