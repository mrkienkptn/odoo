from odoo import fields, models, api

class FarmConfigurationPartner(models.Model):
  _inherit = 'res.partner'
  is_farmer = fields.Boolean(
    compute = "_compute_is_farmer"
  )
  is_animal = fields.Boolean(
    ompute = "_compute_is_animal"
  )
  is_location = fields.Boolean(
    ompute = "_compute_is_location"
  )
  crop_ids = fields.Many2many('farm.crops', string = 'Crops')
  @api.depends("is_animal", "is_location")
  def _compute_is_farmer(self):
    for record in self:
      if record.is_animal or record.is_location:
        record.is_farmer = False

  @api.depends("is_farmer", "is_location")
  def _compute_is_animal(self):
    for record in self:
      if record.is_farmer or record.is_location:
        record.is_animal = False

  @api.depends("is_animal", "is_farmer")
  def _compute_is_location(self):
    for record in self:
      if record.is_animal or record.is_farmer:
        record.is_location = False