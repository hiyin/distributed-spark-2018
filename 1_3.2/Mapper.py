#!/usr/bin/python

"""
Mapper.py

"""

import sys

video_id_views = {}
for row in sys.stdin:
    row = row.strip()
    fields = row.split("\t")
    video_id, trending_date, publish_time, view, country = fields

    if (video_id, country) not in video_id_views:
        # store viewNum in list of viewNum
        video_id_views[(video_id, country)] = [view]

    else:
        video_id_views[(video_id, country)].append(view)


for keys, values in video_id_views.items():
    # subset for 1st and 2nd view only to drop redundant data early
    video_id, country = keys
    values = sorted([int(v) for v in values])[:2]
    for value in values:
        print("%s\t%s\t%d" % (country, video_id, value))

