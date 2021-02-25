from ._anvil_designer import Play_ScreenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import time
from .. import Globals


class Play_Screen(Play_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    global source_word
    Globals.source_word = anvil.server.call('pick_source_word')
    self.word_label.text = Globals.source_word
    self.item['curr_time'] = time.time()
    
  def answer_box_show(self, **event_args):
    """Focus user cursor in this text box so they can type right away"""
    self.answer_box.focus()

  def finished_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    global rules, user_input_list, time
    
    # Prevent user from submitting empty answer.
    if len(self.answer_box.text) < 1:
      n = Notification("You must type an answer!")
      n.show()
    else:
      # Calculate time to answer & evaluate user's answer.
      self.item['end_time'] = time.time()
      Globals.time = anvil.server.call('calculate_time', self.item['curr_time'], self.item['end_time'])
      Globals.user_input_list = self.answer_box.text.split()
      Globals.rules = anvil.server.call('evaluate_answer', Globals.source_word, Globals.user_input_list)
      
      # Get user-agent info, then log their attempt to the log table.
      user_agent = anvil.http.request(anvil.server.get_api_origin() + '/get-user-agent', json=True)['user-agent']
      anvil.server.call('log_attempt', Globals.rules, Globals.source_word, Globals.user_input_list, user_agent)
      
      # Send user to the win or lose screen based on their answer.
      if not Globals.rules['valid_input']:
        Globals.errors = anvil.server.call('generate_errors', Globals.rules)
        open_form('Lose_Screen')
      else:
        open_form('Win_Screen')
  