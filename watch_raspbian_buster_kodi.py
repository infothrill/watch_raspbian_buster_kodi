#!/usr/bin/env python3

import sys
import gzip

import requests
from debian.deb822 import Deb822

URL = 'https://archive.raspbian.org/raspbian/dists/buster/main/binary-armhf/Packages.gz'
r = requests.get(URL, stream=True)
r.raw.decode_content = True
gzip_file = gzip.GzipFile(fileobj=r.raw)

package = 'kodi'
last_known_version = '2:17.6+dfsg1-4+b1'
for p in Deb822.iter_paragraphs(gzip_file):
    if p['Package'] == package:
        print('Current version: %s' % p['Version'])
        if p['Version'] != last_known_version:
            print('Version has changed from %s to %s' % (last_known_version, p['Version']))
            sys.exit(1)
        break
