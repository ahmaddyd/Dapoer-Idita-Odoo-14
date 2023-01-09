from odoo import api, fields, models


class MenuTambahan(models.Model):
    _name = 'dapoeridita.menu_tambahan'
    _description = 'Deskripsi Menu List Tambahan Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Monetary(string='Harga')
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
