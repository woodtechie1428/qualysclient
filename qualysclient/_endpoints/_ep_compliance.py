_compliance_endpoints = [
    [
        'compliance_control_list', 
        '/api/2.0/fo/compliance/control/?action=list', 
        [

            {
                'param_name': 'echo_request'

            },
            {
                'param_name': 'details'
            },
            {
                'param_name': 'ids'
            },
            {
                'param_name': 'id_min'
            },
            {
                'param_name': 'id_max'
            },
            {
                'param_name': 'id_min'
            },
            {
                'param_name': 'updated_after_datetime'
            },
            {
                'param_name': 'created_after_datetime'
            },
            {
                'param_name': 'truncation_limit'
            }           
        ]
    ],
    [
         'compliance_policy_list', 
         '/api/2.0/fo/compliance/policy/?action=list',
         [
             {
                 'param_name': 'echo_request', 
             },
             {
                 'param_name': 'details'
             },
             {
                 'param_name': 'ids'
             },
             {
                 'param_name': 'id_min'
             },
             {
                 'param_name': 'id_max'
             },
             {
                 'param_name': 'updated_after_datetime'
             },
             {
                 'param_name': 'created_after_datetime'
             }           

         ]
    ],
    [
        'compliance_policy_export',
        '/api/2.0/fo/compliance/policy/?action=export',
        [
            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'id',
            },
                        {
                'param_name': 'title',
            },
                        {
                'param_name': 'show_user_controls',
            },
                        {
                'param_name': 'show_appendix',
            }

        ]
    ],
    [
        'compliance_policy_import',
        '/api/2.0/fo/compliance/policy/?action=import',
        [

            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'xml_file',
                'is_required': True
            },
            {
                'param_name': 'title',
                'is_required': True
            },
            {
                'param_name': 'create_user_controls'
            }
        ]
    ],
    [
        'compliance_policy_merge',
        '/api/2.0/fo/compliance/policy/?action=merge',
        [

            {
                'param_name': 'id',
                'is_required': True
            },
            {
                'param_name': 'merge_policy_id',
                'is_required': True
            },
            {
                'param_name': 'replace_cover_page'
            },
            {
                'param_name': 'replace_asset_groups'
            },
            {
                'param_name': 'add_asset_groups'
            },
            {
                'param_name': 'add_new_technologies'
            },
            {
                'param_name': 'add_new_controls'
            },
            {
                'param_name': 'update_section_heading'
            },
            {
                'param_name': 'update_existing_controls'
            },
            {
                'param_name': 'preview_merge'
            }
            
        ]
    ],
    [
        'compliance_policy_add_asset_group_ids',
        '/api/2.0/fo/compliance/policy/?action=add_asset_group_ids',
        [
            {
                'param_name': 'id',
                'is_required': True
            },
            {
                'param_name': 'asset_group_ids',
                'is_required': True
            },
            {
                'param_name': 'evaluate_now'
            },            
        ]
    ],
    [
        'compliance_policy_set_asset_group_ids',
        '/api/2.0/fo/compliance/policy/?action=set_asset_group_ids',
        [
            {
                'param_name': 'id',
                'is_required': True
            },
            {
                'param_name': 'asset_group_ids',
                'is_required': True
            },
            {
                'param_name': 'evaluate_now'
            },            
        ]
    ],
    [
        'compliance_policy_add_asset_groups',
        '/api/2.0/fo/compliance/policy/?action=add_asset_group_ids',
        [
            {
                'param_name': 'id',
                'is_required': True
            },
            {
                'param_name': 'asset_group_ids',
                'is_required': True
            },
            {
                'param_name': 'evaluate_now'
            },            
        ]
    ],
    [
        'compliance_posture_list',
        '/api/2.0/fo/compliance/posture/info/?action=list',
        [
            {
                'param_name': 'policy_id',
                'is_required': True
            },
            {
                'param_name': 'policy_ids'
            },
            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'output_format'
            },
            {
                'param_name': 'details'
            },
            {
                'param_name': 'hide_evidence'
            },
            {
                'param_name': 'include_dp_name'
            },
            {
                'param_name': 'show_remediation_info'
            },
            {
                'param_name': 'cause_of_failure'
            },
            {
                'param_name': 'truncation_limit'
            },
            {
                'param_name': 'ips'
            },
            {
                'param_name': 'host_ids'
            },
            {
                'param_name': 'control_ids'
            },
            {
                'param_name': 'ids'
            },
            {
                'param_name': 'id_min'
            },
            {
                'param_name': 'id_max'
            },
            {
                'param_name': 'status_changes_since'
            },
            {
                'param_name': 'evaluation_date'
            },
            {
                'param_name': 'asset_group_ids'
            },
            {
                'param_name': 'status'
            },
            {
                'param_name': 'criticality_labels'
            },
            {
                'param_name': 'criticality_values'
            },
            {
                'param_name': 'tag_set_by'
            },
            {
                'param_name': 'tag_include_selector'
            },
            {
                'param_name': 'tag_exclude_selector'
            },
            {
                'param_name': 'tag_set_include'
            },
            {
                'param_name': 'tag_set_exclude'
            }
        ]
    ],
    [
        'compliance_exception_list',
        '/api/2.0/fo/compliance/exception/?action=list',
        [
            {
                'param_name': 'exception_number'
            },
            {
                'param_name': 'ip',
            },
            {
                'param_name': 'network_name',
            },
            {
                'param_name': 'status',
            },
            {
                'param_name': 'control_id',
            },
            {
                'param_name': 'control_statement',
            },
            {
                'param_name': 'policy_id',
            },
            {
                'param_name': 'technology_name',
            },
            {
                'param_name': 'assignee_id',
            },
            {
                'param_name': 'created_by',
            },
            {
                'param_name': 'modified_by',
            },
            {
                'param_name': 'details',
            },
            {
                'param_name': 'is_active',
            },
            {
                'param_name': 'created_after_date',
            },
            {
                'param_name': 'updated_after_date',
            },
            {
                'param_name': 'expired_before_date',
            },
            {
                'param_name': 'expired_after_date',
            },
            {
                'param_name': 'exception_numbers',
            },
            {
                'param_name': 'exception_number_min',
            },
            {
                'param_name': 'exception_number_max',
            },
            {
                'param_name': 'truncation_limit',
            }

        ]
    ],
    [
        'compliance_exception_request',
        '//api/2.0/fo/compliance/exception/?action=request',
        [
            {
                'param_name': 'control_id',
                'is_required': True
            },
            {
                'param_name': 'host_id',
                'is_required': True
            },
            {
                'param_name': 'policy_id',
                'is_required': True
            },
            {
                'param_name': 'technology_id',
                'is_required': True
            },
            {
                'param_name': 'instance_string',
            },
            {
                'param_name': 'assignee_id',
                'is_required': True
            },
            {
                'param_name': 'comments',
                'is_required': True
            },
            {
                'param_name': 'reopen_on_evidence_change',
            }

        ]
    ],
    [
        'compliance_exception_update',
        '//api/2.0/fo/compliance/exception/?action=update',
        [
            {
                'param_name': 'exception_numbers',
                'is_required': True
            },
            {
                'param_name': 'comments',
                'is_required': True
            },
            {
                'param_name': 'reassign_to',
            },
            {
                'param_name': 'reopen_on_evidence_change',
            },
            {
                'param_name': 'status',
            },
            {
                'param_name': 'end_date',
            }

        ]
    ],
    [
        'compliance_exception_delete',
        '//api/2.0/fo/compliance/exception/?action=delete',
        [
            {
                'param_name': 'exception_numbers',
                'is_required': True
            }

        ]
    ],
    
]