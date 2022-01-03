from odoo import fields, models

class FarmConfiguration(models.Model):
  _name = 'farm.configuration'
  _description = 'Configuration for farm'
  name = fields.Char(required=True, default="Process 1")
  sequence = fields.Integer('Sequence', default=1, help="Used to order stage.")
  _sql_constraints = [
    ('name', 'UNIQUE(name)', 'Name must be unique')
  ]

  