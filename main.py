import ctypes, time

def main():
    mutex = ctypes.windll.kernel32.CreateMutexW(None, True, "ROBLOX_singletonMutex")
    print("Don't close me")
    while True:
        time.sleep(1)

main()
