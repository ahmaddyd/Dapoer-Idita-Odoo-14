from email.policy import default
from odoo import api, fields, models


class Contact(models.Model):
    _inherit = 'res.partner'

    is_pegawai = fields.Boolean(string='Pegawai', default=False)
    is_pelanggan = fields.Boolean(string='Pelanggan', default=False)
