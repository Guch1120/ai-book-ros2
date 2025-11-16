import rclpy
from rclpy.node import Node

class HappyNode(Node):
    def __init__(self):
        print("ノードの作成")
        super().__init__('happy_node')
        self.get_logger().info('ハッピーワールド')

def main():
    print('プログラム開始')
    rclpy.init()
    node = HappyNode()
    node.destroy_node()
    rclpy.destroy_node()
    rclpy.shutdown()
    print("プログラム終了")


if __name__ == '__main__':
    main()
