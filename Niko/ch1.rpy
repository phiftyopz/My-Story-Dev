label ch0:
    $ import time
    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
    define prr = False
    if month >= "10" and day >= "15":
        $ prr = True
        pass
    else:
        pass
    if prr = False:
        renpy.prompt("The Alpha will go live on October 15. Returning to main menu.");
    elif prr = True:
        renpy.prompt("The Alpha is now live. Please update to the latest version from GitHub.");
        renpy.prompt("Returning to main menu.");
    return    