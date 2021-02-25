from ._anvil_designer import score_boardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
from .. import Globals

class score_board(score_boardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    global time
    rank = 0
    scores = anvil.server.call('get_scores')
    for i, v in enumerate(scores, start=1):
      v['rank'] = i
      if v['time'] == Globals.time and v['matches'] == ", ".join(Globals.user_input_list):
        rank = i
    self.repeating_panel_2.items = scores