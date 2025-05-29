import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from fx_stream_msgs.action import OverlaySetting
from fx_stream_msgs.msg import OverlaySetting as OverlaySettingMsg


class OverlayClient(Node):
    def __init__(self):
        super().__init__('overlay_action_client')
        self._action_client = ActionClient(self, OverlaySetting, '/fx_276730383020104/setting_overlay')

    def send_goal(self):
        msg = OverlaySettingMsg(
            enable_overlay=True,
            enable_source_mode=True,
            number_of_sources=3,
            range=3,
            threshold=10,
            range=1
        )

        goal_msg = OverlaySetting.Goal()
        goal_msg.setting = msg

        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected...')
            return

        self.get_logger().info('Goal accepted!')
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f'Result received: {result.setting}')
        rclpy.shutdown()

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback: {feedback.setting}')


def main(args=None):
    rclpy.init(args=args)
    client = OverlayClient()
    client.send_goal()
    rclpy.spin(client)


if __name__ == '__main__':
    main()
