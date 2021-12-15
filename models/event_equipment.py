# -*- coding: utf-8 -*-

from odoo import models, fields, api

class event_equipment(models.Model):
    _name = 'rentalg1c.event_equipment'
    
    quantity = fields.Integer(string = "Quantity", required = True)
    
    event_id = fields.One2many('rentalg1c.event', id, string="Event")
    equipment_id = fields.One2many('rentalg1c.equipment', id, string="Equipment")
