from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

class BatchUpdateWizard(models.TransientModel):
    _name = "employee.batch.update"
    _description = "Batch Update Wizard for hr.employee model"

    years_of_experience = fields.Integer(string='years of experience', default='0')

    def multi_update(self):
        active_ids = self.env.context.get('active_ids')
        employees = self.env['hr.employee'].browse(active_ids)
        new_data = {}
        if self.years_of_experience:
            new_data["years_of_experience"] = self.years_of_experience

        employees.write(new_data)
