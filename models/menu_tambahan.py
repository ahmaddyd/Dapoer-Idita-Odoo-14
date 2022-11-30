from odoo import api, fields, models


class MenuTambahan(models.Model):
    _name = 'dapoeridita.menu_tambahan'
    _description = 'Deskripsi Menu List Tambahan Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
