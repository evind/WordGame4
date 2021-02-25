from ._anvil_designer import Lose_ScreenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from .. import Globals


class Lose_Screen(Lose_ScreenTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        global errors
        # Display any errors the user made in their answer.
        self.repeating_panel_1.items = Globals.errors

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form("Play_Screen")

    def button_2_click(self, **event_args):
        """This method is called when the button is clicked"""
        open_form("Homepage")
