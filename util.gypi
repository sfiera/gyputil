{
    'target_defaults': {
        'conditions': [
            ['OS=="mac"', {
                'sources/': [
                    ['exclude', '/(win|linux)/'],
                ],
                'include_dirs/': [
                    ['exclude', '/(win|linux)$'],
                ],
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
                'sources/': [
                    ['exclude', '/(mac|linux|posix)/'],
                ],
                'include_dirs/': [
                    ['exclude', '/(mac|linux|posix)$'],
                ],
            }],
            ['OS=="linux"', {
                'sources/': [
                    ['exclude', '/(mac|win)/'],
                ],
                'include_dirs/': [
                    ['exclude', '/(mac|win)$'],
                ],
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
