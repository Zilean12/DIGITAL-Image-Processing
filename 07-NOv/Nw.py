import threading
import random
import time

class Packet:
    def __init__(self, seq_num, data):
        self.seq_num = seq_num
        self.data = data

class Sender:
    def __init__(self, window_size, timeout):
        self.window_size = window_size
        self.timeout = timeout
        self.base = 0
        self.next_seq_num = 0
        self.buffer = [Packet(i, f"Data{i}") for i in range(self.window_size)]
        self.timer_event = threading.Event()

    def send_packets(self):
        for i in range(self.base, min(self.next_seq_num, self.base + self.window_size)):
            packet = self.buffer[i % self.window_size]
            print(f"Sending packet with sequence number {packet.seq_num}")
            # Simulate packet transmission over the network

        self.timer_event.clear()
        self.timer = threading.Thread(target=self.timeout_handler)
        self.timer.start()

    def timeout_handler(self):
        time.sleep(self.timeout)
        self.timer_event.set()
        print("Timeout occurred, resending packets")

    def receive_ack(self, ack_num):
        if self.base <= ack_num < self.next_seq_num:
            self.base = ack_num + 1
            print(f"Received ACK for sequence number {ack_num}")
            if self.base == self.next_seq_num:
                print("All packets acknowledged")
            else:
                self.timer_event.clear()
                self.timer = threading.Thread(target=self.timeout_handler)
                self.timer.start()

class Receiver:
    def __init__(self):
        self.expected_seq_num = 0

    def receive_packet(self, packet):
        if packet.seq_num == self.expected_seq_num:
            print(f"Received packet with sequence number {packet.seq_num}")
            # Process the received packet
            # Simulate sending an acknowledgment
            ack_num = packet.seq_num
            print(f"Sending ACK for sequence number {ack_num}")
            # Simulate packet transmission over the network
            self.expected_seq_num += 1
        else:
            print(f"Discarding out-of-order packet with sequence number {packet.seq_num}")

# Simulate network conditions
def simulate_network(sender, receiver, window_size, timeout, seq_num_loss, ack_delay):
    sender.window_size = window_size
    sender.timeout = timeout

    for i in range(10):
        sender.send_packets()
        # Simulate packet loss
        if random.random() < seq_num_loss:
            print("Simulating sequence number loss")
            continue

        ack_num = receiver.expected_seq_num - 1
        # Simulate acknowledgment delay
        time.sleep(ack_delay)
        sender.receive_ack(ack_num)

if __name__ == "__main__":
    sender = Sender(window_size=4, timeout=2)
    receiver = Receiver()

    # Simulate network conditions
    simulate_network(sender, receiver, window_size=4, timeout=2, seq_num_loss=0.2, ack_delay=1)
