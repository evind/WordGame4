from ._anvil_designer import Play_ScreenTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class Play_Screen(Play_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    rules = {'valid_input': True, 'invalid_letters': [],
          'invalid_words': [], 'small_words': [],
          'duplicate_words': [], 'source_word_check': False}
    prev_words = []
