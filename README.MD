# baresip-roborock - Start your MI vacuum on receiving a phone call

This script allows a Xiaomi Roborock vacuum cleaner to be started if a call arrives a SIP account. This is particularly useful if you have a home router (e.g. an AVM Fritz!Box) and you want to trigger the Roborock from such a ecosystem. SIP is a very widely adopted protocol, and using SIP for signalling avoids an implementation for a particular router or smart home API.

## Example use scenario

We've used this script to start the Roborock cleaner if a button is pressed on an AVM Fritz!Dect 440 button:

```
┌──────┐      ┌────────────────┐       ┌───────────────────────────┐                ──────── │
│      │      │                │       │  Raspbery Pi Zero         │             ┌──         └┐
│Button│      │ Router         ├───────┤►┌───────┐   ┌───────────┐ │            ┌┘  Vacuum    └┐
│      ├─────►│ (e.g. Fritzbox)│       │ │baresip◄───┤THIS SCRIPT├─┼──────────►┌┤   Roborock   │
└──────┘      └────────────────┘       └─┴───────────┴───────────┴─┘           └┤            ┌─┘
                                                                                └────────────┘
```

The figure above illustrates roughly how this is working:

- The button is integrated with the Router.
- The router is configured to make a call to an internal SIP account if the button is pressed. For AVM Fritz!Boxes, this can be achieved by setting setting up a template. The template can be empty but only ring a number. The number needs to belong to a SIP account which baresip is configured against.
- baresip (with ctrl_tcp enabled) runs on an arbitrary external host. We use a Pi Zero here and deploy the Script using Docker for the sake of convenience. The script is integrated using baresip's TCP control port, which emits [netstrings](http://cr.yp.to/proto/netswtrings.txt) upon SIP events.
- The script parses the events and pushes a start command to the Vacuum (using [Python Miio](https://github.com/rytilahti/python-miio)


## Anticipated question

> Why use a full-blown SIP client? Why do we not directly register at the SIP server from Python?

Good one! While hacking this together we discovered that there is very little maintained Python SIP libraries. Unfortunately [PyVoip](https://github.com/tayler6000/pyVoIP) did not work with our Fritz!Box at the time of writing this.

## Installation

Rough guide how to get this running:

1. Install baresip
2. Configure baresip as follows:
  - Setup at least one SIP account
  - Enable the ctrl_tcp module
2. Install requirements: ```pip3 install -r requirements.txt```
3. Obtain the IP address and the token of your roborock device. See the [Python Miio](https://github.com/rytilahti/python-miio) documentation how to do this.
4. Adjust settings in robodaemon.py
5. Start baresip
6. Start this script & have fun!
