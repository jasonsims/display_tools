Display Tools
========
This is a utility module for common console output tasks such as colored output and wait animations. I have found myself reusing these function quite often so I figured it would be useful to have them all in one place. 

Text formatting and output
--------------------------
Usage: ```from display_tools import TextOutput as out```

### Colored alert messages
    >>> out.info('Yo, here is an info message')
    [ INFO ] Yo, here is an info message
    
    >>> out.warn('Aww snap, you have been warned')
    [ WARN ] Aww snap, you have been warned
    
    >>> out.error('Your shit is broke')
    [ ERROR ] Your shit is broke

### Output list or dictionary
    >>> out.dict({'name': 'Jason Sims', 'email': 'sims.jrobert@gmail.com', 'twitter': '@_jasonsims'})
    twitter     : @_jasonsims
    name        : Jason Sims
    email       : sims.jrobert@gmail.com

    >>> out.list(['Beets', 'Bears', 'Battlestar Galactica' ])
    Beets
    Bears
    Battlestar Galactica

Progress display
----------------

Usage: ```from display_tools import ConsoleAnimations```

### Pinwheel animation
    >>> wait = ConsoleAnimations()
    >>> while not something_needs_to_complete:
    ...   wait.pin_wheel()
    
### Infinate progress bar
    >>> wait = ConsoleAnimations()
    >>> while not something_needs_to_complete:
    ...   wait.moving_bar()

Comming Soon
------------
* [ ] Progress bar
* [ ] Animations that run in their own thread
* [ ] Ability to output text with color_name as a parameter
* [ ] Paramaters for dict output (ex. Sort, Key colors)
* [ ] Status messages will incorporate a logger object
