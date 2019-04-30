# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.queue_job.job import job
import logging

_logger = logging.getLogger(__name__)


class AccountInvoiceExtend(models.Model):
   _inherit = 'account.invoice'

   @api.multi
   def button_do_stuff(self):
       self.env['account.invoice.line'].with_delay().my_method('a', k=2)


class AccountInvoiceLineExtend(models.Model):
    _inherit = 'account.invoice.line'

    @api.multi
    @job
    def my_method(self, a, k=None):
        _logger.info('executed with a: %s and k: %s', a, k)