# -*- coding: utf-8 -*-
{
'name': "gestiondirecciones",

    'summary': """
        Módulo para la gestión de direcciones ip""",

    'description': """
        EL presente módulo 
    """,

    'author': "David",
    'website': " ",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menusyacciones.xml',
        'views/control_gestiondirecciones.xml',
        'views/usuario_gestiondirecciones.xml',
    ],
  
}
