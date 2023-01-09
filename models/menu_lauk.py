from odoo import api, fields, models


class MenuLauk(models.Model):
    _name = 'dapoeridita.menu_lauk'
    _description = 'Deskripsi Menu Lauk Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Monetary(string='Harga')
    images = fields.Binary(string='Gambar Makanan')
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
