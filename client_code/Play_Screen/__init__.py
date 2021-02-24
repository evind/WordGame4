from ._anvil_designer import Play_ScreenTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import time
from .. import Globals


class Play_Screen(Play_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global source_word
    Globals.source_word = anvil.server.call('pick_source_word')
    self.word_label.text = Globals.source_word
    
    self.item['curr_time'] = time.time()
    print("curr_time = ", self.item['curr_time'])

    
  def answer_box_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    self.answer_box.focus()

  def finished_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    global rules, user_input_list
    self.item['end_time'] = time.time()
    self.item['total_time'] = anvil.server.call('calculate_time', self.item['curr_time'], self.item['end_time'])
    Globals.user_input_list = self.answer_box.text.split()
    Globals.rules = anvil.server.call('evaluate_answer', self.item['source_word'], self.item['user_input_list'])
#     print("play screen")
#     print("source_word: ", self.item['source_word'])
#     print("user_input_list: ", self.item['user_input_list'])
#     print("valid_input: ", Globals.rules['valid_input'])
#     print("invalid_letters: ", Globals.rules['invalid_letters'])
#     print("invalid_words: ", Globals.rules['invalid_words'])
#     print("small_words: ", Globals.rules['small_words'])
#     print("duplicate_words: ", Globals.rules['duplicate_words'])
#     print("source_word_check: ", Globals.rules['source_word_check'])
    open_form('Score_Screen')
