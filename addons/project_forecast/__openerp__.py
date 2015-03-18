# -*- coding: utf-8 -*-
{
    'name': "Project Forecast",

    'summary': """Resource management for Project""",

    'description': """
    Ressource management for Project
    """,
    'category': 'Project Management',

    'author': "OpenERP SA",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_forecast_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
    'application': True,
}
