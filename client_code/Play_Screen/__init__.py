from ._anvil_designer import Play_ScreenTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import time


class Play_Screen(Play_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.item['source_word'] = anvil.server.call('pick_source_word')
    self.word_label.text = self.item['source_word']
    
    self.item['curr_time'] = time.time()
    print("curr_time = ", self.item['curr_time'])

    
  def answer_box_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    self.answer_box.focus()

  def finished_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.item['end_time'] = time.time()
    self.item['total_time'] = anvil.server.call('calculate_time', self.item['curr_time'], self.item['end_time'])
    self.item['user_input_list'] = self.answer_box.text.split()
    anvil.server.call('evaluate_answer', self.item['source_word'], self.item['user_input_list'])


