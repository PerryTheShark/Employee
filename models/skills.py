from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError
from odoo.tools.populate import compute


class Skills(models.Model):
    _name = "employee.skill"
    _description = "skill"
    _order = "id desc"
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

    name = fields.Char(string='Skill Name', required=True)
    #-----------------------------------------   SQL Constraints   ---------------------
    _sql_constraints = [
        ('check_level_progress', 'CHECK(level_progress BETWEEN 0 AND 100)', "Progress should be a number between 0 and 100."),

    ]

    # ---------------------------------------- Fields Declaration ----------------------
    level_progress = fields.Integer(string="Progress", help="Progress from zero knowledge (0%) to fully mastered (100%).")
    color = fields.Integer("Color Index")

    # Relational
    skill_id = fields.Many2one('employee.skill', string='Skill')
    employee_id = fields.Many2many('hr.employee', string='Employee')

    @api.depends('level_progress', 'skill_id')
    def name_get(self):
        result = []
        for record in self:
            # Construct the display name as "Skill Name (Level Progress%)"
            name = f"{record.skill_id.name} ({record.level_progress}%)"
            result.append((record.id, name))
        return result

    @api.constrains('level_progress', 'skill_id')
    def _check_unique_skill_level(self):
        for record in self:
            existing_records = self.search([
                ('skill_id', '=', record.skill_id.id),
                ('level_progress', '=', record.level_progress),
                ('id', '!=', record.id)
            ])
            if existing_records:
                raise ValidationError("A skill score with the same level progress already exists for this skill.")