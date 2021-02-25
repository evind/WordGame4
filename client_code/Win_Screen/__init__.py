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

        global time
        self.time_label.text = Globals.time

    def text_box_1_show(self, **event_args):
        """Focus user cursor in this text box so they can type right away"""
        self.text_box_1.focus()

    def button_1_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Prevent user from submitting empty name.
        if len(self.text_box_1.text) < 1:
            n = Notification("Please fill in a name!")
            n.show()
        else:
            # Log the user's win in the scores table, then send to post-win screen.
            name = self.text_box_1.text
            anvil.server.call(
                "log_score",
                Globals.time,
                name,
                Globals.source_word,
                Globals.user_input_list,
            )
            open_form("Post_Win_Screen")
