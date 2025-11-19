import time , random
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from fuck_interface.action import StringCommand

class FuckActionServer(Node):
    def __init__(self):
        super().__init__('fuck_action_server')
        self.__action_server = ActionServer(
            self, StringCommand , 'command' ,
            execute_callback=self.execute_callback ,
        )
        self.food = ['apple',  'banana', 'candy']

    def execute_callback(self, goal_handle):
        feedback = StringCommand.Feedback()
        count = random.randint(5,10)

        while count > 0:
            self.get_logger().info(f'フェードバック送信中:残り{count}[s]')
            feedback.process = f'{count}'
            goal_handle.publish_feedback(feedback)
            count -= 1
            time.sleep(1)
        
        item = goal_handle.request.command
        result = StringCommand.Result()
        if item in self.food:
            result.answer = f'はい {item}です'
        else:
            result.answer = f'{item}を見つけれませんでした'
        goal_handle.succeed()
        self.get_logger().info(f'ゴールの結果{result.answer}')
        return result

def main():
    rclpy.init()
    fuck_action_server = FuckActionServer()
    print('サーバ開始')
    try:
        rclpy.spin(fuck_action_server)
    except KeyboardInterrupt:
        pass
    rclpy.try_shutdown()
    print('サーバ終了')

if __name__ == '__main__':
    main()
