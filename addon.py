import subprocess
import xbmc
import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

ok = xbmcgui.Dialog().ok(addonname, "Start Firefox?")
if ok == 'Ok':
    devnull = open(os.devnull, 'wb')
    p = subprocess.Popen(['/usr/bin/firefox'], stdout=devnull, stderr=devnull)
    while p.poll() is None:
        # Sleep for 0.1 seconds
        xbmc.sleep(100000)
