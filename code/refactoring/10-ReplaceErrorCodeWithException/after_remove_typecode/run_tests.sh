#!/bin/bash

# Test runner script for Robot refactoring example (Exception Version)
# This script runs all unit tests for the AFTER refactoring state
# where error codes have been replaced with exceptions

echo "=== Running Unit Tests for Robot Project (Exception Version) ==="
echo ""

# Change to the directory containing this script
cd "$(dirname "$0")"

# Check if pytest is installed
if ! command -v pytest &> /dev/null; then
    echo "Error: pytest is not installed"
    echo "Please install pytest using: pip install pytest"
    exit 1
fi

# Run all tests in the test directory
echo "Running tests for exception-based implementation..."
pytest test/ -v

# Check the exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "=== All tests passed! Exception-based refactoring is working correctly! ==="
else
    echo ""
    echo "=== Some tests failed! Check the exception handling implementation. ==="
    exit 1
fi
