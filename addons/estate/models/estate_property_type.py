from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "All types of estate property"
    name = fields.Char(required=True)
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Type must be unique')
    ]

    