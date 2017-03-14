# -*- coding: utf-8 -*-
from odoo import http
from odoo import models

class Inventario(http.Controller):
    @http.route('/api/inventario/', auth='user', type='json', methods=['POST'], csrf=False)
    def index(self, telegram_chat_id, codigo_de_producto, cantidad_contada):

        partners = http.request.env['res.partner']
        partner = partners.search([('telegram_chat_id','=', telegram_chat_id)])

        inventarios = http.request.env['inventario.inventario']
        inventario_partner = inventarios.search([('partner', '=', partner.id)])

        linea_inventarios = http.request.env['linea.inventario']
        inventario_linea_inventario = inventario_partner.inventario

        linea_inventario_codigo = linea_inventarios.search([('id', '=', inventario_linea_inventario.id)]).codigo

        if len(inventario_partner) >= 1:
            inventario_linea_inventario.cantidad_contada = cantidad_contada

            return {
                        "response": "OK",
                        "data": {
                                    "partner": partner.id,
                                    "linea_inventario": inventario_linea_inventario.id,
                                    "codigo": linea_inventario_codigo
                                }
                    }
        else:
            return {
                        "response": "ERROR"
                    }

#     @http.route('/inventario/inventario/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventario.listing', {
#             'root': '/inventario/inventario',
#             'objects': http.request.env['inventario.inventario'].search([]),
#         })

#     @http.route('/inventario/inventario/objects/<model("inventario.inventario"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventario.object', {
#             'object': obj
#         })
