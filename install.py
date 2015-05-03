#!/usr/bin/env python3

import glob
import shutil
import os

INSTALL_DIR = '/etc/foopkg/rules.d'

if os.geteuid() != 0:
	raise PermissionError('You forgot a sudo. Please use one.')

toinstall = glob.glob('*.json')
os.makedirs(INSTALL_DIR, exist_ok=True, mode=0o755)
for f in toinstall:
	srcpath = os.path.join(os.curdir, f)
	shutil.copy(srcpath, INSTALL_DIR)
	print('Installed', f)