from control.hexapod_controller import Hexapod

def main():
    # Initialize hexapod
    h = Hexapod(TRIPOD)

    # Move forward
    h.walk(steps=20)

