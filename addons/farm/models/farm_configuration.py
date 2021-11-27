from odoo import fields, models

class FarmConfiguration(models.Model):
  _name = 'farm.configuration'
  _description = 'Configuration for farm'
  stage_name = fields.Char(required=True)
  stage_folded_in_kanban = fields.Boolean(default=True)
  stage_description = fields.Char()
  

  