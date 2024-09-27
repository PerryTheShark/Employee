from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError
from odoo.tools.populate import compute


class HrEmployee(models.Model):
    # ---------------------------------------- Private Attributes ------
    _inherit = "hr.employee"
    _description = 'this is a employee model extend from hr.employee'

    # ---------------------------------------- Default Methods -------

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
    certificate_number = fields.Integer(string='Certificate Number', compute='_compute_certificate_number')
    certification_skill = []

    # Relational
    certificate_ids = fields.Many2many('employee.certification', string='Certifications')
    skill_score_id = fields.Many2many('employee.skill.score', string='self skill')
    show_skill_score_id = fields.Many2many('employee.skill.score', string='total skill', compute='_compute_show_skill_score_id')

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

    def V2_open_experience_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Edit Certificates',
            'res_model': 'employee.batch.update.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_certification_ids': self.certificate_ids.ids,
            },
        }

    # ---------------------------------------- Constrains Methods -------
    # when we use api.contrains we do not need to declare it in the fields
    @api.constrains('years_of_experience')
    def _check_years_largest(self):
        for record in self:
            if record.years_of_experience > 30 or record.years_of_experience < 0:
                raise ValidationError("The years of experience cannot be larger than 30 or negative")
    # ---------------------------------------- Onchange Methods -------
    @api.onchange("certificate_ids", "years_of_experience")
    def _onchange_years_of_expoerience(self):
        for record in self:
            aws_certification = record.certificate_ids.filtered(lambda c: c.name == 'AWS')

            # If 'AWS' certification is found and years_of_experience is less than 2, set it to 2
            if aws_certification and record.years_of_experience < 2:
                record.years_of_experience = max(record.years_of_experience, 2)

    # ---------------------------------------- Compute and Search Methods -------

    @api.depends('certificate_ids')
    def _compute_certificate_number(self):
        for record in self:
            record.certificate_number = len(record.certificate_ids)

    @api.depends('certificate_ids')
    def _compute_show_skill_score_id(self):
        for record in self:
            # Start with the existing skill scores
            temp_skill_score_id = record.skill_score_id.ids
            # Add skills from certificates
            for cer in record.certificate_ids:
                temp_skill_score_id.extend(cer.skill_id.ids)
            # Update the show_skill_score_id field
            record.show_skill_score_id = [(6, 0, temp_skill_score_id)]

