#!/usr/bin/python

"""
Reducer.py

"""

import sys

view_fc = {}
for row in sys.stdin:
    row = row.strip()
    fields = row.split("\t")
    country, video_id, view = fields
    view = int(view)

    if (country, video_id) not in view_fc:
        view_fc[(country, video_id)] = [view]
    else:
        view_fc[(country, video_id)].append(view)

for keys, values in view_fc.items():
    if len(values) > 1:
        delta = float((values[1] - values[0]))/values[0]
        country, video_id = keys
        if delta >= 10:
            increase = str(round(delta*100, 1))
            print("%s\t%s\t%s\t%%" % (country, video_id, increase))


