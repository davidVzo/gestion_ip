import string
from odoo import models, fields

class control(models.Model):
	_name = 'control.gestiondirecciones'
	_description = 'Control de usuarios e ip'

	cod_usuario = fields.Many2one('usuario.gestiondirecciones',string="Cédula del usuario",required=True)
	cod_vlan = fields.Many2one('vlan.gestionvlan',string="Vlan",required=True)
	observaciones = fields.Text(string="Observaciones")

	""""
	id_sala = fields.Many2one('sala.gestionhospital',string="Número de la sala",required=True)
	id_paciente_cita = fields.Many2one('paciente.gestionhospital',string="DNI del paciente",required=True)
	fecha = fields.Date(string="Fecha de la cita", required=True)
	especialidad = fields.Text(string="Especialidad")
"""