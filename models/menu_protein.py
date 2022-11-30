from odoo import api, fields, models


class MenuProtein(models.Model):
    _name = 'dapoeridita.menu_protein'
    _description = 'Deskripsi Menu Protein Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    images = fields.Binary(string='Gambar Makanan')
