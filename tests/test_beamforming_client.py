import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from fx_stream_msgs.action import BeamformingSetting
from fx_stream_msgs.msg import BeamformingSetting as BeamformingSettingMsg


class BeamformingClient(Node):
    def __init__(self):
        super().__init__('beamforming_action_client')
        self._action_client = ActionClient(self, BeamformingSetting, '/fx_276730383020104/setting_beamforming')

    def send_goal(self):
        msg = BeamformingSettingMsg(
            autogain=False,
            gain=1.0,
            x_cal=0.0,
            y_cal=0.0,
            distance=5.0,
            high_cut=60000.0,
            low_cut=25000.0,
            l_point_0=580,
            l_point_1=20,
            l_point_2=290
        )

        goal_msg = BeamformingSetting.Goal()
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
    client = BeamformingClient()
    client.send_goal()
    rclpy.spin(client)


if __name__ == '__main__':
    main()
