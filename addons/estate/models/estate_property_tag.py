from odoo import fields, models

class EstatePropertyTag(models.Model):
        _name = "estate.property.tag"
        _description = "Tags for Estate properties"
        _order = "name"
        name = fields.Char(required=True)
        color = fields.Integer()
        _sql_constraints = [
        ('name_unique', 'unique(name)', 'Tag must be unique')
        ]