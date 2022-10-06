# Power-Manager-QT
Power manager program written with Python and Qt5 

![power](https://user-images.githubusercontent.com/29865797/194307561-1f9451fe-5597-4276-b1d3-5e4248092b38.png)______________________


#Power manager-QT v.8 Copyright (c) 2017 JJ Posti <techtimejourney.net>
#This is a power manager application.The program comes with ABSOLUTELY NO WARRANTY;  #for details see: http://www.gnu.org/copyleft/gpl.html. #This is free software, and you are welcome to redistribute it under
#GPL Version 2, June 1991 This is the QT5 version” )

V.8 is a bug-fix release.

Power-Manager QT is upgraded to support systemctl commannds. Also, has Are you sure dialogs on every entry now. Logout is for Openbox.

Notable change in v.6: Power Manager has a new outlook done with CSS.

Dependencies:

The list below should be enough:

python3 python-pyqt5 python-minimal

Additional dependencies for Power-Manager:This tool has Openbox integrations in it. Logout assumes Openbox installed. Screen locking uses i3lock program.

Note. Power Manager assumes you are using sudo and have gksudo installed. If you have an actual root account then make sure that you have gksu installed. Additionally, you must change Power Manager´s code to read gksu in all entries that have gksudo in them. The previous task should be fairly easy to undertake.

Run the program via terminal like this: python something.py

If needed make the program executable with: chmod +x something.py
____________________________
Original post is at:
http://www.techtimejourney.net/power-manager-v-6python/
