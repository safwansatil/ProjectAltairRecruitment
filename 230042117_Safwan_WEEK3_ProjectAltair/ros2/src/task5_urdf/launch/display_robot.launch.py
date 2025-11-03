import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    pkg_path = get_package_share_directory('task5_urdf')
    # What: Constructs the full path to your URDF file
    urdf_file = os.path.join(pkg_path, 'description', 'my_simple_robot.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

 
    rsp_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

   
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz_node',
        output='screen',
        arguments=['-d', os.path.join(pkg_path, 'rviz', 'urdf_config.rviz')]
       
    )


    return LaunchDescription([
        rsp_node,
        rviz_node
    ])