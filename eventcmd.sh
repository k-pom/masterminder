#!/bin/bash

# create variables
while read L; do
	k="`echo "$L" | cut -d '=' -f 1`"
	v="`echo "$L" | cut -d '=' -f 2`"
	export "$k=$v"
done < <(grep -e '^\(title\|artist\|album\|stationName\|songStationName\|pRet\|pRetStr\|wRet\|wRetStr\|songDuration\|songPlayed\|rating\|coverArt\|stationCount\|station[0-9]*\|audioUrl\)=' /dev/stdin) # don't overwrite $1...

echo "{\"event\": \"pandora.$1\",
        \"data\": {
           \"title\": \"$title\",
           \"artist\": \"$artist\",
	   \"station\": \"$stationName\",
	   \"stationCount\": \"$stationCount\"
        }
}" > /home/pi/masterminder/input.fifo
