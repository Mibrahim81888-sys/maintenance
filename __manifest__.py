{
    'name': 'Maintenance',
    'version': '1.0',
    'summary': 'Maintenance Management System',
    'category': 'Services',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/maintenance_ticket_views.xml',
        'reports/maintenance_ticket_reports.xml',
        

    ],
    'installable': True,
    'application': True,
}