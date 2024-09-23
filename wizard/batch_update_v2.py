from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

class BatchUpdateWizardV2(models.TransientModel):
    _name = "employee.batch.update.wizard"
    _description = "Batch Update Wizard for hr.employee model"

    years_of_experience = fields.Integer(string='years of experience', default='0')
    certification_ids = fields.Many2many('employee.certification', string='Certifications')
    is_update_years_of_experience = fields.Boolean(string='Update')

    def add_certificates_to_employees(self):
        active_ids = self.env.context.get('active_ids')
        employees = self.env['hr.employee'].browse(active_ids)
        if self.certification_ids:
            for employee in employees:
                employee.certificate_ids = [(4, cert.id) for cert in self.certification_ids]
        if self.years_of_experience and self.is_update_years_of_experience:
            for employee in employees:
                employee.years_of_experience = self.years_of_experience