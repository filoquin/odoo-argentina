# -*- coding: utf-8 -*-
{
    "name": "Argentinian VAT Ledger Management",
    'version': '9.0.1.2.0',
    'category': 'Localization/Argentina',
    'sequence': 14,
    'author': 'ADHOC SA,Moldeo Interactive',
    'license': 'AGPL-3',
    'summary': '',
    "depends": [
        # TODO we should try to get this report with another tool, not aeroo
        "report_aeroo",
        "l10n_ar_account",
        "report_custom_filename",
        "date_range",
        # si agregamos account_fiscal_year vamos a requerir proyecto
        # financial-tools que requiere connector y mata performance de runbot
        # "account_fiscal_year",
    ],
    'external_dependencies': {
    },
    "data": [
        'account_vat_report_view.xml',
        'report/account_vat_ledger_report.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],
    'test': [
    ],
    'images': [
    ],
    "installable": True,
    'auto_install': True,
    'application': False,
}
