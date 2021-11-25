from odoo import fields, models, api, _, exceptions

class ResUser(models.Model):
    _inherit = "res.users"

    property_ids = fields.One2many('estate.property', 'seller_id')