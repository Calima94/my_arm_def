# ROS2 arm project using Myo armband

This module is a simulator of upper-arm using ROS2 and Gazebo using capture of EMG(Eletromyography) signals.

## How to Use:

* Install ROS2-Foxy in Linux distributions (tested in Ubuntu 20.04)
* Install Gazebo-11
* Install ROS2-Gazebo libraries (https://classic.gazebosim.org/tutorials?tut=ros2_installing&cat=connect_ros)
* Install all other libraries in requirements.txt (Python3 packages) and requirements.yml (Conda Packages)
* Add in the ~/.bashrc the followings commands:

    source /opt/ros/foxy/setup.bash
    source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
    source ~/my_arm_def/install/setup.bash
    export GAZEBO_RESOURCE_PATH=/usr/share/gazebo-11:/usr/share/gazebo_models:${GAZEBO_RESOURCE_PATH}
    export GAZEBO_PLUGIN_PATH=${GAZEBO_PLUGIN_PATH}:~/my_arm_def/install/my_arm_def_cpp_pkg/lib
    export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:~/my_arm_def/src/my_arm_def_cpp_pkg/models

if you are using a Conda environment add the following lines in the ~\.bashrc file:

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/home/"user"/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
       eval "$__conda_setup"
    else
        if [ -f "/home/"user"/anaconda3/etc/profile.d/conda.sh" ]; then
            . "/home/"user"/anaconda3/etc/profile.d/conda.sh"
        else
            export PATH="/home/caio/anaconda3/bin:$PATH"
        fi
    fi
    #unset __conda_setup
    # <<< conda initialize <<<

* remember to change "user" with your user name

* Install the my_arm_def folder in the home directory, otherwise adjust the ~/.bashrc file
* Compile the my_arm_def_cpp_pkg in the my_arm_def folder with the following command (colcon build --packages-select my_arm_def_cpp_pkg)
* Source your enviroment with the comand (source ~/.bashrc)
* Compile the following projects in the following order:
    my_arm_def_interfaces (colcon build --packages-select my_arm_def_interfaces)
    my_arm_def_py_pkg (colcon build --packages-select my_arm_def_py_pkg --symlink-install)
    my_arm_definitive_bringup (colcon build --packages-select my_arm_definitive_bringup --symlink-install)
* Source again your enviroment with the comand (source ~/.bashrc)
* run the file main.

## Aditional observation

There are some .joblib classifiers with my EMG data, please if needed, consider Capture EMG data with the following module (Capture_EMG_Data: https://github.com/Calima94/Capture_EMG_Data.git) and training the classifier with the module (Train_Myo_Signals: https://github.com/Calima94/Train_Myo_Signals.git).

All modules are in alpha phase, please if you like, you're welcome to contribute and improve this project:

My contact is: clima@ufabc.edu.br

Best Regards
    
