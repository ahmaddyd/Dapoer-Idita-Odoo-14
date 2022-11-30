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
        'views/menu_minuman_views.xml',
        'views/menu_protein_views.xml',
        'views/menu_tambahan_views.xml',
        'views/akunting_dapoer_idita_views.xml',
        'views/order_pesanan_views.xml',
        'views/order_pesanan_selesai_views.xml',
        'views/kemasan_views.xml',
        'views/aksesoris_kemasan_views.xml',
        'views/kemasan_box_views.xml',
        'views/pegawai_views.xml',
        'views/pelanggan_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
