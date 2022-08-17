
from odoo import api, fields, models


class EmailDemo(models.Model):
    _name = 'practice.email.demo'
    _inherit = ['mail.thread']
    _description = "Email Demo"

    res_partner_1 = fields.Boolean(string="Partner 1")
    res_partner_2 = fields.Boolean(string="Partner 2")
    res_partner_3 = fields.Boolean(string="Partner 3")
    res_partner_4 = fields.Boolean(string="Partner 4")

    @property
    def receivers_selection_map(self):
        # These partners are already in the system from demo data,
        # You should check they exists in your system,
        # Or you can replace them by others
        return {'res_partner_1': self.env.ref('base.res_partner_1'),
               'res_partner_2': self.env.ref('base.res_partner_2'),
               'res_partner_3': self.env.ref('base.res_partner_3'),
               'res_partner_4': self.env.ref('practice.practice_partner_1')}

    def action_send_mail(self):
        selected_partners = [p.id for k, p in self.receivers_selection_map.items() if self[k]]
        self.message_post(body='Hello, From the email demo. <br/> Email Demo body',
                          subject='email demo subject', partner_ids=selected_partners)

    # To display the fields by partner names in the form
    @api.model
    def fields_get(self, allfields=None, attributes=None):
        result = super().fields_get(allfields=allfields, attributes=attributes)
        for k in self.receivers_selection_map:
            result[k]['string'] = self.receivers_selection_map[k].display_name
        return result
