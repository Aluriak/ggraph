
# std import
import sys

print('This is a print statement in the __main__.py file. '
      'This can\'t be printed more than once.')
# package import
from ggraph.application import app

if __name__ == '__main__':
    # Ok it's hugly but it's run, some day we use a real configuration system
    if len(sys.argv) < 3:
        app.debug = True
    else:
        app.debug = sys.argv[2].startswith("T")

    app.run(port=int(sys.argv[1]))
