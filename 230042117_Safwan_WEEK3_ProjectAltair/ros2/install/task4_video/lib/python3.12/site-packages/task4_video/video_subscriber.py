import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge 
import cv2 

class VideoSubscriber(Node):
    def __init__(self):
        super().__init__('video_subscriber')

        
        self.subscription = self.create_subscription(
            Image,
            'video_feed',
            self.listener_callback, 
            10)
        self.subscription 

        
        self.br = CvBridge()

    def listener_callback(self, data):
        
        current_frame = self.br.imgmsg_to_cv2(data, "bgr8")

        cv2.imshow("Video Feed", current_frame)

        cv2.waitKey(1) 

 
    def destroy_node(self):
        cv2.destroyAllWindows()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    video_subscriber = VideoSubscriber()
    rclpy.spin(video_subscriber)

    
    video_subscriber.destroy_node() 
    rclpy.shutdown()

if __name__ == '__main__':
    main()