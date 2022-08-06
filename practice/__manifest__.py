# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Practicing',
    'version' : '1.2',
    'summary': 'Just for Practicing',
    'sequence': 10,
    'description': """
Practicing
====================
Just for Practicin
""",
    'category': 'Website/Website',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['website'],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web._assets_primary_variables': [
        ],
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            # Here is own work
        ],
        'web.assets_tests': [

        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
        ],
    },
    'license': 'LGPL-3',
}
