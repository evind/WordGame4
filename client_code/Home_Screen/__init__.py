from ._anvil_designer import Home_ScreenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server


class Home_Screen(Home_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def play_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Play_Screen')

  def topten_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Top_Ten')

  def log_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Log_Screen')

