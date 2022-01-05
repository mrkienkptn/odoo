from odoo import fields, models, api, SUPERUSER_ID, exceptions
from dateutil.relativedelta import relativedelta
import json
class FarmCropRequests(models.Model):
  _name = "farm.crop.requests"
  _description = "All crop requests"
  stage_id = fields.Many2one(
    'farm.configuration',
    string='Stage',
    group_expand='_group_expand_stage_ids'
  )
  code = fields.Char(
    required=True,
    string="Code",
    readonly=True,
    default="New REQ"
  )
  name = fields.Char(required=True)
  crop_id = fields.Many2one('farm.crops', string="Crops")
  responsible_user_id = fields.Many2one('res.partner', string='Responsible User')
  supervisor_id = fields.Many2one('res.users', string='Supervisor', default=lambda self: self.env.user)
  start_date = fields.Date(required=True, copy=False, default=lambda self :fields.Datetime.today())
  end_date = fields.Date(copy=False, default=lambda self :fields.Datetime.today() + relativedelta(days=5))
  color = fields.Integer()
  description = fields.Char()
  dieases_cure_count = fields.Integer(compute="_compute_dieases_cure_count")
  project_id = fields.Many2one('project.project', string="Project")
  task_count = fields.Integer(compute="_compute_task_count")
  _sql_constraints = [
    ('code', 'UNIQUE(code)', 'This code already exist')
  ]

  @api.model
  def _group_expand_stage_ids(self, stages, domain, order):
    """ Read group customization in order to display all the stages in the
        kanban view, even if they are empty
    """
    stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
    return stages.browse(stage_ids)

  def test_action():
    pass

  @api.model
  def create(self, vals):
    vals['code'] = self.env['ir.sequence'].next_by_code('farm.crop.requests')
    return super(FarmCropRequests, self).create(vals)

  @api.depends("crop_id")
  def _compute_dieases_cure_count(self):
    for record in self:
      record.dieases_cure_count = record.crop_id.dieases_cure_count

  @api.depends("project_id")
  def _compute_task_count(self):
    for record in self:
      record.task_count = record.project_id.task_count

  def action_open_tasks(self):
    self.ensure_one()
    return {
      'type': 'ir.actions.act_window',
      'name': 'Tasks',
      'res_model': 'project.task',
      'action': 'project.act_project_project_2_project_task_all',
      'domain': [('project_id', '=', self.project_id.id)],
      'view_mode': 'kanban,tree,calendar,graph'
    }
  
  def action_open_dieases(self):
    self.ensure_one()
    return {
      'type': 'ir.actions.act_window',
      'name': 'Dieases Cure',
      'res_model': 'farm.dieases.cure',
      'action': 'farm.farm_dieases_cure_action',
      'domain': [('crop_ids', '=', self.crop_id.id)],
      'view_mode': 'tree,form'
    }