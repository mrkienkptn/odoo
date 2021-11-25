from odoo import fields, models
import calendar
from datetime import datetime, date

MONTH_LIST =  [('1', 'Jan'), ('2', 'Feb'), ('3', 'Mar'), ('4', 'Apr'), ('5', 'May'), ('6', 'Jun'), ('7', 'Jul'), ('8', 'Aug'), ('9', 'Sep'), ('10', 'Oct'), ('11', 'Nov'),('12', 'Dec')]
DATE_LIST = [('1', '1st'), ('2', '2nd'), ('3', '3rd')]
for i in range(4, 32):
  DATE_LIST.append((str(i), str(i)+'th'))
class FarmCropRequests(models.Model):
  _name = "farm.crops"
  _description = "Farm Crops"
  name = fields.Char(required=True, default="Default")
  month_from = fields.Selection(
    selection=MONTH_LIST,
    required=True, 
    default=MONTH_LIST[int(datetime.now().strftime('%m'))-1]
  )
  month_to = fields.Selection(
    selection=MONTH_LIST,
    required=True, 
    default=MONTH_LIST[int(datetime.now().strftime('%m'))-1]
  )
  date_from = fields.Selection(
    selection=DATE_LIST,
    required=True, 
  )
  date_to = fields.Selection(
    selection=DATE_LIST,
    required=True, 
  )
  wharehouse = fields.Char(default="Default")
  stock_location = fields.Char()
  description = fields.Char()


  