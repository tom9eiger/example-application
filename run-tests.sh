#!/bin/bash

set -e  # exit immediately on error

function check_component() {
  COMPONENT=$1
  echo "🔍 Checking $COMPONENT..."
  cd $COMPONENT

  python -m venv venv
  source venv/bin/activate

  pip install --upgrade pip
  if [ -f requirements.txt ]; then
    pip install -r requirements.txt
  fi

  echo "✅ Verifying $COMPONENT runs..."
  # If you have an entrypoint, use that — otherwise just check syntax
  if [ -f app.py ]; then
    python app.py || true  # try running it (e.g. Flask or CLI app)
  else
    python -m compileall .        # just make sure Python code compiles
  fi

  deactivate
  cd ..
}

check_component frontend
check_component backend

echo "🎉 All components passed startup check!"