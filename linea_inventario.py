# -*- coding: utf-8 -*-

from odoo import models, fields

class linea_inventario(models.Model):
    _name = "linea.inventario"

    inventario = fields.Many2one('inventario.inventario')
    codigo = fields.Char('Codigo')
    producto = fields.Char('Producto')
    cantidad_tecnica = fields.Char('Cantidad Tecnica')
    cantidad_contada = fields.Char('Cantidad Contada')
