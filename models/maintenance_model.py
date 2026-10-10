from odoo import models, fields, api

class MaintenanceModel(models.Model):
    _name = 'maintenance.model'
    _description = 'Maintenance Model'

    name = fields.Char(string='Name', required=True)
