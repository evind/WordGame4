from ._anvil_designer import Lose_ScreenTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from .. import Globals


class Lose_Screen(Lose_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

   
    # Any code you write here will run when the form opens.
    global errors    
    self.repeating_panel_1.items = Globals.errors

    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Play_Screen')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Homepage')


