Python Script using Expect to help backup TPLINK Based Managed Switches that aren't supported under Rancid.

I discoverd that Rancid doesn't work with these switches so had to design something to help and pull switch configs via TFTP this can be cron nightly or hourly - the script appends date+time stamp so you can use that to keep track of changes.


Reqs to make this work.

A Linux or BSD Based System

* Will work with OSX provided your using Brew with Python 2.7.10+
* Python 2.7.10+
* TFTP Server 
* Python Pexpect
* Expect 5.45+


Enjoy
