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
        # if you are using master branch uncomment this part and comment the next one
        # 'mail.assets_messaging': [
        #     'mail_ext/static/src/models/composer_view.js',
        # ],

        # if your are using 15.0 branch use this and comment the above
        'mail.assets_discuss_public': [ # front end bundle
            'mail_ext/static/src/models/composer_view_15.js',
        ],
        'web.assets_backend': [ # banck end bundle
            'mail_ext/static/src/models/composer_view_15.js',
        ],
    },
    'license': 'LGPL-3',
}
