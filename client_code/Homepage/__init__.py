from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.server

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def play_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    rules = {'valid_input': True, 'invalid_letters': [],
             'invalid_words': [], 'small_words': [],
             'duplicate_words': [], 'source_word_check': False}
    prev_words = []
    # leaderboard stuff
    # create dictionary
    open_form('Play_Screen')



