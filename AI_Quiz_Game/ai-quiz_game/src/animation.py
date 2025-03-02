import time

def show_loading_animation():
    animation = ["|", "/", "-", "\\"]
    for i in range(10):
        print("\rLoading Quiz " + animation[i % len(animation)], end="")
        time.sleep(0.2)
    print("\n")
