from email.policy import default
from odoo import api, fields, models


class OrderPesananSelesai(models.Model):
    _name = 'dapoeridita.order_pesanan_selesai'
    _description = 'Daftar Orderan sudah dikirim'

    name = fields.Char(compute='_compute_nama_pelanggan', string='Nama Pelanggan')
    order_ids = fields.Many2one(comodel_name='dapoeridita.order_pesanan', string='Order',
                                domain="[('sudah_dikirim','=',False)]")
    tanggal_dikirim = fields.Date(string='Tanggal Pengiriman', default=fields.Date.today())
    tagihan = fields.Char(compute='_compute_tagihan', string='Tagihan')

    @api.depends('order_ids')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_ids.total

    @api.depends('order_ids')
    def _compute_nama_pelanggan(self):
        for record in self:
            record.name = self.env['dapoeridita.order_pesanan'].search([('id', '=', record.order_ids.id)]).mapped(
                'pelanggan_id').name

    @api.model
    def create(self, vals):
        record = super(OrderPesananSelesai, self).create(vals)
        if record.tanggal_dikirim:
            self.env['dapoeridita.order_pesanan'].search([('id', '=', record.order_ids.id)]).write(
                {'sudah_dikirim': True})
            if record.s.metode_bayar == 'kredit':
                self.env['dapoeridita.akunting'].create({'kredit': record.tagihan, 'name': record.name})
            else:
                self.env['dapoeridita.akunting'].create({'cash': record.tagihan, 'name': record.name})
            return record

    def unlink(self):
        for ahmad in self:
            self.env['dapoeridita.order_pesanan'].search([('id', '=', ahmad.order_ids.id)]).write(
                {'sudah_dikirim': False})
        record = super(OrderPesananSelesai, self).unlink()
