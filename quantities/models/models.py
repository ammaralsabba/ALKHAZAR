# -*- coding: utf-8 -*-

from odoo import models, fields, api

class quantities(models.Model):

    _inherit = 'sale.order'

    x_unit = fields.Float(compute="_total_of_all_quantity")
    x_cm = fields.Float(compute="_total_of_all_quantity")
    x_day = fields.Float(compute="_total_of_all_quantity")
    x_dozen = fields.Float(compute="_total_of_all_quantity")
    x_foot = fields.Float(compute="_total_of_all_quantity")
    x_inch = fields.Float(compute="_total_of_all_quantity")
    x_kg = fields.Float(compute="_total_of_all_quantity")
    x_sqm = fields.Float(compute="_total_of_all_quantity")
    x_liter = fields.Float(compute="_total_of_all_quantity")


    def _total_of_all_quantity(self):
      for order in self:
        for line_qty in order.order_line:
            if 'Unit' in line_qty.product_uom.name:
              order.x_unit += line_qty.product_uom_qty
            if 'cm' in line_qty.product_uom.name:
              order.x_cm += line_qty.product_uom_qty
            if 'Day' in line_qty.product_uom.name:
              order.x_day += line_qty.product_uom_qty
            if 'Dozen' in line_qty.product_uom.name:
              order.x_dozen += line_qty.product_uom_qty
            if 'foot' in line_qty.product_uom.name:
              order.x_foot += line_qty.product_uom_qty
            if 'inch(es)' in line_qty.product_uom.name:
              order.x_inch += line_qty.product_uom_qty
            if 'kg' in line_qty.product_uom.name:
              order.x_kg += line_qty.product_uom_qty
            if 'SQM' in line_qty.product_uom.name:
              order.x_sqm += line_qty.product_uom_qty
            if 'Liter' in line_qty.product_uom.name:
              order.x_liter += line_qty.product_uom_qty


class quantity(models.Model):

    _inherit = 'account.invoice'


    i_unit = fields.Float(compute="_total_of_all_quantity")
    i_cm = fields.Float(compute="_total_of_all_quantity")
    i_day = fields.Float(compute="_total_of_all_quantity")
    i_dozen = fields.Float(compute="_total_of_all_quantity")
    i_foot = fields.Float(compute="_total_of_all_quantity")
    i_inch = fields.Float(compute="_total_of_all_quantity")
    i_kg = fields.Float(compute="_total_of_all_quantity")
    i_sqm = fields.Float(compute="_total_of_all_quantity")
    i_liter = fields.Float(compute="_total_of_all_quantity")


    def _total_of_all_quantity(self):
        for invoice in self:
           for line_qty in invoice.invoice_line_ids:
            if 'Unit' in line_qty.uom_id.name:
              invoice.i_unit += line_qty.quantity
            if 'cm' in line_qty.uom_id.name:
              invoice.i_cm += line_qty.quantity
            if 'Day' in line_qty.uom_id.name:
              invoice.i_day += line_qty.quantity
            if 'Dozen' in line_qty.uom_id.name:
              invoice.i_dozen += line_qty.quantity
            if 'foot' in line_qty.uom_id.name:
              invoice.i_foot += line_qty.quantity
            if 'inch(es)' in line_qty.uom_id.name:
              invoice.i_inch += line_qty.quantity
            if 'kg' in line_qty.uom_id.name:
              invoice.i_kg += line_qty.quantity
            if 'SQM' in line_qty.uom_id.name:
              invoice.i_sqm += line_qty.quantity
            if 'Liter' in line_qty.uom_id.name:
              invoice.i_liter += line_qty.quantity

