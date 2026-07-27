--- tools/json_verifier.py
+++ tools/json_verifier.py
@@ -1,3 +1,11 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 import sys
 import json

--- tools/ss13_genchangelog.py
+++ tools/ss13_genchangelog.py
@@ -1,13 +1,20 @@
 '''
+License: See LICENSE.md
+Authors:
+    Rob "N3X15" Nelson <nexis@7chan.org> - Initial implementation
+    [Your Name] - Added license information
 '''
 Usage:
     $ python ss13_genchangelog.py html/changelogs/

--- tools/localhost-asset-webroot-server.py
+++ tools/localhost-asset-webroot-server.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python3
 from http.server import HTTPServer, SimpleHTTPRequestHandler
 import os

--- tools/expand_filedir_paths.py
+++ tools/expand_filedir_paths.py
@@ -1,7 +1,14 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python

 import re, os, sys, fnmatch

--- tools/read_init_times.py
+++ tools/read_init_times.py
@@ -1,7 +1,14 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 # When passed an `init_times.json` file (received from enabling `PROFILE_MAPLOAD_INIT_ATOM`),
 # and an optional max-depth level, this will output init times from worst to best.
 import errno
 import json

--- tools/mapmerge2/frontend.py
+++ tools/mapmerge2/frontend.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 # Common code for the frontend interface of map tools
 import sys
 import os

--- tools/mapmerge2/dmm_test.py
+++ tools/mapmerge2/dmm_test.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 import os
 import sys
 from .dmm import *

--- tools/mapmerge2/mapmerge.py
+++ tools/mapmerge2/mapmerge.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python3
 import shutil
 from collections import defaultdict

--- tools/mapmerge2/fixup.py
+++ tools/mapmerge2/fixup.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python3
 import os
 import pygit2

--- tools/mapmerge2/merge_driver.py
+++ tools/mapmerge2/merge_driver.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python3
 import sys
 import collections

--- tools/mapmerge2/precommit.py
+++ tools/mapmerge2/precommit.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python3
 import os
 import sys

--- tools/mapmerge2/convert.py
+++ tools/mapmerge2/convert.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 #!/usr/bin/env python3
 from . import frontend, dmm

--- tools/mapmerge2/dmm.py
+++ tools/mapmerge2/dmm.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+'''
+
 # Tools for working with DreamMaker maps
 import io
 import bidict

--- tools/MapTileAggregator/__main__.py
+++ tools/MapTileAggregator/__main__.py
@@ -1,5 +1,12 @@
+'''
+License: See LICENSE.md
+Authors:
+    [Your Name] - Initial implementation
+    itsmeow of BeeStation - Original code
+'''
+
 #!/usr/bin/env python3
 import os
 import pathlib
