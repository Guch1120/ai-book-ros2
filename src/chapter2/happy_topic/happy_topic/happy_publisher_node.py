import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HappyPublisher(Node):  
    def __init__(self):
        super().__init__('happy_publisher_node') 
        self.pub = self.create_publisher(String, 'topic', 10)
        self.i = 10 
        self.timer = self.create_timer(1.0, self.timer_callback) 

    def timer_callback(self):
        msg = String()
        if self.i > 0:
            msg.data = f'カウンドダウン {self.i}'
        elif self.i == 0:
            msg.data = '発射'
        else:
            msg.data = f'経過時間 {-self.i}'
        self.pub.publish(msg)
        self.get_logger().info(f'パブリッシュ: {msg.data}') 
        self.i -= 1

def main(args=None):
    rclpy.init() 
    
    node = HappyPublisher() 
    
    try:
        rclpy.spin(node) 
    except KeyboardInterrupt:
        print('ctrl+cが押されたよ') 
    finally:
        node.destroy_node()
        rclpy.try_shutdown() 
