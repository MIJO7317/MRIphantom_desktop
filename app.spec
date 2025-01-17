# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files
import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None
excluded_modules = ['torch.distributions']
datas = [('studies', 'studies'), ('assets', 'assets'), ('UI', 'UI')]
datas += collect_data_files('timm', include_py_files=True)

a = Analysis(
    ['app.py'],
    pathex=['C:\\dev\\git\\MRIphantom_desktop', 'C:\\dev\\git\\MRIphantom_desktop\\src'],
    binaries=[],
    datas=datas,
    hiddenimports=['dcm2niix', 'vtk', 'vtk.qt', 'pydicom.encoders.gdcm', 'pydicom.encoders.pylibjpeg', 'PySide6.QtWebEngineWidgets', 'QtWebEngineWidgets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excluded_modules,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)

app = BUNDLE(
    coll,
    name='app.app',
    icon=None,
    bundle_identifier=None,
)
