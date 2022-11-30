from odoo import api, fields, models


class MenuMinuman(models.Model):
    _name = 'dapoeridita.menu_minuman'
    _description = 'Menu Minuman Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')