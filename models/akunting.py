from email.policy import default
from odoo import api, fields, models


class Akunting(models.Model):
    _name = 'dapoeridita.akunting'
    _description = 'Deskripsi Akunting Daper Idita'
    _order = 'id asc'

    name = fields.Char(string='Nama')
    kode_akunting = fields.Char(string='Kode Akunting')
    tanggal = fields.Datetime(string='Date', default = fields.Datetime.now())
    debet = fields.Integer(string='Debet')
    cash = fields.Integer(string='Cash')
    kredit = fields.Integer(string='Kredit')
    saldo = fields.Float(compute='_compute_saldo', string='Saldo')
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")

    @api.depends('debet','kredit','cash')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id','<',record.id)],limit=1, order='tanggal desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.cash + record.kredit - record.debet

