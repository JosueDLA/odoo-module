# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    servicios = fields.One2many(
        'res.partner.services', 'service_id', string='Servicios')


class Partner_list():
    _name = 'res.partner.services'

    service = fields.Char(required=False, string="Servicio")
    url = fields.Char(required=False, string="URL")
    user = fields.Char(required=True, string="Usuario")
    password = fields.Char(required=True, string="Contraseña")

    service_id = fields.Many2one('res.partner', string='Partner Id')
