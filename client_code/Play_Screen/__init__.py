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
    global rules, user_input_list, time
    self.item['end_time'] = time.time()
    Globals.time = anvil.server.call('calculate_time', self.item['curr_time'], self.item['end_time'])
    Globals.user_input_list = self.answer_box.text.split()
    Globals.rules = anvil.server.call('evaluate_answer', Globals.source_word, Globals.user_input_list)
    if not Globals.rules['valid_input']:
      Globals.errors = anvil.server.call('generate_errors', Globals.rules)

    open_form('Win_Screen')
