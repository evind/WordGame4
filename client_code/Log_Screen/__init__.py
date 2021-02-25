from ._anvil_designer import Log_ScreenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files


class Log_Screen(Log_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    
    # Any code you write here will run when the form opens.
    logs = anvil.server.call('get_logs')
    self.repeating_panel_1.items = logs

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Home_Screen')

