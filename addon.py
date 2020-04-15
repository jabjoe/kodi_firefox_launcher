import os
import psutil
import subprocess
import xbmc
import xbmcaddon
import xbmcgui

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


def which(filename):
    pathenv=os.getenv('PATH')
    for p in pathenv.split(os.path.pathsep):
        p = os.path.join(p, filename)
        if os.path.exists(p) and os.access(p,os.X_OK):
            return p

firefox_path = which("firefox")

ok = xbmcgui.Dialog().ok(addonname, "Start Firefox?")
if ok:
    # Collect any zombies children.
    for p in psutil.Process().children():
        if p.exe() == firefox_path:
            p.terminate()
            p.wait()

    win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    width       = win.getWidth()
    height      = win.getHeight()
    xbmc.log("Starting Firefox", xbmc.LOGNOTICE)
    devnull = open(os.devnull, 'wb')
    subprocess.Popen([firefox_path, '-width', str(width), '-height', str(height)], stdout=devnull, stderr=devnull)
