# Most of the content of this file has been copied from the odoo maintenance addon
from odoo import api, fields, models, SUPERUSER_ID

class MaintenanceTeam(models.Model):
    _name = 'practice.maintenance.team'
    _description = 'Practice Maintenance Teams'

    name = fields.Char('Team Name', required=True, translate=True)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one('res.company', string='Company',
        default=lambda self: self.env.company)
    member_ids = fields.Many2many(
        'res.users', 'practice_maintenance_team_users_rel', string="Team Members",
        domain="[('company_ids', 'in', company_id)]")
    color = fields.Integer("Color Index", default=0)
    request_ids = fields.One2many('practice.maintenance.request', 'maintenance_team_id', copy=False)

    stages = fields.Many2many('practice.maintenance.stage', compute='_compute_team_stages', store=True)

    @api.depends('request_ids.stage_id')
    def _compute_team_stages(self):
        for team in self:
            team.stages = team.request_ids.stage_id

    def write(self, *args, **kwargs):
        return super().write(*args, **kwargs)



class MaintenanceRequest(models.Model):
    _name = 'practice.maintenance.request'
    _description = 'Practice Maintenance Request'
    _order = "id desc"
    _check_company_auto = True

    @api.returns('self')
    def _default_stage(self):
        return self.env['practice.maintenance.stage'].search([], limit=1)

    def _get_default_team_id(self):
        MT = self.env['practice.maintenance.team']
        team = MT.search([('company_id', '=', self.env.company.id)], limit=1)
        if not team:
            team = MT.search([], limit=1)
        return team.id

    name = fields.Char('Subjects', required=True)
    company_id = fields.Many2one('res.company', string='Company',
        default=lambda self: self.env.company)
    description = fields.Html('Description')
    request_date = fields.Date('Request Date', tracking=True, default=fields.Date.context_today,
                               help="Date requested for the maintenance to happen")
    owner_user_id = fields.Many2one('res.users', string='Created by User', default=lambda s: s.env.uid)
    user_id = fields.Many2one('res.users', string='Technician', tracking=True)
    stage_id = fields.Many2one('practice.maintenance.stage', string='Stage', ondelete='restrict', tracking=True,
                               group_expand='_read_group_stage_ids', default=_default_stage, copy=False)
    priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High')], string='Priority')
    color = fields.Integer('Color Index')
    close_date = fields.Date('Close Date', help="Date the maintenance was finished. ")
    kanban_state = fields.Selection([('normal', 'In Progress'), ('blocked', 'Blocked'), ('done', 'Ready for next stage')],
                                    string='Kanban State', required=True, default='normal', tracking=True)
    # active = fields.Boolean(default=True, help="Set active to false to hide the maintenance request without deleting it.")
    archive = fields.Boolean(default=False, help="Set archive to true to hide the maintenance request without deleting it.")
    maintenance_type = fields.Selection([('corrective', 'Corrective'), ('preventive', 'Preventive')], string='Maintenance Type', default="corrective")
    schedule_date = fields.Datetime('Scheduled Date', help="Date the maintenance team plans the maintenance.  It should not differ much from the Request Date. ")
    maintenance_team_id = fields.Many2one('practice.maintenance.team', string='Team', required=True, default=_get_default_team_id)
    duration = fields.Float(help="Duration in hours.")
    done = fields.Boolean(related='stage_id.done')

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        """ Read group customization in order to display all the stages in the
            kanban view, even if they are empty
        """
        stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

class MaintenanceStage(models.Model):
    """ Model for case stages. This models the main stages of a Maintenance Request management flow. """

    _name = 'practice.maintenance.stage'
    _description = 'Practice Maintenance Stage'
    _order = 'sequence, id'

    name = fields.Char('Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=20)
    fold = fields.Boolean('Folded in Maintenance Pipe')
    done = fields.Boolean('Request Done')
