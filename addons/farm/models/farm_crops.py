from odoo import fields, models, api
class FarmCropRequests(models.Model):
  _name = "farm.crops"
  _description = "Farm Crops"
  name = fields.Char(required=True, default="Default")
  date_from = fields.Date()
  date_to = fields.Date()
  wharehouse = fields.Char(default="Default")
  stock_location = fields.Char()
  description = fields.Char()
  image = fields.Image("Image")
