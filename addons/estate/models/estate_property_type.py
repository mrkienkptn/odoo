from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "All types of estate property"
    _order = "name"
    name = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    sequence = fields.Integer('Sequence', default=1, help="Used to order type. Lower is better.")
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id', string='Offers')
    offer_count = fields.Integer(compute="_compute_amount_offers")
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Type must be unique')
    ]

    @api.depends("offer_ids")
    def _compute_amount_offers(self):
        for record in self:
            list_offer = record.offer_ids.mapped("price")
            record.offer_count = len(list_offer)
        


    