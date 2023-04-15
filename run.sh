#!/bin/bash

# Start the backend (Uvicorn)
cd ./backend
uvicorn main:app --reload &

# Save the backend process ID
backend_pid=$!

# Start the frontend (npm)
cd ../frontend
npm run dev &

# Save the frontend process ID
frontend_pid=$!

# Wait for both processes to finish
wait $backend_pid $frontend_pid

# Exit the script
exit 0