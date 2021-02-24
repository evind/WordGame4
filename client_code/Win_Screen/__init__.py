from ._anvil_designer import Win_ScreenTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from .. import Globals

class Win_Screen(Win_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global time
    self.time_label.text = Globals.time
