{
    'variables': {
        'mac_file_pattern': '(^|/)(mac|posix)(/|$)',
        'win_file_pattern': '(^|/)(win)(/|$)',
        'linux_file_pattern': '(^|/)(linux|posix)(/|$)',
    },
    'target_defaults': {
        'sources/': [
            ['exclude', '<(mac_file_pattern)'],
            ['exclude', '<(win_file_pattern)'],
            ['exclude', '<(linux_file_pattern)'],
        ],
        'include_dirs/': [
            ['exclude', '<(mac_file_pattern)'],
            ['exclude', '<(win_file_pattern)'],
            ['exclude', '<(linux_file_pattern)'],
        ],
        'conditions+': [
            ['OS=="mac"', {
                'sources/': [['include', '<(mac_file_pattern)']],
                'include_dirs/': [['include', '<(mac_file_pattern)']],
                'xcode_settings': {
                    'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
                    'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
                    'SDKROOT': 'macosx10.4',
                    'GCC_VERSION': '4.0',
                    'ARCHS': 'ppc x86_64 i386',
                    'WARNING_CFLAGS': [
                        '-Wall',
                        '-Wendif-labels',
                    ],
                },
            }],
            ['OS=="win"', {
                'sources/': [['include', '<(win_file_pattern)']],
                'include_dirs/': [['include', '<(win_file_pattern)']],
            }],
            ['OS=="linux"', {
                'sources/': [['include', '<(linux_file_pattern)']],
                'include_dirs/': [['include', '<(linux_file_pattern)']],
            }],
        ],
    },
    'targets': [
        {
            'target_name': 'check-deps',
            'type': 'none',
            'actions': [
                {
                    'action_name': 'check-deps',
                    'inputs': [ ],
                    'outputs': [ ],
                    'action': [
                        '<(DEPTH)/ext/gyputil/check-deps.sh',
                        '<(DEPTH)',
                    ],
                },
            ],
        },
    ],
}
