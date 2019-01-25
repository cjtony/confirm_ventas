# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class ConfirmVentas(models.Model):
	_inherit = 'sale.order'
	
	pruebacampo = fields.Text(string="prueba de campo")
	user_validation = fields.Many2one('res.users', string="Validado Por: ")
	user_approve = fields.Many2one('res.users', string="Aprobado por: ")

	state = fields.Selection(selection_add=[('to_validate','Validar'),('to_approve','Aprobar')])

	@api.one
	def action_validate(self):
		self.write({'state': 'to_validate'})
		self.write({'user_validation' : self.env.user.id})
		#user_validation = self.env.user.name

	@api.one
	def action_aprobe(self):
		self.write({'state':'to_approve'})
		self.write({'user_approve' : self.env.user.id})
		#user_approve = self.env.user.id

	#raise UserError(user_validation)
	#return (ConfirmVentas, self).action_validate

	
