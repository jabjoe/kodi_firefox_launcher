import subprocess
import xbmc
import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

ok = xbmcgui.Dialog().ok(addonname, "Start Firefox?")
if ok:
    xbmc.log("Starting Firefox", xbmc.LOGNOTICE)
    subprocess.Popen(['/usr/bin/firefox'],
                         stdout=open("/tmp/firefox.stdout", 'wb'),
                         stderr=open("/tmp/firefox.stderr", 'wb'))
