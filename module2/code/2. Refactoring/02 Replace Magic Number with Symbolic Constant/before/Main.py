from Robot import Robot

def main():
    robot = Robot("Andrew")
    robot.order(0)  # walk - magic number!
    robot.order(1)  # stop - magic number!
    robot.order(2)  # jump - magic number!

if __name__ == "__main__":
    main()
