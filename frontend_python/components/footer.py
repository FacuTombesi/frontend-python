import reflex as rx
import datetime

def footer() -> rx.Component:
  return rx.stack(
    rx.image(
      src="favicon.ico"
    ),
    rx.link(
      f"© 2023-{datetime.date.today().year} FTombesi by Facundo Tombesi",
      href="https://ftportfolio.vercel.app/",
      is_external=True,
      color="white"
    ),
    direction="row",
    justify="between",
    align="center",
    bg="gray",
    padding_x="16px",
    padding_y="16px"
  )