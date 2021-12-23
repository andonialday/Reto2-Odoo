# -*- coding: utf-8 -*-

from odoo import models, fields

class client(models.Model):
    _name = 'rentalg1c.client'
    _inhertit = 'res.users'

    type = fields.Selection([('0','PARTICULAR'),('1','ASOCIATION'),('2','ENTERPRISE'),('3','PUBLIC_ENTITY')], string='Type', default='0')

    event = fields.One2many('rentalg1c.event', 'client', ondelete='set null', string='Event')
    commercial = fields.Many2one('rentalg1c.commercial', ondelete='set null', string='Commercial')