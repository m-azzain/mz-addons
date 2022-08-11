
from odoo import api, fields, models

class SaleOrder(models.Model):
    _name = 'email.demo'
    _inherit = ['mail.thread']
    _description = "Email Demo"

    partner_id = fields.Many2one(comodel_name='res.partner', string="Receiver", required=True)
    random_check_1 = fields.Boolean(string="Random Check 1")
    random_check_2 = fields.Boolean(string="Random Check 2")

    def action_send_mail(self):
        # Do whatever logic you have with these random_check_1, random_check_1 and if you decide to send the email execute the next line.
        self.message_post(body='Hello, From the email demo. <br/> Email Demo body', subject='email demo subject', partner_ids=self.partner_id.ids)
