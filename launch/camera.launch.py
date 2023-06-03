from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    v4l2_node = Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen'
            )

    image_transport = Node(
            package='image_transport',
            executable='republish',
            arguments=["raw"],
            remappings=[('in', '/image_raw'),
                ('out', '/image_raw/compressed')
                ],
            output='screen'
            )

    return LaunchDescription([
        v4l2_node,
        image_transport
        ])
