import unittest
from Logger import Logger
from StateStopped import StateStopped
from StateLogging import StateLogging

class TestLogger(unittest.TestCase):
    """Simple unittest for Logger class - complete scenario test"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.logger = Logger()
    
    def test_complete_scenario_from_main(self):
        """Test the complete scenario from main.py to verify state changes."""
        
        # Initial state should be STOPPED
        self.assertIsInstance(self.logger.get_state(), StateStopped)
        
        # Log when stopped - state should remain STOPPED
        self.logger.log("information #1")
        self.assertIsInstance(self.logger.get_state(), StateStopped)
        
        # Start logging - state should change to LOGGING
        self.logger.start()
        self.assertIsInstance(self.logger.get_state(), StateLogging)
        
        # Log when logging - state should remain LOGGING
        self.logger.log("information #2")
        self.assertIsInstance(self.logger.get_state(), StateLogging)
        
        # Start when already logging - state should remain LOGGING
        self.logger.start()
        self.assertIsInstance(self.logger.get_state(), StateLogging)
        
        # Log when logging - state should remain LOGGING
        self.logger.log("information #3")
        self.assertIsInstance(self.logger.get_state(), StateLogging)
        
        # Stop logging - state should change to STOPPED
        self.logger.stop()
        self.assertIsInstance(self.logger.get_state(), StateStopped)
        
        # Log when stopped - state should remain STOPPED
        self.logger.log("information #4")
        self.assertIsInstance(self.logger.get_state(), StateStopped)
        
        # Stop when already stopped - state should remain STOPPED
        self.logger.stop()
        self.assertIsInstance(self.logger.get_state(), StateStopped)
        
        # Log when stopped - state should remain STOPPED
        self.logger.log("information #5")
        self.assertIsInstance(self.logger.get_state(), StateStopped)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)