# -*- coding: utf-8 -*-
from odoo import http
from odoo import models

class Inventario(http.Controller):
    @http.route('/api/inventario/', auth='user', type='json', methods=['POST'], csrf=False)
    def index(self, telegram_chat_id, codigo_de_producto, cantidad_contada):

        partners = http.request.env['res.partner']
        partner = partners.search([('telegram_chat_id','=', telegram_chat_id)])

        inventarios = http.request.env['inventario.inventario']
        inventario = inventarios.search([('partner', '=', partner.id)])

        linea_inventarios = http.request.env['linea.inventario']
        linea_inventario = linea_inventarios.search([('codigo', '=', codigo_de_producto)])


        if len(inventario) >= 1:
            linea_inventario.cantidad_contada = cantidad_contada

            return {
                        "response": "OK",
                        "inventario_partner": len(inventario),
                        "data": {
                                    "partner": partner.id,
                                    "codigo": linea_inventario.codigo
                                }
                    }
        else:
            return {
                        "response": "NO",
                        "inventario_partner": len(inventario),
                        "data": {
                                    "partner": partner.id,
                                    "codigo": linea_inventario.codigo
                                }
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
