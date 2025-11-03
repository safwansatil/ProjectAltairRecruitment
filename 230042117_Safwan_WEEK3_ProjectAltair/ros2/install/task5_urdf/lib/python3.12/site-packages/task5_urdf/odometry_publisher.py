import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped 
from tf2_ros import StaticTransformBroadcaster 
import math

class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')

       
        self.tf_broadcaster = StaticTransformBroadcaster(self)

     
        self.start_time = self.get_clock().now()
        self.x = 0.0

       
        timer_period = 0.05
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Odometry Publisher Started. Robot moving...')

    def timer_callback(self):
       
        current_time = self.get_clock().now()
        elapsed_time = (current_time - self.start_time).nanoseconds / 1e9

        
        linear_speed = 0.5 # meters per second
        self.x = linear_speed * elapsed_time

        
        if self.x > 5.0:
             self.get_logger().warn('Motion limit reached (5m). Stopping the transform.')
             self.timer.cancel() # Stop the timer
             return

    
        t = TransformStamped()

        
        t.header.stamp = self.get_clock().now().to_msg()
       
        t.header.frame_id = 'odom' 
        
        t.child_frame_id = 'base_link' 

        
        t.transform.translation.x = self.x
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0 

       
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

   
        self.tf_broadcaster.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    odometry_publisher = OdometryPublisher()
    rclpy.spin(odometry_publisher)
    odometry_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()