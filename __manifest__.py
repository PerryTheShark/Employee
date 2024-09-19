# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html
{
    "name": "Human resources",
    "depends": [
        "base",
        "web",
        "hr",
    ],
    "data": [
        'security/employee_security.xml',
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/certification_views.xml',
        'views/skill_views.xml',
        'views/skill_score_views.xml',
        'wizard/batch_update.xml',
        'wizard/batch_update_v2.xml',
        'data/employee.xml',
        'views/menu.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'D:/Odoo16/odoo/addons/hr_skills/static/src/fields/skills_one2many.xml',
            'D:/Odoo16/odoo/addons/hr_skills/static/src/fields/*',
            'D:/Odoo16/odoo/addons/hr_skills/static/src/scss/*.scss',
            'D:/Odoo16/odoo/addons/hr_skills/static/src/views/*.js',
            'D:/Odoo16/odoo/addons/hr_skills/static/src/xml/**/*',
        ],
        'web.assets_tests': [
            'hr_skills/static/tests/tours/*',
        ],
    },
    "application": True,
    "license": "LGPL-3",
}
