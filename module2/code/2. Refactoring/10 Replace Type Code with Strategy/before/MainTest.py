import unittest
from Logger import Logger

class TestLogger(unittest.TestCase):
    """Simple unittest for Logger class - complete scenario test"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.logger = Logger()
    
    def test_complete_scenario_from_main(self):
        """Test the complete scenario from main.py to verify state changes."""
        
        # Initial state should be STOPPED
        self.assertEqual(self.logger.state, Logger.STATE_STOPPED)
        
        # Log when stopped - state should remain STOPPED
        self.logger.log("information #1")
        self.assertEqual(self.logger.state, Logger.STATE_STOPPED)
        
        # Start logging - state should change to LOGGING
        self.logger.start()
        self.assertEqual(self.logger.state, Logger.STATE_LOGGING)
        
        # Log when logging - state should remain LOGGING
        self.logger.log("information #2")
        self.assertEqual(self.logger.state, Logger.STATE_LOGGING)
        
        # Start when already logging - state should remain LOGGING
        self.logger.start()
        self.assertEqual(self.logger.state, Logger.STATE_LOGGING)
        
        # Log when logging - state should remain LOGGING
        self.logger.log("information #3")
        self.assertEqual(self.logger.state, Logger.STATE_LOGGING)
        
        # Stop logging - state should change to STOPPED
        self.logger.stop()
        self.assertEqual(self.logger.state, Logger.STATE_STOPPED)
        
        # Log when stopped - state should remain STOPPED
        self.logger.log("information #4")
        self.assertEqual(self.logger.state, Logger.STATE_STOPPED)
        
        # Stop when already stopped - state should remain STOPPED
        self.logger.stop()
        self.assertEqual(self.logger.state, Logger.STATE_STOPPED)
        
        # Log when stopped - state should remain STOPPED
        self.logger.log("information #5")
        self.assertEqual(self.logger.state, Logger.STATE_STOPPED)


if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)