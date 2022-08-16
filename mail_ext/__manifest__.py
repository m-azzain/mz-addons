# -*- coding: utf-8 -*-
{
    'name' : 'Mail Ext',
    'version' : '1.0',
    'summary': 'Just for Practicing',
    'sequence': 200,
    'description': """
Email
====================
Just to practice what can be customized in emil addon
""",
    'category': 'Productivity/Discuss',
    'depends' : ['mail'],
    'data': [
    ],
    'demo': [
    ],
    'installable': True,
    #'application': True,
    'assets': {
        'web._assets_primary_variables': [
        ],
        'web.assets_backend': [
        ],
        'web.assets_frontend': [

        ],
        'web.assets_tests': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
        ],
        'mail.assets_messaging': [
            'mail_ext/static/src/models/composer_view.js',
        ],
    },
    'license': 'LGPL-3',
}
