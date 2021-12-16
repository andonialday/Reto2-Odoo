# -*- coding: utf-8 -*-

from odoo import models, fields, api

class user(models.Model):
    _name = 'res.users'
    _inhertit = 'res.users'
    
    privilege = fields.Selection([('0','USER'),('1','ADMIN')], string='Privilege', default='0')
    status = fields.Boolean(default='True')
    lastPasswordChange = fields.Char()