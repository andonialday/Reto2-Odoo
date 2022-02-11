# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class event(models.Model):
    _name = 'rentalg1c.event'
    
    name = fields.Char()
    dateStart = fields.Date()
    dateEnd = fields.Date()
    description = fields.Text()
    
    client = fields.Many2one('rentalg1c.client', ondelete='set null', string="Client")
    event_equipments = fields.One2many('rentalg1c.event_equipment', 'event', ondelete='set null', string="Rental")
    
    @api.constrains('dateEnd', 'dateStart')
    def _verify_valid_end_date(self):
        for record in self:
            if record.dateEnd < record.dateStart:
                raise ValidationError("The Event cannot have an Ending Date earlier than the Starting Date")
            
    @api.onchange('dateEnd', 'dateStart')
    def _control_valid_end_date(self):    
        if self.dateEnd and self.dateStart:
            if self.dateEnd < self.dateStart:
                return {
                    'warning': {
                    'title': "Incorrect Date End",
                    'message': "The Event cannot have an Ending Date earlier than the Starting Date",
                    },
                }