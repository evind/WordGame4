from ._anvil_designer import Win_ScreenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    self.text_box_1.focus()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_1.text
    anvil.server.call('log_score', Globals.time, name, Globals.source_word, Globals.user_input_list)
    open_form('High_Scores')



