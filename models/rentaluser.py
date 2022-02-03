# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class client(models.Model):
    _name = 'rentalg1c.usr'

    login = fields.Char(required=True)
    name = fields.Char(required=True)
    email = fields.Char(required=True)
    password = fields.Char()
    lastPasswordChange = fields.Date()
    
    status = fields.Selection([('0', 'ENABLED'), ('1', 'DISABLED')], string='Type', default='0')
    privilege = fields.Selection([('0', 'USER'), ('1', 'ADMIN')], string='Type', default='0')