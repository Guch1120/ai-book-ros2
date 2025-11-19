import rclpy
from rclpy.node import Node
from fuck_interface.srv import StringCommand

class BringmeClient(Node):
    def __init__(self):
        super().__init__('bringme_client_node')
        self.client = self.create_client(StringCommand , 'command')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('サービスは利用不可。待機。')
        self.request = StringCommand.Request()
    
    def send_request(self, order):
        self.request.command = order
        self.future = self.client.call_async(self.request)

def main():
    rclpy.init()
    bringmeclient = BringmeClient()
    order = input("何？")
    bringmeclient.send_request(order)

    while rclpy.ok():
        rclpy.spin_once(bringmeclient)
        if bringmeclient.future.done():
            try:
                respons = bringmeclient.future.result()
            except Exception as e:
                bringmeclient.get_logger().info(f'サービスの呼び出しに失敗')
            else:
                bringmeclient.get_logger().info(
                    f'\nリクエスト{bringmeclient.request.command} -> レスポンス: {respons.answer}'
                )
                break
    bringmeclient.destroy_node()
    rclpy.shutdown()