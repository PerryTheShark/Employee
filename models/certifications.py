from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError

class Certifications(models.Model):
    _name = "employee.certification"
    _description = "certifications of employee"
    _order = "id desc"

# ---------------------------------------- Default Methods -------

# ---------------------------------------- Fields Declaration ----
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    expiration_date = fields.Date(string='Expiration Date')
    score = fields.Integer(string='Score')


    # Relational
    employee_id = fields.Many2many('hr.employee', string='Employee')
    skill_id = fields.Many2many('employee.skill.score', string='Skill')
    #----------------------------------------- Action Methods -------