from odoo import api, fields, models


class Menu(models.Model):
    _name = 'dapoeridita.menu'
    _description = 'Deskripsi Menu Paket Dapoer Idita'

    name = fields.Char(string='Name')
    jenis = fields.Selection(string='Jenis Buku Menu',
                             selection=[('vegan', 'Vegan'), ('vegetarian', 'Vegetarian')])
    deskripsi = fields.Char(string='Deskripsi Menu')
    menu_lauk = fields.Many2one(comodel_name="dapoeridita.menu_lauk", string="Menu Lauk", required=True)
    menu_minuman = fields.Many2one(comodel_name="dapoeridita.menu_minuman", string="Menu Minuman", required=True)
    menu_protein = fields.Many2one(comodel_name="dapoeridita.menu_protein", string="Menu Protein", required=True)
    menu_tambahan = fields.Many2one(comodel_name="dapoeridita.menu_tambahan", string="Menu List Tambahan")

    deskripsi_protein = fields.Char(compute='_compute_deskripsi_protein', string='Deskripsi Menu Protein')

    @api.depends('menu_protein')
    def _compute_deskripsi_protein(self):
        for record in self:
            record.deskripsi_protein = record.menu_protein.deskripsi

    harga = fields.Monetary(compute="_compute_harga", string='Harga')

    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)
    currency_id = fields.Many2one('res.currency', related="company_id.currency_id")

    @api.depends('menu_protein', 'menu_minuman', 'menu_lauk', 'menu_tambahan')
    def _compute_harga(self):
        for record in self:
            record.harga = record.menu_protein.harga + record.menu_minuman.harga + record.menu_lauk.harga + record.menu_tambahan.harga

    deskripsi_minuman = fields.Char(compute='_compute_deskripsi_minuman', string='Deskripsi Menu Minuman')

    @api.depends('menu_minuman')
    def _compute_deskripsi_minuman(self):
        for record in self:
            record.deskripsi_minuman = record.menu_minuman.deskripsi

    deskripsi_lauk = fields.Char(compute='_compute_deskripsi_lauk', string='Deskripsi Menu Lauk')

    @api.depends('menu_lauk')
    def _compute_deskripsi_lauk(self):
        for record in self:
            record.deskripsi_lauk = record.menu_lauk.deskripsi

    deskripsi_tambahan = fields.Char(compute='_compute_deskripsi_tambahan', string='Deskripsi Menu List Tambahan')

    @api.depends('menu_tambahan')
    def _compute_deskripsi_tambahan(self):
        for record in self:
            record.deskripsi_tambahan = record.menu_tambahan.deskripsi
