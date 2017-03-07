# -*- coding: utf-8 -*-

from odoo import models, fields, api
import base64
import re

class Inventario(models.Model):
    _name = "inventario.inventario"

    name = fields.Char('Nombre')
    inventario = fields.One2many('linea.inventario', 'inventario')
    archivo = fields.Binary('Archivo')

    @api.model
    def create(self, vals):
        record = super(Inventario, self).create(vals)

        file_content = base64.b64decode(record.archivo)

        lines = file_content.split("\n")

        rows = []
        for line in lines:
            codigo = re.search('^(.{15})', line)
            producto = re.search('^.{15}(.{45})', line)
            cantidad_tecnica = re.search('^.{15}.{45}(.+)', line)

            if codigo and producto and cantidad_tecnica:
                rows.append([codigo.group(1).strip(), producto.group(1).strip(), cantidad_tecnica.group(1).strip()])

        for index in range(len(rows)):
            self.env['linea.inventario'].create({
                'inventario': record.id,
                'codigo': rows[index][0],
                'producto': rows[index][1],
                'cantidad_tecnica': rows[index][2]
            })

        return record
