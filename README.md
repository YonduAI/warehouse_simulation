# Warehouse Simulation

This repository provides Isaac Sim setup for simulating deformables in warehouse environment setup.

![](./preview/deformables.mp4)

---

## Table of Content
1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Usage](#usage)


---

### Prerequisites

- Inorder to run Isaac Sim inside container, you will require docker and Nvidia Container Toolkit. Complete the [Container Setup from Official Documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/install_container.html#container-setup).
- Since we will be running Isaac Sim in headless mode from inside the container, you will require WebRTC Streaming Client to visualize and modify Isaac Sim. [Download the AppImage and make it executable](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/download.html#latest-release).

  ```
  chmod +x <webrtc_streaming_client.AppImage>
  ```

---

### Setup

- Clone repository from GitHub:
  
  ```
  git clone git@github.com:YonduAI/warehouse_simulation.git
  ```

- Create docker image **yondu/isaac:latest** using startScript:

  ```
  chmod +x startScript
  ./startScript # Press 2
  ```

---

### Usage

- Run docker container **yondu_isaac** using startScript:

  ```
  ./startScript # Press 1
  ```

- Launch WebRTC Streaming Client:
  ```
  ./<webrtc_streaming_client.AppImage>
  ```
