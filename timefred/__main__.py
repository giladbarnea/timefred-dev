import os
if os.getenv('TIMEFRED_DEV'):
    print('Patching sys.excepthook')
    import sys
    from IPython.core import ultratb
    sys.excepthook=ultratb.VerboseTB()

from timefred.timefred import main

if __name__ == '__main__':
    main()
