import os
import sys
import yaml
import argparse
from isaacsim import SimulationApp


def get_script_directory():
    return os.path.dirname(os.path.abspath(__file__))


def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def load_extension():
    from isaacsim.core.utils.extensions import enable_extension

    # Enable Necessary extensions
    enable_extension("isaacsim.ros2.bridge")
    enable_extension("isaacsim.core.nodes")
    enable_extension("isaacsim.core.api")
    enable_extension("omni.kit.livestream.webrtc")
    # enable_extension("omni.syntheticdata")

    # Essential of else segmentation error
    kit.update()


def is_valid_usd(file_path):
    #from omni.isaac.nucleus import is_file
    from isaacsim.storage.native import is_file

    if is_file(file_path):
        return True
    else:
        return False
    

def load_usd(usd_path):
    import carb
    import omni
    from isaacsim.core.utils.prims import create_prim
    from isaacsim.core.utils.stage import is_stage_loading, add_reference_to_stage

    # Check if the environment usd file is valid
    if is_valid_usd(usd_path):
        pass
    else:
        carb.log_error("Environment usd file path not found.")

    omni.usd.get_context().open_stage(usd_path) 

    # Update the simulation to ensure the environment is loaded
    kit.update()
    kit.update()

    # Wait for the stage to finish loading
    while is_stage_loading():
        kit.update()

    carb.log_info("Loading environment complete ...")


def setup_kit_parameters():
    # Default Livestream settings
    kit.set_setting("/app/window/drawMouse", True)
    kit.set_setting("/app/livestream/proto", "ws")
    kit.set_setting("/ngx/enabled", False)
    
    # Enable DLSS 
    #kit.set_setting("/rtx-transient/dlssg/enabled", True)

    # Disable Reflections
    #kit.set_setting("/rtx/reflections/enabled", False)

    # Disable Translucency
    #kit.set_setting("/rtx/translucency/enabled", False)

    # Sample Per Pixel
    #kit.set_setting("/rtx/directLighting/sampledLighting/samplesPerPixel", 1)

    # Disable Indirect Diffusion
    #kit.set_setting("/rtx/indirectDiffuse/enabled", False)


def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--usd_path", type=str, help="Path to USD file.",
        required=True
    )

    args = parser.parse_args()

    script_path = get_script_directory()
    config_path = os.path.join(script_path,  "../config/isaac.yml")
    config = read_config(config_path)


    # Start the omniverse application
    global kit
    kit = SimulationApp(launch_config=config["isaac_sim"]["live_stream_config"])

    # Setup Kit parameters
    setup_kit_parameters()

    # Load extensions
    load_extension()

    # Load usd on stage
    load_usd(args.usd_path)

    for _ in range(10):
        kit.update()
    
    import omni.kit.viewport.utility
    
    # Run simulation
    while kit._app.is_running() and not kit.is_exiting():
        kit.update()
        print(omni.kit.viewport.utility.get_active_viewport().fps)

    # Close omniverse application
    kit.close()


if __name__ == "__main__":
    main()
