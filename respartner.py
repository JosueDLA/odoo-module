# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    service = fields.Char(required=False, string="Servicio")
    url = fields.Char(required=False, string="URL")
    user = fields.Char(required=True, string="Usuario")
    password = fields.Char(required=True, string="Contraseña")
