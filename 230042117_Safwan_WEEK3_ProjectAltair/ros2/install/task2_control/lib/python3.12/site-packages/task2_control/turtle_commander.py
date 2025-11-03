import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
import time
import threading

class TurtleCommander(Node):

    def __init__(self):
        super().__init__('turtle_commander')

        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

        
        threading.Thread(target=self.get_user_input, daemon=True).start()

    def publish_cmd(self, linear_x, angular_z):
        
        msg = Twist()
        
        msg.linear.x = linear_x
        # Angular velocity (turning/rotation) is around the Z-axis
        msg.angular.z = angular_z
        self.publisher_.publish(msg)

    def move_turtle(self, command):
        self.get_logger().info(f'Executing command: {command}')

        

        
        if command == 'A' or command == 'a':
            
            self.publish_cmd(2.0, 1.0)
            self.get_logger().info("Moving in a Circle...")

        
        elif command == 'B' or command == 'b':
            self.get_logger().info("Moving in a Square (This will take a few seconds)...")
            side_speed = 1.5
            side_duration = 2.0 
            turn_speed = 1.57 
            turn_duration = 1.0 

            
            self.publish_cmd(0.0, 0.0) 
            time.sleep(0.5)

            for _ in range(4): # 4 sides of a square
                
                self.publish_cmd(side_speed, 0.0)
                time.sleep(side_duration)
                
                self.publish_cmd(0.0, 0.0)
                time.sleep(0.1)
                
                self.publish_cmd(0.0, turn_speed)
                time.sleep(turn_duration) 
                
                self.publish_cmd(0.0, 0.0)
                time.sleep(0.1)

        elif command == 'C' or command == 'c':
            self.get_logger().info("Moving in an Outward Spiral (press Enter to stop)...")
            # Stop existing motion
            self.publish_cmd(0.0, 0.0)
            time.sleep(0.5)

            angular_speed = 1.0 
            linear_speed = 0.5 
            rate = self.create_rate(20) 

            
            for i in range(200):
                linear_speed += 0.01 
                self.publish_cmd(linear_speed, angular_speed)

                
                if rclpy.ok(): 
                    rate.sleep()
                else:
                    break

            
            self.publish_cmd(0.0, 0.0)

        
        elif command == 'S' or command == 's':
            self.publish_cmd(0.0, 0.0)
            self.get_logger().info("Stopped.")

        else:
            self.get_logger().warn("Invalid command. Use A, B, C, or S.")
            self.publish_cmd(0.0, 0.0)


    def get_user_input(self):
        
        while rclpy.ok():
            try:
                command = input("Enter A (Circle), B (Square), C (Spiral), or S (Stop): ").strip().upper()
                self.move_turtle(command)
            except EOFError:
                break
            except Exception as e:
                self.get_logger().error(f"Error getting input: {e}")
                break
            time.sleep(0.1)


def main(args=None):
    rclpy.init(args=args)
    turtle_commander = TurtleCommander()

    
    rclpy.spin(turtle_commander) 

    
    turtle_commander.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()