# -*- coding: utf-8 -*-

from odoo import models, fields, api

class user(models.Model):
    _name = 'res.users'
    _inhertit = 'res.users'
    
    privilege = fields.Char()
    status = fields.Boolean()
    lastPasswordChange = fields.Char()