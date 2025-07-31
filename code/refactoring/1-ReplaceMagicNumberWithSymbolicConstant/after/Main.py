#from Robot import Robot
from Robot_enum import Robot

def main():
    robot = Robot("Andrew")
    robot.order(Robot.COMMAND_WALK)
    robot.order(Robot.COMMAND_STOP)
    robot.order(Robot.COMMAND_JUMP)

def main_enum():
    robot = Robot("Andrew")
    robot.order(Robot.Command.WALK)
    robot.order(Robot.Command.STOP)
    robot.order(Robot.Command.JUMP)

if __name__ == "__main__":
    #main()
    main_enum()
