import datetime
from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
import datetime
class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "People offer property"
    price = fields.Float()
    status = fields.Selection(
        string="Status",
        selection = [('accepted', "Accepted"), ("refused", "Refused")],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string = "Partner", required=True)
    property_id = fields.Many2one("estate.property", string = "Property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_validity")

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            if (type(record.create_date) != datetime.date):
                
                record.date_deadline = datetime.date.today() + relativedelta(days=record.validity)

            else: 
                record.date_deadline = record.create_date.date() + relativedelta(days=record.validity)

    def _inverse_validity(self):
        for record in self:
            record.validity = (record.date_deadline - record.create_date.date()).days 

    def accept_offer(self):
        for record in self:
            record.status = 'accepted'
            record.property_id.selling_price = record.price
            record.property_id.buyer_id = record.partner_id

    def refuse_offer(self):
        for record in self:
            record.status = 'refused'
            record.property_id.selling_price = 0
