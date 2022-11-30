from odoo import http, fields, models
from odoo.http import request
import json

class KemasanControllers(http.Controller):
    @http.route(['/kemasan','/kemasan/<int:idnya>'],auth='public', methods = ['GET'], csrf = True)
    def getKemasan(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            package = request.env['dapoeridita.kemasan'].search([])
            for k in package:
                value.append({"id": k.id,
                              "namakemasan" : k.name,
                              "deskripsi" : k.deskripsi,
                              "stok_tersedia" : k.stock,
                              "harga" : k.harga,})
            return json.dumps(value)
        else:
            packageid = request.env['dapoeridita.kemasan'].search([('id','=',idnya)])
            for k in packageid:
                value.append({"id": k.id,
                              "namakemasan" : k.name,
                              "deskripsi" : k.deskripsi,
                              "stok_tersedia" : k.stock,
                              "harga" : k.harga})
            return json.dumps(value)

    @http.route('/createkemasan',auth = 'user', type = 'json', methods = ['POST'])
    def createKemasan(self, **kw):
        if request.jsonrequest:
            if kw['name']:
                vals = {
                    'name' : kw['name'],
                    'deskripsi' : kw['deskripsi'],
                    'stock' : kw['stock'],
                    'harga' : kw['harga'],
                    'box' : kw['box'],
                    'aksesoris' : kw['kemasan_aksesoris']
                }
                packagebaru = request.env['dapoeridita.kemasan'].create(vals)
                args = {'succeed': True, "ID" : packagebaru}
                return args

