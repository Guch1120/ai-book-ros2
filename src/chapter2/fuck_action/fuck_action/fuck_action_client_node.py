import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from fuck_interface.action import StringCommand

class FuckActionClient(Node):
    def __init__(self):
        super().__init__('fuck_action_client_node')
        self._action_client = ActionClient(self, StringCommand, 'command')

    def send_goal(self, order):
        goal_mgs = StringCommand.Goal()
        goal_mgs.command = order
        self._action_client.wait_for_server()
        return self._action_client.send_goal_async(
            goal_mgs, feedback_callback=self.feedback_callback
        )

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'フィードバック受信中:残り{feedback_msg.feedback.process}[s]')

def main():
    rclpy.init()
    fuck_action_client = FuckActionClient()
    order = input('What?')
    future = fuck_action_client.send_goal(order)
    rclpy.spin_until_future_complete(fuck_action_client,future)
    goal_handle = future.result()

    if not goal_handle.accepted:
        fuck_action_client.get_logger().info('Denied')
    else:
        fuck_action_client.get_logger().info('OK')
        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(fuck_action_client, result_future)
        result = result_future.result().result
        fuck_action_client.get_logger().info(f'結果{result.answer}')

    fuck_action_client.destroy_node()   
    rclpy.shutdown()