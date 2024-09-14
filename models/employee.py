from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError

class HrEmployee(models.Model):
    # ---------------------------------------- Private Attributes ------
    _inherit = "hr.employee"
    _description = 'this is a employee model extend from hr.employee'

    # ---------------------------------------- Default Methods -------
    def action_button_test(self):
        raise UserError("An offer as already been accepted.")

    @api.model
    def write(self,vals_list):
        res = super(HrEmployee, self).write(vals_list)
        if 'years_of_experience' in vals_list:
            for record in self:
                if record.years_of_experience < 0:
                    raise ValidationError("The years of experience must be positive")
        return res

    @api.model
    def create(self, vals):
        res = super(HrEmployee, self).create(vals)
        re_code = self.env['ir.sequence'].next_by_code('book.sequence')
        res.code = re_code
        return res
    # ---------------------------------------- Fields Declaration ----

    years_of_experience  = fields.Integer(string='years of experience', default='0', groups='Employee.group_employee_experience_manager')
    code = fields.Char(String='Code')
    the_past_company = fields.Char(string='The past company', groups='Employee.group_extended_experience_manager')


    # Relational

    #----------------------------------------- Action Methods -------
    def open_experience_wizard(self):
        """Opens the wizard to edit years of experience."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Edit Yearsof Experience',
            'res_model': 'employee.batch.update.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_years_of_experience': self.years_of_experience,
            },
        }

    # ---------------------------------------- Constrains Methods -------
    # when we use api.contrains we do not need to declare it in the fields
    @api.constrains('years_of_experience')
    def _check_years_largest(self):
        for record in self:
            if record.years_of_experience > 30:
                raise ValidationError("The years of experience cannot be larger than 30")
