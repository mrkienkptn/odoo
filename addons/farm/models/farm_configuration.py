from odoo import fields, models

class FarmConfiguration(models.Model):
  _name = 'farm.configuration'
  _description = 'Configuration for farm'
  name = fields.Char(required=True, default="Process 1")
  fold = fields.Boolean(default=True)
  description = fields.Char()
  

  