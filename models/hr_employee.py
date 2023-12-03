# -*- coding: utf-8 -*- 

from odoo import models, fields, _,api
from odoo.exceptions import ValidationError


class HrEmployeePrivate(models.Model):
    _inherit = 'hr.employee'

    birth_act = fields.Char(string='Birth act',index=True,copy=False)
    blood_type = fields.Selection([('a+','A+'),
                                   ('a-','A-'),
                                   ('b+','B+'),
                                   ('b-','B-'),
                                   ('ab+','AB+'),
                                   ('ab-','AB-'),
                                   ('o+','O+'),
                                   ('o-','O-'),],index=True,copy=False)
    spouse_at_home = fields.Boolean(string='Spouse at home',copy=False)
    schoolchildren = fields.Integer(string='School children',copy=False)
    disabledchildren = fields.Integer(string='Disabled children',copy=False)

    @api.onchange('marital')
    def onchange_marital(self):
        self.spouse_at_home = False
