from ._anvil_designer import Top_TenTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class Top_Ten(Top_TenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get rank and scores from embedded score_board data grid component
    rank = self.custom_1.get_rank()
    scores = self.custom_1.get_scores()