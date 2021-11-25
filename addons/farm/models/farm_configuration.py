from odoo import fields, models

class FarmCropRequests(models.Model):
  _name = "farm.configuration"
  _description = "Farm Configuration"

  farmer_name = fields.Char()
  