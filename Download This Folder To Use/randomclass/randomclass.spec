# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew

block_cipher = None


a = Analysis(['randomclass.py'],
             pathex=['C:\\Users\\geoff\\OneDrive\\Desktop\\Randomgen'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [('randomclass.kv', 'C:\\Users\\geoff\\OneDrive\\Desktop\\Randomgen\randomclass.kv', 'DATA')]

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='randomclass',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree('C:\\Users\\geoff\\OneDrive\\Desktop\\Randomgen'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in
               (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='randomclass')
