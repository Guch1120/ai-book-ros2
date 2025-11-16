import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FuckyouSubscriber(Node):
    def __init__(self):
        super().__init__('fuckyou_subscriber_node')
        self.sub = self.create_subscription(String ,
                                            'topic' , self.callback , 10)
    def callback(self,msg):
        self.get_logger().info(f'サブスクライブ{msg.data}')

def main(args=None):
    rclpy.init()
    node = FuckyouSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('中断')
    finally:
        node.destroy_node()
        rclpy.try_shutdown()