from odoo import api, fields, models


class MenuLauk(models.Model):
    _name = 'dapoeridita.menu_lauk'
    _description = 'Deskripsi Menu Lauk Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
