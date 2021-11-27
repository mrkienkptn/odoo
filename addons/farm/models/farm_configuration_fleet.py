from odoo import fields, models
from dateutil.relativedelta import relativedelta

class FarmConfigurationFleet(models.Model):
  _name = 'farm.configuration.fleet'
  _description = 'Configuration for fleet'
  vehicle = fields.Char(required=True)
  quantity = fields.Integer(default=0)
  start_date = fields.Date('Start Date', copy=False, default= lambda self :fields.Datetime.today())
  end_date = fields.Date('End Date', copy=False, default= lambda self :fields.Datetime.today() +  relativedelta(days=20))
  description = fields.Char()
  

  