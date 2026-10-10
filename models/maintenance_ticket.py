from odoo import api, fields, models


class MaintenanceTicket(models.Model):
    _name = 'maintenance.ticket'
    _description = 'Maintenance Ticket'

    name = fields.Char(
        string='Ticket Name',
        compute='_compute_name',
        store=True,
        readonly=True,
    )
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('responsible.user', string='Responsible', required=True)
    status = fields.Selection(
        [('new', 'New'), ('in_progress', 'In Progress'), ('done', 'Done'), ('cancel', 'Cancel')],
        string='Status',
        default='new',
    )
    done_date=fields.Date(string="Done Date" , readonly=True)

    date = fields.Date(string='Date', default=fields.Date.today)
    done_date = fields.Datetime(string='Done Date')
    model_id = fields.Many2one('maintenance.model', string='Maintenance Model', required=True)
    visit_ids= fields.One2many('visit.details', 'ticket_id', string='Visits')

    @api.depends('customer_id', 'model_id')
    def _compute_name(self):
        for rec in self:
            model_name = rec.model_id.name if rec.model_id else ''
            customer_name = rec.customer_id.name if rec.customer_id else ''
            if model_name and customer_name:
                rec.name = f'{model_name} {customer_name}'
            elif model_name:
                rec.name = model_name
            elif customer_name:
                rec.name = customer_name
            else:
                rec.name = 'Unnamed Ticket'

    def action_start(self):
        for rec in self:
            rec.status = 'in_progress'
    def action_cancel(self):
        for rec in self:
                rec.status = 'cancel'
    def action_done(self):
        for rec in self:
            rec.status='done'
            rec.done_date=fields.Date.today()
    def action_reopen(self):
        for rec in self:
            rec.status = 'new'

