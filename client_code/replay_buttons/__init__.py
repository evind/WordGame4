from ._anvil_designer import replay_buttonsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class replay_buttons(replay_buttonsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Play_Screen')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home_Screen')


