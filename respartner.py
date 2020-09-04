# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    partners = fields.One2many('res.partner.services.list', 'partner_id', string='Partners')


class PartnerList(models.Model):
    _name = 'res.partner.services.list'
    _description = 'Service List'

    partner_id = fields.Many2one('res.partner.services', strin='Partner')
    service = fields.Char(required=False, string="Servicio")
    url = fields.Char(required=False, string="URL")
    user = fields.Char(required=True, string="Usuario")
    password = fields.Char(required=True, string="Contraseña")



