from odoo import api, fields, models


class MenuTambahan(models.Model):
    _name = 'dapoeridita.menu_tambahan'
    _description = 'Daftar macam pilihan makanan tambahan Homade Catering'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')