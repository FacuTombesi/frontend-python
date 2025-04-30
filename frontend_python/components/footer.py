import reflex as rx

def footer() -> rx.Component:
  return rx.stack(
    rx.image(
      src="favicon.ico"
    ),
    rx.link(
      "Mini-Projects by FTombesi .",
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