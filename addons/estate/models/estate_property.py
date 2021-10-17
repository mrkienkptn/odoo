from odoo import fields, models, api, _, exceptions
from dateutil.relativedelta import relativedelta
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Test Model"
    name = fields.Char(required=True, default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date('Availability Date', copy=False, default= lambda self :fields.Datetime.today() + relativedelta(days=90))
    expected_price = fields.Float(required = True)
    selling_price = fields.Float(required=True, readonly=True, default=100.0)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean(default=False)
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('west', 'West'), ('south', 'South'), ('north', 'North'), ('east', 'East')]
    )
    active = fields.Boolean('Active', default=True)
    state = fields.Selection(
        string = 'State',
        selection = [('new','New'), ('offer_received','Offer Received'), ('offer_accepted','Offer Accepted'), ('sold','Sold'), ('canceled','Canceled')],         
        default = 'new',
        store = True
    )
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    seller_id = fields.Many2one('res.users', string='Saleman', default=lambda self: self.env.user)
    property_type_id = fields.Many2one("estate.property.type", string = "Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", inverse_name="property_id",string = "Offers")
    total_area = fields.Integer(compute="_compute_total_area")
    best_price = fields.Float(compute="_compute_best_price")
    
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price>0)', 'Price must be a positive number')
    ]
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        

        for record in self:
            best_price = 0
            list_offers_price = record.offer_ids.mapped("price")
            if (len(list_offers_price) == 0):
                best_price = 0
            else:
                best_price = max(record.offer_ids.mapped("price"))
            record.best_price = best_price

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden == False:
            self.garden_area = 0
            self.garden_orientation=''
            return {'warning': {
                'title': _("Warning"),
                'message': ('This option reset to 0')}}
        else:
            self.garden_area = 10
            self.garden_orientation='south'
    
    def sold_property(self):
        for record in self:                

            if record.state == 'canceled':
                raise exceptions.UserError("Canceled Properties could not be sold")
            else:
                record.state = 'sold'
        return True

    def cancel_property(self):
        for record in self:
            if record.state == 'sold':
                raise exceptions.UserError("Sold Properties could not be canceled")
            else:
                record.state = 'canceled'
        return True

    @api.constrains("selling_price")
    def _check_selling_price(self):
        for record in self:
            if record.selling_price < record.expected_price * 0.9:
                raise exceptions.UserError("Selling price must be at least 90% of Expected price")