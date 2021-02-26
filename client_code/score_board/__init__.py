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

        # Iterate over sorted scores table data to add rank number, determine rank of current
        # user's answer, then update repeating panel.
        scores = anvil.server.call("get_scores")
        for i, v in enumerate(scores, start=1):
            v['rank'] = i
            if v['time'] == Globals.time and v["matches"] == ", ".join(
                Globals.user_input_list
            ):
                rank = i
            # Convert time to a formatted str to work around issue causing
            # long decimal numbers despite round() usage in server code.
            v['time'] = "{:0.2f}".format(v['time'])
        self.repeating_panel_1.items = scores[0:10]

    def get_rank(self):
        global rank
        return rank

    def get_scores(self):
        global scores
        return scores
