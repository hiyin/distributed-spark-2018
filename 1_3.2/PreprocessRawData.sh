#!/usr/bin/env bash

infilepath=$1
outfilepath=$2
# Condense file to include 5 useful columns below:
# video_id, trending_date, publish_time, view, country

# skip header and ignore delimiter found in doubled quote to prevent awk to print mistakes
# sort by date (because we want to have first and second view by time)

# e.g.
# $ tail -n +2 ALLvideos.csv | head -300 | awk -vFPAT='([^,]*)|("[^"]+")' -vOFS=, '{print $1"\t"$2"\t"$7"\t"$9"\t"$NF}' | sort -k2 | grep ZJ9We4bjcg0
# ZJ9We4bjcg0	17.14.11	2017-11-12T13:10:36.000Z	822213	DE
# ZJ9We4bjcg0	17.15.11	2017-11-12T13:10:36.000Z	958741	DE

tail -n +2 $infilepath | awk -vFPAT='([^,]*)|("[^"]+")' -vOFS=, '{print $1"\t"$2"\t"$7"\t"$9"\t"$NF}' | sort -k2 > $outfilepath

