init:
    $ import time

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

label ch0_main:
    
    define prr = False
    if month >= "10" and day >= "15":
        define prr = True
        pass
    else:
        pass
    if prr is False:
        "Month is [month]"
        "Day is [day]"
        "The Alpha will go live on October 15. Quitting to desktop."
        $ renpy.quit()
    elif prr is True:
        "The Alpha is now live. Please update to the latest version from GitHub."
        "Quitting to desktop."
        $ renpy.quit()
    return