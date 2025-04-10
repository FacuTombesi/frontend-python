import reflex as rx
from enum import Enum

# Constants
MAX_WIDTH = "600px"

# Classes
class Size(Enum):
  SMALL="0.5em"
  DEFAULT="1em" # Using em instead of px is a good practice for web development. "1em" is equal to the website's current font-size
  BIG="2em"

# Global Styles
GLOBAL_STYLE = {
  rx.button: {
    "width": "100%",
    "height": "100%",
    "padding": Size.SMALL.value
  }
}