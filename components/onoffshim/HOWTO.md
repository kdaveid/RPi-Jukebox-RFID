## On Off Shim

Source: https://github.com/pimoroni/clean-shutdown

Macht einen Service (cleanshutd)
der überwacht die Pins

`systemctl status cleanshutd`

## Settings
/etc/cleanshutd.conf


## Problems with shutdowns
`sudo systemctl disable cleanshutd`

As alternative to the above, you may add the following to your /boot/config.txt file from another computer:
`disable_cleanshutd=1`


sudo service mpd restart
sudo mpc update