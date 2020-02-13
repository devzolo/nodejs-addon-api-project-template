{
  'variables': {
    'platform': '<(OS)',
    'build_arch': '<!(node -p "process.arch")',
    'build_win_platform': '<!(node -p "process.arch==\'ia32\'?\'Win32\':process.arch")',
  },
  'conditions': [
    # Replace gyp platform with node platform, blech
    ['platform == "mac"', {'variables': {'platform': 'darwin'}}],
    ['platform == "win"', {'variables': {'platform': 'win32'}}],
  ],
  'targets': [
    {
      'target_name': 'example',
      'sources': [
        'src/example.c'
      ],
      'defines' : ['UNICODE'],
      'libraries': [],
      'include_dirs' : [],
      'library_dirs' : [],
    },
    {
      "target_name": "copy_modules",
      "type":"none",
      "dependencies" : [ "example" ],
      "copies":[
        {
          'destination': '<(module_root_dir)\\bin\\<(platform)\\<(target_arch)',
          'files': [
            '<(module_root_dir)\\build\\Release\\example.node',
          ]
        },
      ]
    }
  ]
}
