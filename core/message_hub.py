import queue
from typing import Dict

class MessageHub:
    """message queue"""
    def __init__(self):
        self.queues: Dict[str, queue.Queue] = {}
        self._initialize_queues()

    def _initialize_queues(self):
        """program queue init"""
        program_names = ["program1", "program2", "program3", "program4"]
        for name in program_names:
            self.queues[name] = queue.Queue()

    def send_message(self, program_name: str, message: str):
        """send message to program queue"""
        if program_name in self.queues:
            self.queues[program_name].put(message)
            return True
        return False

    def get_message(self, program_name: str, timeout: float = None):
        """get message from program queue"""
        if program_name in self.queues:
            try:
                return self.queues[program_name].get(timeout=timeout)
            except queue.Empty:
                return None
        return None

    def get_queue_sizes(self):
        """get queue sizes"""
        return {name: q.qsize() for name, q in self.queues.items()}

# static message hub instance
message_hub = MessageHub()

