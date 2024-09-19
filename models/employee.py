from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError
from odoo.tools.populate import compute


class HrEmployee(models.Model):
    # ---------------------------------------- Private Attributes ------
    _inherit = "hr.employee"
    _description = 'this is a employee model extend from hr.employee'

    # ---------------------------------------- Default Methods -------

    # @api.model
    # def write(self,vals_list):
    #     res = super(HrEmployee, self).write(vals_list)
    #     if 'years_of_experience' in vals_list:
    #         for record in self:
    #             if record.years_of_experience < 0:
    #                 raise ValidationError("The years of experience must be positive")
    #     return res

    @api.model
    def create(self, vals):
        res = super(HrEmployee, self).create(vals)
        re_code = self.env['ir.sequence'].next_by_code('book.sequence')
        res.code = re_code
        return res
    # ---------------------------------------- Fields Declaration ----

    years_of_experience  = fields.Integer(string='years of experience', default='0', groups='Employee.group_employee_experience_manager')
    code = fields.Char(string='Code')
    the_past_company = fields.Char(string='The past company', groups='Employee.group_extended_experience_manager')


    # Relational
    certificate_ids = fields.Many2many('employee.certification', string='Certificates')
    score_id = fields.One2many('employee.skill.score', 'employee_id', string='Score')

    #----------------------------------------- Action Methods -------
    def open_experience_wizard(self):
        """Opens the wizard to edit years of experience."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Edit Years of Experience',
            'res_model': 'employee.batch.update',
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
    # ---------------------------------------- Onchange Methods -------
    @api.onchange("certificate_ids")
    def _onchange_years_of_expoerience(self):
        for record in self:
            aws_certification = record.certificate_ids.filtered(lambda c: c.name == 'AWS')

            # If 'AWS' certification is found and years_of_experience is less than 2, set it to 2
            if aws_certification and record.years_of_experience < 20:
                record.years_of_experience = 20
            # record.years_of_experience = max(record.years_of_experience, len(record.certificate_ids))
                # ValidationError('AWS is not a valid certificate')
                # record.years_of_experience = max(record.years_of_experience, 2)

    # ---------------------------------------- Compute and Search Methods -------
    @api.depends('certificate_ids')
    def _compute_years_of_experience(self):
        for record in self:
            if(record.certificate_ids.mapped('name') == 'AWS'):
                ValidationError('AWS is not a valid certificate')

