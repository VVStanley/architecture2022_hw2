import threading

from commands import act


class FightThread(threading.Thread):
    container = threading.local()
    queue = None

    def __init__(self, container, queue):
        self.queue = queue
        super().__init__(daemon=True)
        self.container = container

    def run(self):
        while True:
            api_command = self.queue.get()
            command = act.get(api_command.get("command"))
            command = command(api_command.get("id"))
            command.execute()
            self.queue.task_done()
