import os
import signal
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

firefox_pid = "/tmp/firefox.pid"
firefox_path = which("firefox")

ok = xbmcgui.Dialog().ok(addonname, "Start Firefox?")
if ok:
    # Collect any zombies children.
    if os.path.exists(firefox_pid):
        with open(firefox_pid, "r") as f:
            pid = int(f.readline())
        proc_filename = "/proc/%u/stat" % pid
        if os.path.exists(proc_filename):
            with open(proc_filename) as f:
                stat = f.readline().split()
                name = stat[1]
                state = stat[2]
                if name == "(firefox)" and state == "Z":
                    os.waitpid(pid, 0)
        os.unlink(firefox_pid)

    win = xbmcgui.Window(xbmcgui.getCurrentWindowId())
    width       = win.getWidth()
    height      = win.getHeight()
    xbmc.log("Starting Firefox", xbmc.LOGNOTICE)
    devnull = open(os.devnull, 'wb')
    p = subprocess.Popen([firefox_path, '-width', str(width), '-height', str(height)], stdout=devnull, stderr=devnull)
    if p:
        with open(firefox_pid, "w") as f:
            f.write("%u" % p.pid)
    else:
        xbmc.log("Failed to start Firefox", xbmc.LOGERROR)
