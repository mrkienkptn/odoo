from odoo import fields, models

class FarmConfiguration(models.Model):
  _inherit = 'res.partner'
  is_farmer = fields.Boolean()
  is_animal = fields.Boolean()
  is_location = fields.Boolean()
  crop_ids = fields.Many2many('farm.crops', string = 'Crops')
  

  