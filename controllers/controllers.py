# -*- coding: utf-8 -*-
# from odoo import http


# class Dapoeridita(http.Controller):
#     @http.route('/dapoeridita/dapoeridita/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dapoeridita/dapoeridita/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dapoeridita.listing', {
#             'root': '/dapoeridita/dapoeridita',
#             'objects': http.request.env['dapoeridita.dapoeridita'].search([]),
#         })

#     @http.route('/dapoeridita/dapoeridita/objects/<model("dapoeridita.dapoeridita"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dapoeridita.object', {
#             'object': obj
#         })
