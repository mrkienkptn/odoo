import datetime
from odoo import fields, models, api, exceptions
from dateutil.relativedelta import relativedelta
import datetime
import logging
_logger = logging.getLogger(__name__)
class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "People offer property"
    _order = "price desc"
    price = fields.Float(required =True)
    status = fields.Selection(
        string="Status",
        selection = [('accepted', "Accepted"), ("refused", "Refused")],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string = "Partner", required=True)
    property_id = fields.Many2one("estate.property", string = "Property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_validity")
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)

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
            if (record.price < record.property_id.selling_price * 0.9):
                raise exceptions.UserError("Selling price must be at least 90% of Expected price")
            else:
                record.property_id.selling_price = record.price
                record.property_id.buyer_id = record.partner_id
                record.property_id.state = 'offer_accepted'

    def refuse_offer(self):
        for record in self:
            record.status = 'refused'
            
    @api.model
    def create(self, vals):
        current_state_of_property = self.env["estate.property"].browse(vals['property_id']).state
        if (current_state_of_property == "new"):
            self.env["estate.property"].browse(vals['property_id']).state = "offer_received"
        offers_of_this_property = self.env["estate.property"].browse(vals["property_id"]).offer_ids.mapped("price")
        if len(offers_of_this_property) != 0:

            max_price = max(offers_of_this_property)
            # _logger.debug("++++++++++++++++++++++++++++++++++++++++++++++++++")
            # _logger.debug(max_price)
            # _logger.debug(vals["price"])
            if vals["price"] < max_price: 
                raise exceptions.UserError("New price must be greater than " + str(max_price))
        return super(EstatePropertyOffer, self).create(vals)