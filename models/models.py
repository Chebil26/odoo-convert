# -*- coding: utf-8 -*-

from odoo import models, fields, api
import pandas as pd
import base64
import tempfile
import xlwt
import io 
from io import StringIO, BytesIO

from xlwt import easyxf


class co(models.Model):
    _name = 'co.co'
    # _description = 'co.co'
    # name = fields.Char()
    # value = fields.Integer()
    # description = fields.Text()

    file_pcc = fields.Binary(string="Fichier pccompta", readonly=False)
    name_file_pcc = fields.Char('Nom du fichier pcc')

    file_odoo = fields.Binary(string="Fichier odoo", readonly=True)
    file_odoo_name = fields.Char('Nom du fichier odoo')


    def do(self):

        file =tempfile.TemporaryFile(suffix=".xls")
        file.write(base64.decodestring(self.file_pcc))
        dff = pd.read_excel(file)

        #dff = pd.read_excel(BytesIO(self.file_pcc))

        # workbook = xlwt.Workbook()
        # worksheet = workbook.add_sheet('odoo')

        date =  dff['DATE'].tolist()
        ref = dff['LIBELLE'].tolist()
        j_id = dff['CODE_JRN'].tolist()
        ref2 = []

        date3 = []

        j_id3 = []

        i = 0
        while i < len(ref):
            if ref[i] == ref[i-1]:
                ref2.append('')
                date3.append('')
                j_id3.append('')
            else:
                ref2.append(ref[i])
                date3.append(date[i])
                j_id3.append(j_id[i])

            i = i + 1



        df1 = pd.DataFrame({'date': date3,
                    'ref': ref2,
                    'journal_id': j_id3,
                    'account_id': dff['CODE_COM'].tolist(),
                    'name': dff['LIBELLE'].tolist(),
                    'partner_id': dff['CODE_AUX'].tolist(),
                    'debit': dff['DEBIT'].tolist(),
                    'credit': dff['CREDIT'].tolist(),
                    })



        # workbook = xlwt.Workbook()
        # worksheet = workbook.add_sheet('df1')
        # cell_style = easyxf('font:height 200;font:bold False;borders:left 2;borders:right 2;borders:top 2;borders:bottom 2;')
        # worksheet.write(0 , 0, "test", cell_style)
        fp2 = io.BytesIO()
        #workbook.save(fp2)

        df1.to_excel(fp2, sheet_name='Sheet2' , index=False)


        self.file_odoo = base64.encodestring(fp2.getvalue())
        self.file_odoo_name = 'odoo.xls'

        # output = BytesIO()
        # writer = pd.ExcelWriter(output)

        # df1.to_excel(writer)
        # writer.save()
        # self.file_odoo = output.getvalue()










#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
