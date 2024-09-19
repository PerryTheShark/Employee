from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError

class Skills(models.Model):
    _name = "employee.skill"
    _description = "skill"
    _order = "id desc"
    # ---------------------------------------- Default Methods -------

    # ---------------------------------------- Fields Declaration ----
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

    # Relational
    score_id = fields.One2many('employee.skill.score','skill_id' , string='Score')
    # ------------------------

class SkillScore(models.Model):
    _name = "employee.skill.score"
    _description = "score of skill of employee"
    _order = "id desc"
    # ---------------------------------------- Default Methods -------

    # ---------------------------------------- Fields Declaration ----
    score = fields.Integer(string='Score')

    # Relational
    skill_id = fields.Many2one('employee.skill', string='Skill')
    employee_id = fields.Many2one('hr.employee', string='Employee')