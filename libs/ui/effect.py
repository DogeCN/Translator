from pywinstyles import apply_style
import sys

def acrylic(window):
    if sys.getwindowsversion().major >= 10:
        apply_style(window, 'acrylic')
