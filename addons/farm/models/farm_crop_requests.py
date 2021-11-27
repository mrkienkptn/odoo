from odoo import fields, models, api

class FarmCropRequests(models.Model):
  _name = "farm.crop.requests"
  _description = "All crop requests"
  stage_id = fields.Many2one('farm.configuration')
  code = fields.Char(required=True, string="Code of request")
  name = fields.Char(required=True)
  crop = fields.Many2one('farm.crops', string="Crops")
  responsible_user_id = fields.Many2one('res.users', string='Responsible User', default=lambda self: self.env.user)
  supervisor_id = fields.Many2one('res.users', string='Supervisor', default=lambda self: self.env.user)
  start_date = fields.Date()
  end_date = fields.Date()
