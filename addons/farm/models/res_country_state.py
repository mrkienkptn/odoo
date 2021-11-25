from odoo import fields, models

class ResCountryState(models.Model):
    _name="res.country.state"
    _description = "Res Country"
    country_id = fields.Char()
    name = fields.Char()
    code = fields.Char()

