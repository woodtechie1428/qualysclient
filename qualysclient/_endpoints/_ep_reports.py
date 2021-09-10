_reports_endpoints = [
    [
        'list_reports', 
        '/api/2.0/fo/report/?action=list', 
        [
            {
                'param_name': 'echo_request'

            },
            {
                'param_name': 'id',
                'description': 'some description'
            },
            {
                'param_name': 'state'
            }
            
        ]
    ],
    [
         'launch_report', 
         '/api/2.0/fo/report/?action=launch',
         [
             {
                 'param_name': 'template_id',
                 'is_required': True
             }
         ]
    ],
    [
        'launch_scorecard',
        '/api/2.0/fo/report/scorecard/?action=launch',
        [
            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'name'
            },
            {
                'param_name': 'report_title'
            },
            {
                'param_name': 'output_format'
            },

        ]
    ],
    [
        'cancel_running_report',
        '/api/2.0/fo/report/?action=cancel',
        [
            {
                'param_name': 'id',
                'is_required': True
            },
            {
                'param_name': 'echo_request'
            },
        ]
    ],
    [
        'download_saved_report',
        '/api/2.0/fo/report/?action=fetch',
        [
            {
                'param_name': 'id',
                'is_required': True
            },
            {
                'param_name': 'echo_request'
            },
        ]
    ]
    
]