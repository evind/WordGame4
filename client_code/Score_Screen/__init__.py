from ._anvil_designer import Score_ScreenTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from .. import Globals


class Score_Screen(Score_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    # Any code you write here will run when the form opens.
    global source_word, user_input_list, rules
#     print("score screen")
#     print("valid_input: ", Globals.rules['valid_input'])
#     print("invalid_letters: ", Globals.rules['invalid_letters'])
#     print("invalid_words: ", Globals.rules['invalid_words'])
#     print("small_words: ", Globals.rules['small_words'])
#     print("duplicate_words: ", Globals.rules['duplicate_words'])
#     print("source_word_check: ", Globals.rules['source_word_check'])
    