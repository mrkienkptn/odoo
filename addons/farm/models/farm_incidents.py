from odoo import fields, models


class FarmIncidents(models.Model):
    _name = "farm.incidents"
    _description = "Farm Incidents"
    name = fields.Char(required=True)
    crop_id = fields.Many2one("farm.crops", string="Crop")
    task = fields.Char(required=True)
    datetime = fields.Datetime()
    description = fields.Char()
    location_id = fields.Many2one('res.partner', string="Location")