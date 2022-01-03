from odoo import fields, models, api
class FarmCrops(models.Model):
  _name = "farm.crops"
  _description = "Farm Crops"
  name = fields.Char(required=True, default="Default")
  date_from = fields.Date()
  date_to = fields.Date()
  warehouse_id = fields.Many2one("stock.warehouse", string="Wharehouse")
  stock_location_id = fields.Many2one("stock.location", string="Stock Location")
  description = fields.Char()
  image = fields.Image("Image")
  incident_ids = fields.Many2many("farm.incidents", string="Crop Incidents")
  dieases_cure_ids = fields.Many2many("farm.dieases.cure", string="Dieses Cures")
  dieases_cure_count = fields.Integer(compute="_compute_dieases_cure_count")
  @api.depends("dieases_cure_ids")
  def _compute_dieases_cure_count(self):
    for record in self:
      list_cure = record.dieases_cure_ids.mapped("name")
      record.dieases_cure_count = len(list_cure)
          
