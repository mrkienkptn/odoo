from odoo import fields, models

class EstatePropertyTag(models.Model):
        _name = "estate.property.tag"
        _description = "Tags for Estate properties"
        name = fields.Char(required=True)
        _sql_constraints = [
        ('name_unique', 'unique(name)', 'Type must be unique')
        ]