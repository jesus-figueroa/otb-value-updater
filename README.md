# otb-value-updater
Simple value updater for olympian trading bot.

This python script will gather values from https://www.rolimons.com/ and update the values in OTB. It works by replacing the values of each items in OTB's values file. It will update the values when ever the script is ran.

## Compiling into executable with PyInstaller

I have precompiled an executable [here](https://github.com/jafigueroa-dev/otb-value-updater/blob/master/valueupdater.exe). To compile the python script into an executable to use in windows for yourself, you can use the following commands:

Install pyinstaller using pip
> pip install pyinstaller

Compile into an executable with pyinstaller
> pyinstaller --onefile valueupdater.py

## Windows Installation

To install in windows, first complete your OTB setup and ensure it's working properly and that the values file was generated.

Then download the **olympian.bat** provided here and either compile your own **valueupdater.exe** or download the precompiled [**valueupdater.exe**](https://github.com/jafigueroa-dev/otb-value-updater/blob/master/valueupdater.exe).

Then place both files into you **olympian.exe** directory, and replace the old **olympian.bat** with the new one provided.

Launch using the new **olympian.bat**, you can edit the restart interval in there as well by editing the **timeout** number value in seconds.

## Linux Installation

To install in linux, first complete your OTB setup and ensure it's working properly and that the values file was generated.

Then download the **valueupdater.py** and upload it into your **olympian.exe** directory.

Install **python3** using the following command:
> apt-get install python3

Lastly, edit your crontab so that both OTB and the script will run automatically using the following command:
> crontab -e

Chose nano as your editor.

Next add commands for both OTB and the valueupdater so that your crontab can automatically update values and restart OTB:
> 0 * * * * /usr/bin/python3 /root/bin3/valueupdater.py
> 0 * * * * systemctl restart olympian.service

> NOTE: You must add and empty line after your crontab commands or it won't work

It should look like this [image](https://i.gyazo.com/06512cf9cb38880a7a26543388e7de42.png)

Afterwards, hit CTRL + X and hit Y to save the your crontab.
