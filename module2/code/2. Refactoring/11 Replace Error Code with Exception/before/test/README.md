# Unit Tests for Robot Project

This directory contains comprehensive unit tests for the Robot refactoring example that demonstrates replacing error codes with exceptions.

## Test Files

- **test_command.py**: Tests the Command class functionality including:
  - Command creation and naming
  - Predefined command constants (FORWARD, BACKWARD, TURN_LEFT, TURN_RIGHT)
  - Command parsing from strings
  - Error handling for invalid commands

- **test_direction.py**: Tests the Direction class functionality including:
  - Direction creation with x, y components
  - Setting new direction values
  - Handling negative and zero values

- **test_position.py**: Tests the Position class functionality including:
  - Position creation with x, y coordinates
  - Relative movement calculations
  - Multiple movement operations
  - Handling negative coordinates and zero movement

- **test_robot.py**: Tests the Robot class functionality including:
  - Robot creation and initialization
  - Individual command execution (forward, backward, left, right)
  - Robot turning and movement behavior
  - Command sequence execution
  - Error handling for invalid commands
  - Output verification for error messages

## Running the Tests

### Option 1: Using the shell script (recommended)
```bash
./run_tests.sh
```

Note: You may need to make the script executable first:
```bash
chmod +x run_tests.sh
```

### Option 2: Using pytest directly
```bash
pytest test/ -v
```

### Option 3: Running individual test files
```bash
python -m pytest test/test_command.py -v
python -m pytest test/test_direction.py -v
python -m pytest test/test_position.py -v
python -m pytest test/test_robot.py -v
```

## Prerequisites

Make sure you have pytest installed:
```bash
pip install pytest
```

## Test Coverage

The tests cover:
- ✅ Normal operation scenarios
- ✅ Edge cases (zero values, negative values)
- ✅ Error conditions and invalid inputs
- ✅ Integration between classes
- ✅ Output verification for error messages

## Learning Objectives

These tests help students understand:
1. How to write clear, simple unit tests
2. Testing different scenarios (positive, negative, edge cases)
3. Verifying expected behavior vs. error conditions
4. The importance of testing before refactoring
5. How the current error code system works (before refactoring to exceptions)
