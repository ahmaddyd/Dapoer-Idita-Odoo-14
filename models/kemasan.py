from odoo import api, fields, models


class Kemasan(models.Model):
    _name = 'dapoeridita.kemasan'
    _description = 'Deskripsi Kemasan Paket Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Monetary(string='Harga')
    stock = fields.Integer(string='Stok Kemasan Pengiriman')
    box = fields.Many2one(comodel_name="dapoeridita.kemasan_box", string="Pilihan Box", required=True)
    deskripsi_box = fields.Char(compute='_compute_deskripsi_box', string='Deskripsi Kemasan Box')

    @api.depends('box')
    def _compute_deskripsi_box(self):
        for record in self:
            record.deskripsi_box = record.box.deskripsi

    kemasan_aksesoris = fields.Many2one(comodel_name="dapoeridita.kemasan_aksesoris", string='Pilihan Aksesoris',
                                   required=True)
    deskripsi_aksesoris = fields.Char(compute='_compute_deskripsi_aksesoris', string='Deskripsi Aksesoris')

    @api.depends('kemasan_aksesoris')
    def _compute_deskripsi_aksesoris(self):
        for record in self:
            record.deskripsi_aksesoris = record.kemasan_aksesoris.deskripsi

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")
