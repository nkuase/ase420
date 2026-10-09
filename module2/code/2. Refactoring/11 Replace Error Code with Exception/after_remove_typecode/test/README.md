# Unit Tests for Robot Project (Exception Version)

This directory contains updated unit tests for the Robot refactoring example that demonstrates the **AFTER** state - where error codes have been replaced with exceptions.

## What Changed from "Before" to "After"

### 🔄 **Key Refactoring Changes**

1. **Command.parse_command()**: 
   - **Before**: Returns `None` for invalid commands
   - **After**: Throws `InvalidCommandException` for invalid commands

2. **Robot.execute_command()**: 
   - **Before**: Returns `boolean` (True/False for success/failure)
   - **After**: Returns `void` - either succeeds or throws exception

3. **Robot._execute_command()**: 
   - **Before**: Returns `False` for unknown commands
   - **After**: Throws `InvalidCommandException` for unknown commands

4. **New Exception Class**: 
   - Added `InvalidCommandException` with a `message` attribute

### 📝 **Test File Updates**

#### **test_command.py**
- ✅ **CHANGED**: `test_parse_invalid_command()` now uses `assertRaises()` instead of `assertIsNone()`
- ✅ **ADDED**: `test_invalid_command_exception_details()` to verify exception messages
- ✅ **UNCHANGED**: Valid command parsing tests remain the same

#### **test_direction.py**
- ✅ **UNCHANGED**: Direction class was not affected by refactoring

#### **test_position.py**
- ✅ **UNCHANGED**: Position class was not affected by refactoring

#### **test_robot.py**
- ✅ **CHANGED**: `test_execute_command_*()` methods no longer check return values (no more `assertTrue(result)`)
- ✅ **CHANGED**: `test_execute_command_invalid()` now uses `assertRaises()` instead of `assertFalse()`
- ✅ **ADDED**: `test_multiple_invalid_commands_throw_exceptions()` to test various invalid inputs
- ✅ **UPDATED**: Sequence execution tests still verify error message printing behavior
- ✅ **IMPROVED**: Better exception message verification

### 🎯 **Learning Objectives**

These updated tests help students understand:

1. **Exception-Based Error Handling**: How to test code that throws exceptions instead of returning error codes
2. **assertRaises() Usage**: Proper use of unittest's exception testing capabilities
3. **Exception Message Testing**: Verifying that exceptions contain meaningful error information
4. **Behavioral Preservation**: How refactoring changes implementation but preserves external behavior
5. **Test Evolution**: How unit tests must evolve along with code refactoring

### 🔍 **Key Testing Patterns Demonstrated**

#### **Testing Exceptions**
```python
# NEW: Testing that exceptions are thrown
with self.assertRaises(InvalidCommandException) as context:
    Command.parse_command("invalid")
self.assertEqual(context.exception.message, "invalid")
```

#### **Testing Success Cases**
```python
# OLD: Checking return values
result = robot.execute_command("forward")
self.assertTrue(result)

# NEW: No return value to check - just verify no exception
robot.execute_command("forward")  # Success = no exception thrown
self.assertEqual(robot.position.y, 1)  # Verify side effects
```

### 📊 **Test Coverage**

- ✅ **39 individual test methods** covering all functionality
- ✅ **Exception throwing scenarios** for invalid inputs
- ✅ **Exception message verification** for proper error reporting
- ✅ **Normal operation scenarios** (unchanged behavior)
- ✅ **Integration testing** between refactored classes
- ✅ **Output verification** for error message printing (still works)

## Running the Tests

### Using the shell script:
```bash
./run_tests.sh
```

### Using pytest directly:
```bash
pytest test/ -v
```

### Prerequisites
```bash
pip install pytest
```

## Comparing "Before" vs "After"

Students can run both test suites to see:
1. **Same external behavior** - robot still moves and turns the same way
2. **Different error handling** - exceptions vs return codes
3. **Cleaner code structure** - no need to check return values for success cases
4. **Better error reporting** - exception messages provide more context

This demonstrates that **good refactoring preserves behavior while improving code quality**.
