import rclpy 
from rclpy.node import Node

class HappyNode3(Node):
    def __init__(self):
        print('ノードの作成')
        super().__init__('happy_node2')
        self.timer = self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info('ハッピーワールド3')

def main():
    print('プログラム開始')
    rclpy.init()
    node = HappyNode3()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print('強制終了')
        node.destroy_node()
        rclpy.try_shutdown()
    print('プログラム終了')