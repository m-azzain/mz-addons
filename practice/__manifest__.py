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
    'depends' : ['website'],
    'data': [
        'views/practice_templates.xml',
    ],
    'icon': 'practice/static/description/practice.png',
    'demo': [
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web._assets_primary_variables': [
            'practice/static/src/scss/primary_variables.scss'
        ],
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            # Here is own work
            'practice/static/src/scss/navbar.scss'
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
