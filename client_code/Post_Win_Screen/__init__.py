from ._anvil_designer import Post_Win_ScreenTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class Post_Win_Screen(Post_Win_ScreenTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get rank and scores from embedded score_board data grid component.
    rank = self.custom_2.get_rank()
    scores = self.custom_2.get_scores()
    self.placement_label.text = f"Your rank is:  {rank} out of {len(scores)} players!"
