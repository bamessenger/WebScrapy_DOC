# -*- mode: python -*-

block_cipher = None


a = Analysis(['C:\\Users\\brand\\OneDrive - InsureGood LLC\\Documents - Cedar Insights\\applications\\WebScrape\\DOC\\src\\main\\python\\WebScrapy_DOC\\main.py'],
             pathex=['C:\\Users\\brand\\OneDrive - InsureGood LLC\\Documents - Cedar Insights\\applications\\WebScrape\\DOC\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\users\\brand\\onedrive - insuregood llc\\documents - cedar insights\\applications\\webscrape\\doc\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\brand\\OneDrive - InsureGood LLC\\Documents - Cedar Insights\\applications\\WebScrape\\DOC\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='WebScrapy_DOC',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\brand\\OneDrive - InsureGood LLC\\Documents - Cedar Insights\\applications\\WebScrape\\DOC\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='WebScrapy_DOC')
