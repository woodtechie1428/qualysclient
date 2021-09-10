_assets_endpoints = [
    [
        'list_ip', 
        '/api/2.0/fo/asset/ip/?action=list', 
        [

            {
                'param_name': 'echo_request'

            },
            {
                'param_name': 'ips',
                'description': '(Optional) Show only certain IP addresses/ranges. One or more IPs/ranges may be specified. Multiple entries are comma separated. A host IP range is specified with a hyphen (for example, 10.10.10.44-10.10.10.90).'
            },
            {
                'param_name': 'network_id'
            },
            {
                'param_name': 'tracking_method'
            }
            
        ]
    ],
    [
         'add_ips', 
         '/api/2.0/fo/asset/ip/?action=add',
         [
             {
                 'param_name': 'action', 
                 'is_required': True
             },
             {
                 'param_name': 'ips',
                 'is_required': True
             }
         ]
    ],
    [
        'update_ips',
        '/api/2.0/fo/asset/ip/?action=update',
        [
            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'show_asset_id',
            },
                        {
                'param_name': 'details',
            },
                        {
                'param_name': 'os_pattern',
            },
                        {
                'param_name': 'truncation_limit',
            },
                        {
                'param_name': 'ips',
            },
                        {
                'param_name': 'show_asset_id',
            },
                        {
                'param_name': 'no_vm_scan_since'
            },

        ]
    ],
    [
        'host_list',
        '/api/2.0/fo/asset/host/?action=list',
        [

            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'show_asset_id'
            },
            {
                'param_name': 'details'
            },
            {
                'param_name': 'os_pattern'
            },
            {
                'param_name': 'truncation_limit',
                'default': '10'
            },
            {
                'param_name': 'ips'
            },
            {
                'param_name': 'ipv6'
            },
            {
                'param_name': 'ag_ids'
            },
            {
                'param_name': 'ag_titles'
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
                'param_name': 'network_ids'
            },
            {
                'param_name': 'compliance_enabled'
            },
            {
                'param_name': 'no_vm_scan_since'
            },
            {
                'param_name': 'no_compliance_scan_since'
            },
            {
                'param_name': 'vm_scan_since'
            },
            {
                'param_name': 'compliance_scan_since'
            },
            {
                'param_name': 'vm_processed_before'
            },
            {
                'param_name': 'vm_processed_after'
            },
            {
                'param_name': 'vm_scan_date_before'
            },
            {
                'param_name': 'vm_scan_date_after'
            },
            {
                'param_name': 'vm_auth_scan_date_before'
            },
            {
                'param_name': 'vm_auth_scan_date_after'
            },
            {
                'param_name': 'scap_scan_since'
            },
            {
                'param_name': 'no_scap_scan_since'
            },

            {
                'param_name': 'use_tags'
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
            },
            {
                'param_name': 'show_tags'
            },
            {
                'param_name': 'host_metadata'
            },
            {
                'param_name': 'host_metadata_fields'
            },
            {
                'param_name': 'show_cloud_tags'
            },
            {
                'param_name': 'cloud_tag_fields'
            },
            
        ]
    ],

    [
        'host_list_detection',
        '/api/2.0/fo/asset/host/vm/detection/?action=list',
        [

            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'show_results'
            },
            {
                'param_name': 'show_reopened_info'
            },
            {
                'param_name': 'arf_kernel_filter'
            },
            {
                'param_name': 'arf_service_filter'
            },
            {
                'param_name': 'arf_config_filter'
            },
            {
                'param_name': 'active_kernels_only'
            },
            {
                'param_name': 'output_format'
            },
            {
                'param_name': 'suppress_duplicated_data_from_csv'
            },
            {
                'param_name': 'truncation_limit'
            },
            {
                'param_name': 'max_days_since_detection_updated'
            },
            {
                'param_name': 'detection_updated_since'
            },
            {
                'param_name': 'detection_updated_before'
            },
            {
                'param_name': 'detection_processed_before'
            },
            {
                'param_name': 'detection_processed_after'
            },
            {
                'param_name': 'detection_last_tested_since'
            },
            {
                'param_name': 'detection_last_tested_since_days'
            },
            {
                'param_name': 'detection_last_tested_before'
            },
            {
                'param_name': 'detection_last_tested_before_days'
            },
            {
                'param_name': 'include_ignored'
            },
            {
                'param_name': 'include_disabled'
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
                'param_name': 'ips'
            },
            {
                'param_name': 'ipv6'
            },
            {
                'param_name': 'ag_ids'
            },
            {
                'param_name': 'ag_titles'
            },
            {
                'param_name': 'network_ids'
            },
            {
                'param_name': 'vm_scan_since'
            },
            {
                'param_name': 'no_vm_scan_since'
            },
            {
                'param_name': 'max_days_since_last_vm_scan'
            },
            {
                'param_name': 'vm_processed_before'
            },
            {
                'param_name': 'vm_processed_after'
            },
            {
                'param_name': 'vm_scan_date_before'
            },
            {
                'param_name': 'vm_scan_date_after'
            },
            {
                'param_name': 'vm_auth_scan_date_before'
            },
            {
                'param_name': 'vm_auth_scan_date_after'
            },
            {
                'param_name': 'status'
            },
            {
                'param_name': 'compliance_enabled'
            },
            {
                'param_name': 'os_pattern'
            },
            {
                'param_name': 'qids'
            },
            {
                'param_name': 'severities'
            },
            {
                'param_name': 'filter_superseded_qids'
            },
            {
                'param_name': 'show_igs'
            },
            {
                'param_name': 'include_search_list_titles'
            },
            {
                'param_name': 'exclude_search_list_titles'
            },
            {
                'param_name': 'include_search_list_ids'
            },
            {
                'param_name': 'exclude_search_list_ids'
            },
            {
                'param_name': 'use_tags'
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
            },
            {
                'param_name': 'show_tags'
            },
            {
                'param_name': 'host_metadata'
            },
            {
                'param_name': 'host_metadata_fields'
            },
            {
                'param_name': 'show_cloud_tags'
            },
            {
                'param_name': 'cloud_tag_fields'
            },
            {
                'param_name': 'LAST_SCAN_DATETIME'
            },
            {
                'param_name': 'LAST_VM_SCANNED_DATE'
            },
            {
                'param_name': 'LAST_VM_SCANNED_DURATION'
            },
            {
                'param_name': 'LAST_VM_AUTH_SCANNED_DATE'
            },
            {
                'param_name': 'LAST_VM_AUTH_SCANNED_DURATION'
            },
            {
                'param_name': 'LAST_PC_SCANNED_DATE'
            },
            {
                'param_name': 'FIRST_FOUND_DATETIME'
            },
            {
                'param_name': 'LAST_FOUND_DATETIME'
            },
            {
                'param_name': 'LAST_TEST_DATETIME'
            },
            {
                'param_name': 'LAST_UPDATE_DATETIME'
            },
            {
                'param_name': 'LAST_FIXED_DATETIME'
            }          

            
        ]
    ],
    [
        'excluded_host_list',
        '/api/2.0/fo/asset/excluded_ip/?action=list',
        [
            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'ips'
            },
            {
                'param_name': 'network_id'
            },
            {
                'param_name': 'ag_ids'
            },
            {
                'param_name': 'ag_titles'
            },
            {
                'param_name': 'use_tags'
            },
            {
                'param_name': 'tag_include_selector'
            },
            {
                'param_name': 'tag_exclude_selector'
            },
            {
                'param_name': 'tag_set_by'
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
        'excluded_host_change_history',
        '/api/2.0/fo/asset/excluded_ip/history/?action=list',
        [
            {
                'param_name': 'echo_request'
            },
            {
                'param_name': 'ips'
            },
            {
                'param_name': 'network_id'
            },
            {
                'param_name': 'id_min'
            },
            {
                'param_name': 'id_max'
            },
            {
                'param_name': 'ids'
            }
            
        ]
    ]
    
    
]