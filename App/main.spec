# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# Define base path for each OS
if sys.platform == 'win32':
    base_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
else:
    base_path = os.path.abspath(os.path.join(os.getcwd(), '..'))

# Define paths for data and binary files
datas = [
    (os.path.join(base_path, 'App', 'Config', 'config.ini'), 'Config'),
    (os.path.join(base_path, 'App', 'Classes'), 'Classes'),
    (os.path.join(base_path, 'App', 'Config'), 'Config'),
    (os.path.join(base_path, 'App', 'Data'), 'Data'),
    (os.path.join(base_path, 'App', 'Fonts'), 'Fonts'),
    (os.path.join(base_path, 'App', 'Music'), 'Music'),
    (os.path.join(base_path, 'App', 'Tools'), 'Tools'),
]

a = Analysis(
    ['main.py'],
    pathex=[base_path],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'numpy',
        'pygame.surfarray',
        'pygame.sndarray',
        'pygame.error',
        'pygame.register_quit'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main'
)
