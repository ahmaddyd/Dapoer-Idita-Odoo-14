from odoo import api, fields, models


class Box(models.Model):
    _name = 'dapoeridita.kemasan_box'
    _description = 'Kemasan Box Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
