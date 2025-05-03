# ====================================================================
# Stage 1: Base Image Setup (Isaac Sim 4.5.0)
# ====================================================================
ARG ISAAC_SIM_TAG=4.5.0
FROM nvcr.io/nvidia/isaac-sim:$ISAAC_SIM_TAG

ENV DEBIAN_FRONTEND=noninteractive

# Install essential system dependencies
RUN apt-get update && apt-get install -y \
	curl \
	wget \
	gnupg2 \
	lsb-release \
	software-properties-common \
	locales \
    git \
	tmux \
	vim \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set up locales
ENV LANG=en_US.UTF-8
RUN locale-gen en_US en_US.UTF-8 && \
	update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8


# ====================================================================
# Stage 2: Isaac Sim Variables
# ====================================================================

# Setup Isaac Sim environment variables
ENV ISAAC_SIM_PATH=/isaac-sim
ENV CARB_APP_PATH=${ISAAC_SIM_PATH}/kit
ENV ISAAC_PATH=${ISAAC_SIM_PATH}
ENV EXP_PATH=${ISAAC_PATH}/apps
ENV OMNI_KIT_ALLOW_ROOT=1

# Source Isaac Sim 4.5 environment in .bashrc
RUN echo "source ${ISAAC_SIM_PATH}/setup_python_env.sh" >> /root/.bashrc

# Add alias for running isaacsim python
RUN echo "alias isaac=/isaac-sim/python.sh" >> /root/.bashrc


# ===================================================================
# Stage 3: Use Internal ROS2 Humble Library
# ===================================================================
RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ISAAC_SIM_PATH/exts/isaacsim.ros2.bridge/humble/lib" >> /root/.bashrc


# ====================================================================
# Stage 4: Install Python Packages from requirements.txt 
# ====================================================================
# Copy the requirements.txt file to the container
COPY ./requirements.txt /tmp/requirements.txt   

# Install Python packages
RUN pip3 install --upgrade pip && \
	pip3 install -r /tmp/requirements.txt

# Set default work directory
WORKDIR /home/workspaces

# Default command
CMD ["/bin/bash"]
