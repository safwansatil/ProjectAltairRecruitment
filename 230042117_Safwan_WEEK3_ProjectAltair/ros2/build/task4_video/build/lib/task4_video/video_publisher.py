import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')

        
        self.publisher_ = self.create_publisher(Image, 'video_feed', 10)

        
        timer_period = 1.0 / 30.0  # seconds (33.3 ms per frame)
        self.timer = self.create_timer(timer_period, self.timer_callback)

        
        self.br = CvBridge()

        
        self.cap = cv2.VideoCapture(0) 

        
        if not self.cap.isOpened():
            self.get_logger().error("Error: Could not open video stream or file.")
            
    def timer_callback(self):
        
        ret, frame = self.cap.read()

        if ret:
            
            ros_image_msg = self.br.cv2_to_imgmsg(frame, encoding="bgr8")

            
            self.publisher_.publish(ros_image_msg)

        
def main(args=None):
    rclpy.init(args=args)
    video_publisher = VideoPublisher()
    rclpy.spin(video_publisher)

    
    video_publisher.cap.release()
    video_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()