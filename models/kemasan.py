from odoo import api, fields, models


class Kemasan(models.Model):
    _name = 'dapoeridita.kemasan'
    _description = 'Kemasan Paket Dapoer Idita'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    stok = fields.Integer(string='Stok Kemasan Pengiriman')
    box = fields.Many2one(comodel_name="dapoeridita.kemasan_box", string="Pilihan Box", required=True)
    deskripsi_box = fields.Char(compute='_compute_deskripsi_box', string='Deskripsi Kemasan Box')

    @api.depends('box')
    def _compute_deskripsi_box(self):
        for record in self:
            record.deskripsi_box = record.box.deskripsi

    aksesoris_id = fields.Many2one(comodel_name="dapoeridita.kemasan_aksesoris", string='Pilihan Aksesoris',
                                   required=True)
    deskripsi_aksesoris = fields.Char(compute='_compute_deskripsi_aksesoris', string='Deskripsi Aksesoris')

    @api.depends('aksesoris_id')
    def _compute_deskripsi_aksesoris(self):
        for record in self:
            record.deskripsi_aksesoris = record.aksesoris_id.deskripsi
