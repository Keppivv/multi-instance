import ctypes, time

def main():
    mutex = ctypes.windll.kernel32.CreateMutexW(None, True, "ROBLOX_singletonMutex")
    print("Keep this running while playing.")
    while True:
        time.sleep(10)

main()
