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
        'wizard/batch_update.xml',
        'data/employee.xml',
        'views/menu.xml'
    ],
    "application": True,
    "license": "LGPL-3",
}
