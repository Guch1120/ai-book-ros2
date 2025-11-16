import rclpy 
from rclpy.node import Node

class HappyNode2(Node):
    def __init__(self):
        print('ノードの作成')
        super().__init__('happy_node2')
        self.timer = self.create_timer(1.9, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info('ハッピーワールド2')

def main():
    print('プログラム開始')
    rclpy.init()
    node = HappyNode2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    print('プログラム終了')