# -*- coding: utf-8 -*-

from odoo import models, fields, api

class event_equipment(models.Model):
    _name = 'rentalg1c.event_equipment'
    
    quantity = fields.Integer(string = "Quantity", required = True)
    
    event = fields.Many2one('rentalg1c.event', ondelete='set null', string="Event")
    equipment = fields.Many2one('rentalg1c.equipment', ondelete='set null', string="Equipment")
