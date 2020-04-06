import os
import subprocess
import xbmc
import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

ok = xbmcgui.Dialog().ok(addonname, "Start Firefox?")
if ok:
    xbmc.log("Starting Firefox", xbmc.LOGNOTICE)
    devnull = open(os.devnull, 'wb')
    subprocess.Popen(['/usr/bin/firefox', '--kiosk'], stdout=devnull, stderr=devnull)
