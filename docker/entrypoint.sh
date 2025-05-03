#!/bin/bash

# Exit immediately if a command fails
set -e

# Using builtin ROS2 Humble
export isaac_sim_package_path=/isaac-sim
unset LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$isaac_sim_package_path/exts/isaacsim.ros2/bridge/humble/lib

# Log container start
echo "Starting Isaac Sim inside Docker ..."

# Run Isaac Sim  
python3 /home/workspaces/docker/tmux.py

# Keep the container running
exec /bin/bash
