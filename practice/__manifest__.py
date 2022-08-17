# -*- coding: utf-8 -*-
{
    'name' : 'Practicing',
    'version' : '1.0',
    'summary': 'Just for Practicing',
    'sequence': 10,
    'description': """
Practicing
====================
Just for Practicing
""",
    'category': 'Website/Website',
    'depends' : ['website'],
    'data': [
        'data/res_user_data.xml',
        'views/practice_templates.xml',
        'security/ir.model.access.csv',
        'views/email_demo_views.xml',
        'views/kanban_demo_views.xml',
        'views/field_tracking_demo_views.xml',
        'views/practice_menus.xml',
        'data/kanban_demo_data.xml',
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
