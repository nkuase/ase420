#!/bin/bash

# Test runner script for Robot refactoring example
# This script runs all unit tests using pytest

echo "=== Running Unit Tests for Robot Project ==="
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
echo "Running tests..."
pytest test/ -v

# Check the exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "=== All tests passed! ==="
else
    echo ""
    echo "=== Some tests failed! ==="
    exit 1
fi
