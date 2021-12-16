# -*- coding: utf-8 -*-

from odoo import models, fields, api

class event_equipment(models.Model):
    _name = 'rentalg1c.event_equipment'
    
    quantity = fields.Integer(string = "Quantity", required = True)
    
    event = fields.One2many('rentalg1c.event', 'event_equipments', string="Event")
    equipment = fields.One2many('rentalg1c.equipment', 'event_equipments', string="Equipment")
