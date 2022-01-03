from odoo import fields, models

class FarmProjects(models.Model):
  _name = "farm.projects"
  _description = "Projects"
  name = fields.Char(required=True)
  