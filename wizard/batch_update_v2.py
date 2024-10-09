from odoo import models, fields
from odoo.tools import groupby
from odoo.exceptions import UserError, ValidationError

class BatchUpdateWizardV2(models.TransientModel):
    _name = "employee.batch.update.wizard"
    _description = "Batch Update Wizard for hr.employee model"

    years_of_experience = fields.Integer(string='years of experience', default='0')
    certification_ids = fields.Many2many('employee.certification', string='Certifications')
    is_update_years_of_experience = fields.Boolean(string='Update')
    is_select_department = fields.Boolean(default=True)


    department_selection = fields.Selection(
        selection=lambda self: self.set_department_selection(),
        string='Department',
        default='all',
    )

    def set_department_selection(self):
        active_ids = self._context.get('active_ids', [])
        employees = self.env['hr.employee'].browse(active_ids)

        selection = [('all', 'All(%s)' % len(employees))]

        for department, group in groupby(employees, key=lambda x: x.department_id):
            if not department:
                continue
            count = len(list(group))
            selection.append((str(department.id), f"{department.name} ({count})"))

        employees_without_department = employees.filtered(lambda x: not x.department_id)
        if employees_without_department:
            selection.append(('no_department', 'No Department (%s)' % len(employees_without_department)))
        return selection

    def add_certificates_to_employees(self):
        active_ids = self.env.context.get('active_ids')
        all_employees = self.env['hr.employee'].browse(active_ids)

        employees = all_employees
        if self.department_selection:
            if self.department_selection == 'no_department':
                employees = employees.filtered(lambda rc: not rc.department_id)
            elif self.department_selection.isdigit():
                employees = employees.filtered(
                    lambda rc: rc.department_id.id == int(self.department_selection))
        elif self.is_select_department:
            raise UserError("Please select Department")

        if self.certification_ids:
            for employee in employees:
                employee.certificate_ids = [(4, cert.id) for cert in self.certification_ids]
        if self.years_of_experience and self.is_update_years_of_experience:
            for employee in employees:
                employee.years_of_experience = self.years_of_experience