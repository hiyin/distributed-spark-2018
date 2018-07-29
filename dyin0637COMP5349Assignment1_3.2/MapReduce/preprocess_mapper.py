
import sys

cat_id = {}
for row in sys.stdin:
    row = row.strip()
    fields = row.split("\t")
    video_id, country, cat = fields

    if (country, cat) not in cat_id:
        view_fc[(country, video_id)] = [view]
    else:
        view_fc[(country, video_id)].append(view)