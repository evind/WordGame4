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

    global time, rank, scores
    rank = 0
    scores = anvil.server.call('get_scores')
    
    # Iterate over sorted scores table data to add rank number, and determine rank of current 
    user's # answer.
    for i, v in enumerate(scores, start=1):
      v['rank'] = i
      if v['time'] == Globals.time and v['matches'] == ", ".join(Globals.user_input_list):
        rank = i
    self.repeating_panel_1.items = scores
    
  def get_rank(self):
    global rank
    return rank
  
  def get_scores(self):
    global scores
    return scores
    