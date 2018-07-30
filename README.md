## Teenager Attention Grabbing Towerlight

Inspired by [http://www.jameswest.site/the-tea-time-klaxon](http://www.jameswest.site/the-tea-time-klaxon)

As featured in MagPi #73. Full details of how to build the project can be found at [https://raspberrypi.org/magpi](https://raspberrypi.org/magpi) (free PDF download).

### Improved Software Available

If you are after the basic software listed in MagPi and are looking to play around with your own code, this is place to be. If you want some more features, a snazzy user interface, sound and DISCO MODE, head over to [https://github.com/mrpjevans/klaxon](https://github.com/mrpjevans/klaxon) for an alternative version.


### Installation

Make sure you know the hostname or IP address of the Pi connected to the tower light.

Once the tower light is wired up as per MagPi #73...

```bash
cd
sudo apt update && sudo apt upgrade

# Install the Automation pHAT libraries
curl https://get.pimoroni.com/automationhat | bash

# Install the Flash web app framework globally
sudo -H pip install flask

# Clone this package to the directory '~/pi/towerlight'
git clone https://github.com/mrpjevans/towerlight.git
```

### Test

```bash
python ~/towerlight/towerlight
```

If all is well after a second or two the lights on the tower will cycle. You should now be able to go to http://_address-of-tower-light_:5000/ and see a simple web page.

`Ctrl+C` will shut things down.

### Run As a Service

We can set the web server to startup at boot:

```bash
sudo nano /lib/systemd/system/towerlight.service
```

In nano, add the following:

```
[Unit]
Description=Towerlight           
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python /home/pi/towerlight/towerlight.py

[Install]
WantedBy=multi-user.target
```
Then `Ctrl+X` followed by `y` to save and exit.

To enabled everything:

```bash
sudo chmod 644 /lib/systemd/system/towerlight.service 
sudo systemctl daemon-reload
sudo systemctl enable towerlight.service
sudo systemctl start towerlight.service
```

The lights should cycle as before. Now the server will start whenever the Pi is booted.

### Usage

Just point a web browser to http://_ip-or-hostname-of-your-pi_:5000/ to see a simple web page that allows you to control the lights. It's a very simple interface, one that is intended to be built on.

### Thanks
To James West for the original project: [http://www.jameswest.site/the-tea-time-klaxon](http://www.jameswest.site/the-tea-time-klaxon) and to MagPi for featuring it in their magnificent publication (I may be a bit biased).