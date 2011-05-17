#!/bin/bash
# checks for cfg files and runs cccp
# set as cron job to run every x mins
# */x * * * * 

cccp='path/to/cccp/script'
csv='path/to/cfg/dir/'

cfg=`ls -1 $csv | grep '.cfg'`

for f in $cfg
do
	nice python $cccp "$csv$f"
done
