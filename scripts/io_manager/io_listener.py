import rospy
from std_msgs.msg import UInt16


class IoListener():
    def __init__(self):
        self._inputs = [0, 0, 0, 0, 0, 0, 0, 0]
        self._outputs = [0, 0, 0, 0, 0, 0, 0, 0]
        self.input_subs = [rospy.Subscriber(
            'io/input/port%d' % (i), UInt16, self.input_callback, i, queue_size=10) for i in range(1, 9)]
        self.output_subs = [rospy.Subscriber(
            'io/output/port%d' % (i), UInt16, self.output_callback, i, queue_size=10) for i in range(1, 9)]

    def input_callback(self, msg, port):
        self._inputs[port-1] = msg.data

    def output_callback(self, msg, port):
        self._outputs[port-1] = msg.data

    def reset_inputs_outputs(self):
        self._inputs = [0, 0, 0, 0, 0, 0, 0, 0]
        self._outputs = [0, 0, 0, 0, 0, 0, 0, 0]

    def get_inputs(self):
        return self._inputs

    def get_outputs(self):
        return self._outputs


if __name__ == '__main__':
    rospy.init_node('io_listener', anonymous=True)
    listener1 = IoListener()
    rospy.spin()
