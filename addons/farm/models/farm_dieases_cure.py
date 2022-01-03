from odoo import fields, models

class FarmDieasesCure(models.Model):
  _name = "farm.dieases.cure"
  _description = "Farm Dieases Cure"
  name = fields.Char(required=True)
  description = fields.Char(required=True)
  image = fields.Image("Image")
  crop_ids = fields.Many2many("farm.crops")
  _sql_constraints = [
    ('name', 'UNIQUE(name)', 'This dieases cure is already exist')
  ]