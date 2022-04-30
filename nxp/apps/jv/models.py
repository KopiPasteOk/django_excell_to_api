from datetime import datetime, timedelta
from .models import *
from django.utils import timezone
from django.db import models

# Create your models here.
class JV(models.Model):
    no_jv = models.CharField(max_length=100, blank=True, null=True)  # a
    no_akun = models.CharField(max_length=100, blank=True, null=True)  # b
    tgl_jv = models.CharField(max_length=100, blank=True, null=True)  # c
    nama_akun = models.CharField(
        max_length=100, blank=True, null=True)  # d
    keterangan = models.CharField(max_length=100, blank=True, null=True)  # e
    debit = models.CharField(max_length=250, blank=True, null=True)  # f
    kredit = models.CharField(max_length=100, blank=True, null=True)  # g
    nama_dep = models.CharField(max_length=100, blank=True, null=True)  # h

    def __str__(self):
        return f"{self.nama_pelanggan}"

    def generate_json_all_date(self):
        data_to_summarize = {}
        for dt in Invoice().objects.all():
            debit = dt.debit.replace(".", "").replace(",","")
            kredit = dt.kredit.replace(".", "").replace(",","")
            detil = {
                "accountCode": dt.no_akun,  # B
                "debitAmount": debit,  # F
                "creditAmount": kredit,  # G
                "currencyCode": "IDR",  # static
                "currencyRate": 1,  # static
                "description": dt.keterangan,  # E
                "locCode": "HO",  # static
                "deptCode": dt.nama_dep,  # H
                "prjCode": ""  # null
            }
            if data_to_summarize.get(dt.nama_pelanggan) is None:
                {
                    "no": dt.no_jv,  # A
                    "dt": dt.tgl_jv,  # C
                    "reviewDate": dt.tgl_jv,  # C
                    "approveddDate": dt.tgl_jv,  # C
                    "type": "1",  # static
                    "locCode": "HO",  # static
                    "createBy": "retailsoft",  # static
                    "reviewedBy": "retailsoft",  # static
                    "approvedBy": "retailsoft",  # static
                    "remark": "TEST ",  # static
                    "details": [detil],
                    "item_joined": 1,  # helper
                }
            else:
                data_to_summarize[dt.nama_pelanggan]["item_joined"] += 1
                data_to_summarize[dt.nama_pelanggan]["details"].append(detail)

        return data_to_summarize