from odoo import models, fields

class WizardReapertura(models.TransientModel):
    _name = 'tarea.wizard_reapertura'

    motivo_reapertura = fields.Text(string='Motivo de reapertura', required=True)
    fecha_limite_nueva = fields.Datetime(string='Fecha Límite', required=True)

    def confirmar_reapertura(self):
  
        tarea = self.env['tareas.lista_tarea'].browse(self.env.context.get('active_id'))
        if tarea and tarea.categoria == 'atrasado':
            tarea.write({'categoria': 'pendiente'})

        return {'type': 'ir.actions.act_window_close'}
