# -*- coding: utf-8 -*-
{
    'name': "DAPOER IDITA",

    'summary': """
       Dapoer Idita merupakan Pemesanan Tempat Makanan secara 
       online yang dapat menjangkau lapisan menengah ke bawah terutama pelajar dan mahasiswa.""",

    'description': """
        Tempat Pemesanan makanan menengah ke bawah
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '1.2',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/menu_views.xml',
        'views/menu_lauk_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
