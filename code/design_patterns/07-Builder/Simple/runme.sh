PYTHON_PATH=$(command -v python)

if [ -z "$PYTHON_PATH" ]; then
  PYTHON_PATH=$(command -v python3)
fi

if [ -n "$PYTHON_PATH" ]; then
    $PYTHON_PATH main.py text
    $PYTHON_PATH main.py html
else
  echo "No python or python3"
fi

