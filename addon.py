import os
import subprocess
import xbmc
import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

ok = xbmcgui.Dialog().ok(addonname, "Start Firefox?")
if ok:
    win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    width       = win.getWidth()
    height      = win.getHeight()
    xbmc.log("Starting Firefox", xbmc.LOGNOTICE)
    devnull = open(os.devnull, 'wb')
    subprocess.Popen(['/usr/bin/firefox', '-width', str(width), '-height', str(height)], stdout=devnull, stderr=devnull)
