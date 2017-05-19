# -*- coding: utf-8 -*-

from openerp import models, fields, api, _

class citasjmo_cita(models.Model):
	_name = 'citasjmo.cita'
	
	autor = fields.Char(string='Autor', required=True, help='Autor de la Cita')
	cita = fields.Text('Cita', required=True, help='Inserte la Cita')
	fecha = fields.Date(string='Fecha de visualizacion', required=True, help='Fecha de visualizacion')
	orden = fields.Integer(string='Orden de visualizacion', required=False, help='Orden de visualizacion')