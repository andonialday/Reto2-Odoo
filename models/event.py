# -*- coding: utf-8 -*-

from odoo import models, fields, api

class event(models.Model):
    _name = 'rentalg1c.event'
    
    name = fields.Char()
    dateStart = fields.Date()
    dateEnd = fields.Date()
    description = fields.Text()
    
    client = fields.Many2one('rentalg1c.client', ondelete='set null', string="Client")
    event_equipments = fields.One2many('rentalg1c.event_equipment', 'event_equipments', ondelete='set null', string="Rental")