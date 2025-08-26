from Robot import Robot

def main():
    robot = Robot("Andrew")
    print(robot)
    
    robot.execute("forward right forward")
    print(robot)
    
    robot.execute("left backward left forward")
    print(robot)
    
    robot.execute("right forward forward farvard")  # 'farvard' is invalid
    print(robot)

if __name__ == "__main__":
    main()
