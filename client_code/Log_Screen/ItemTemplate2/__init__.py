from ._anvil_designer import ItemTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files

class ItemTemplate2(ItemTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    if self.item['won']:
      won = "SUCCESS"
    else:
      won = "FAILURE"
    sw = self.item['source_word']
    guesses = self.item['guesses']
    datetime = self.item['datetime'].strftime('%a %b %-d %H:%M:%S %Y')
    ip = self.item['ip_address']
    ua = self.item['user_agent']
      
    self.label_1.text = f"{won}: {sw} - {guesses}\n{datetime} - {ip} - {ua}\n----------------------------------"