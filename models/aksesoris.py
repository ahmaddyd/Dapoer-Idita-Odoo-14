from odoo import api, fields, models


class Aksesoris(models.Model):
    _name = 'dapoeridita.kemasan_aksesoris'
    _description = 'Kemasan Aksesoris Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')


