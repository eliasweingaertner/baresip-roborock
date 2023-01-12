# baresip-roborock

Start a roborock vacuum cleaner my making a SIP call

Rough guide how to get this running:

1. Install baresip
2. Configure baresip as follows:
  - Setup at least one SIP account
  - Enable the ctrl_tcp module
2. Install requirements: ```pip3 install -r requirements.txt```
3. Obtain the IP address and the token of your roborock device. See the [Python Miioo](https://github.com/rytilahti/python-miio) documentation how to do this.
4. Adjust settings in robodaemon.py
5. Start baresip
6. Start this script & have fun!
