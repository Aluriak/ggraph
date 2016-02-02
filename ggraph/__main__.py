
# std import
import sys

# package import
from .application import app

if __name__ == '__main__':
    # Ok it's hugly but it's run, some day we use a real configuration system
    if len(sys.argv) < 3:
        app.debug = True
    else:
        app.debug = sys.argv[2].startswith("T")

    app.run(port=int(sys.argv[1]))
