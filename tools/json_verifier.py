--- tools/mapmerge2/dmm.py
+++ tools/mapmerge2/dmm.py
@@ -15,6 +15,7 @@
 TGM_HEADER = "//MAP CONVERTED BY dmm2tgm.py THIS HEADER COMMENT PREVENTS RECONVERSION, DO NOT REMOVE"
 ENCODING = 'utf-8'

+GACHA_RARITY = {'1 Star': 1, '2 Star': 2, '3 Star': 3, '4 Star': 4, '5 Star': 5}
 Coordinate = namedtuple('Coordinate', ['x', 'y', 'z'])

 class DMM:
     __slots__ = ['key_length', 'size', 'dictionary', 'grid', 'header']
