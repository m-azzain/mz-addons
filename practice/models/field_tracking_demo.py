from odoo import fields, models


class FieldTracking(models.Model):
    _name = 'practice.field.tracking'
    _inherit = ['mail.thread']
    _description = 'Field Tracking Demo'
    _order = 'sequence, id'

    name = fields.Char('Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=20)
    done = fields.Boolean('Request Done', tracking=True)  #

    def toggle_done(self):
        for s in self:
            s.done = not s.done
