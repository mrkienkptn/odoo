from odoo import fields, models, api

class FarmConfigurationPartner(models.Model):
  _inherit = 'res.partner'
  is_farmer = fields.Boolean(
    default = False
  )
  is_location = fields.Boolean(    
    default = False
  )
  crop_ids = fields.Many2many('farm.crops', string = 'Crops')

  @api.onchange('is_farmer')
  def _onchange_is_farmer(self):
    self.is_location = False

  @api.onchange('is_location')
  def _onchange_is_location(self):
    self.is_farmer = False
  