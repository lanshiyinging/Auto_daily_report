#!/bin/bash

usrname="yourusername"
password="yourpassword"
email="youremail"

python auto_daily_report.py $usrname $password
result=$?
i=0
until  [ $result -eq 0 -o $i -gt 5 ];
do

    sleep 1h

    python auto_daily_report.py $usrname $password
    result=$?

    echo ${i}

    i=`expr $i + 1`

done

#mail -s "Daily report success" youremail

if [ $result -eq 0 ]; then
    mail -s "Daily report success" email
else
    mail -s "Daily report failed" email
fi
