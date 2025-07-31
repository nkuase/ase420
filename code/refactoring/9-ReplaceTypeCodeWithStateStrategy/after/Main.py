from Logger import Logger

def main():
    logger = Logger()
    logger.log("information #1")
    
    logger.start()
    logger.log("information #2")
    
    logger.start()
    logger.log("information #3")
    
    logger.stop()
    logger.log("information #4")
    
    logger.stop()
    logger.log("information #5")

if __name__ == "__main__":
    main()
