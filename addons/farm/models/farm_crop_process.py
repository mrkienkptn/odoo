from odoo import fields, models

class FarmCropProcess(models.Model):
  _name = "farm.crop.process"
  _description = "Crop process"
  name = fields.Char(required=True)
  crop_id = fields.Many2one('farm.crops', string='Crop')
  description = fields.Char(string='Description')

  
  