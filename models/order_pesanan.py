from email.policy import default
from odoo import api, fields, models
import datetime
from odoo.exceptions import ValidationError


class OrderPesanan(models.Model):
    _name = 'dapoeridita.order_pesanan'
    _description = 'Order Pesanan Dapoer Idita'

    detailorderpesanan_ids = fields.One2many(comodel_name='dapoeridita.detail_order_pesanan', inverse_name='order_ids',
                                             string='Details Order')
    pelanggan_id = fields.Many2one(comodel_name="res.partner", string="Pelanggan", required=True,
                                   domain="[('is_pelanggan','=','true')]")
    alamat = fields.Char(string='Alamat Pengiriman', required=True)
    total = fields.Integer(compute='_compute_total', string='Total', store=True)
    name = fields.Char(string='Kode Order', required=True)
    metode_pembayaran = fields.Selection(string='Metode Pembayaran', selection=[('kredit', 'Kredit'), ('cash', 'Cash')],
                                         required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', default=fields.Date.today(), required=True)
    tanggal_pengiriman = fields.Datetime(string='Tanggal Pengiriman',
                                         default=fields.Datetime.now() + datetime.timedelta(days=1), required=True)
    sudah_dikirim = fields.Boolean(string='Sudah Dikirim', default=False)

    @api.depends('detailorderpesanan_ids')
    def _compute_total(self):
        for record in self:
            a = sum(
                self.env['dapoeridita.detail_order_pesanan'].search([('order_ids', '=', record.id)]).mapped('harga'))
            record.total = a

    def barang_dikirim(self):
        pass


class DetailOrderPesanan(models.Model):
    _name = 'dapoeridita.detail_order_pesanan'
    _description = 'Detail Order Pesanan Dapoer Idita'

    menu_id = fields.Many2one(comodel_name='dapoeridita.menu', string='Menu Paket Makanan')
    kemasan_id = fields.Many2one(comodel_name='dapoeridita.kemasan', string='Kemasan Paket Makanan')
    order_ids = fields.Many2one(comodel_name='homade.order', string='Order')
    name = fields.Selection(string='Name',
                            selection=[('makanan', 'Menu Paket Makanan'), ('packaging', 'Kemasan Paket Makanan')])
    harga = fields.Integer(compute='_compute_harga', string='Harga')

    qty = fields.Integer(string='Jumlah')

    harga_makanan = fields.Integer(compute='_compute_harga_makanan', string='Harga Makanan')

    harga_kemasan = fields.Integer(compute='_compute_harga_kemasan', string='Harga Kemasan')

    @api.constrains('qty')
    def _check_stock(self):
        for record in self:
            bahan = self.env['dapoeridita.kemasan'].search([('stock', '<', record.qty), ('id', '=', record.id)])
            if bahan:
                raise ValidationError("Stok Kemasan Paket yang dipilih tidak cukup")

    @api.depends('menu_id')
    def _compute_harga_makanan(self):
        for record in self:
            record.harga_makanan = record.menu_id.harga

    @api.depends('kemasan_id')
    def _compute_harga_kemasan(self):
        for record in self:
            record.harga_kemasan = record.kemasan_id.harga

    @api.depends('harga_makanan', 'harga_kemasan', 'qty')
    def _compute_harga(self):
        for record in self:
            record.harga = record.harga_makanan * record.qty + record.harga_kemasan * record.qty

    @api.model
    def create(self, vals):
        record = super(DetailOrderPesanan, self).create(vals)
        if record.qty:
            self.env['dapoeridita.kemasan'].search([('id', '=', record.kemasan_id.id)]).write(
                {'stock': record.kemasan_id.stock - record.qty})
            return record
