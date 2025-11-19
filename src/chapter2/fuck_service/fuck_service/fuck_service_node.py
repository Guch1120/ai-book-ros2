import time 
import rclpy
from rclpy.node import Node
from fuck_interface.srv import StringCommand

class BringmeService(Node):
    def __init__(self):
        super().__init__('bringme_service')
        self.service = self.create_service(StringCommand, 'command' , self.callback)
        self.food = ['apple','banana','candy']
    def callback(self,request,respons):
        time.sleep(1)
        item = request.command
        if item in self.food:
            respons.answer = f"はい {item}です"
        else:
            respons.answer = f"{item}が見つからない"
        self.get_logger().info(f"レスポンス:{respons.answer}")
        return respons

def main():
    rclpy.init()
    bringmeService = BringmeService()
    try:
        rclpy.spin(bringmeService)
    except KeyboardInterrupt:
        pass
    rclpy.try_shutdown()
    print("サーバー終了")