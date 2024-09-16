from odoo import  models, fields, api
from odoo.api import constrains
from odoo.exceptions import UserError, ValidationError

class HrEmployee(models.Model):
    # ---------------------------------------- Private Attributes ------
    _inherit = "employee.skills"
    _description = 'this is a table skill for employee'

    # ---------------------------------------- Default Methods -------

    # ---------------------------------------- Fields Declaration ----



    # Relational

    #----------------------------------------- Action Methods -------


    # ---------------------------------------- Constrains Methods -------
    # when we use api.contrains we do not need to declare it in the fields
