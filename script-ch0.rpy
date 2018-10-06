init:
    $ import time

    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()

label ch0:
    
    define prr = False
    "Day: [day] Month: [month]"
    if day < 15:
        "The Alpha will be released on October 15th."
        "The game will now quit."
    elif day > 14:
        "The Alpha is now available. Please update the mod from GitHub."
        "The game will now quit."
    $ renpy.quit()
    return