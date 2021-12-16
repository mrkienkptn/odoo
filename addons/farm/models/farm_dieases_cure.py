from odoo import fields, models

class FarmCropRequests(models.Model):
  _name = "farm.dieases.cure"
  _description = "Farm Dieases Cure"
  name = fields.Char(required=True)
  description = fields.Char(required=True)
  image = fields.Image("Image")
  