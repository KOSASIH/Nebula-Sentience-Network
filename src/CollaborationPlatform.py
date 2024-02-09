class Task:
    def __init__(self, task_id, task_name, assigned_to=None, status="Pending"):
        self.task_id = task_id
        self.task_name = task_name
        self.assigned_to = assigned_to
        self.status = status

class CollaborationPlatform:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_id, task_name):
        task = Task(task_id, task_name)
        self.tasks.append(task)

    def assign_task(self, task_id, assigned_to):
        task = self._get_task_by_id(task_id)
        if task:
            task.assigned_to = assigned_to
            task.status = "Assigned"
        else:
            print("Task not found.")

    def update_task_status(self, task_id, status):
        task = self._get_task_by_id(task_id)
        if task:
            task.status = status
        else:
            print("Task not found.")

    def complete_task(self, task_id):
        task = self._get_task_by_id(task_id)
        if task:
            task.status = "Completed"
        else:
            print("Task not found.")

    def get_task_status(self, task_id):
        task = self._get_task_by_id(task_id)
        if task:
            return task.status
        else:
            print("Task not found.")
            return None

    def _get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

# Example usage
platform = CollaborationPlatform()

# Create tasks
platform.create_task(1, "Implement feature A")
platform.create_task(2, "Test feature B")
platform.create_task(3, "Refactor code")

# Assign tasks
platform.assign_task(1, "John")
platform.assign_task(2, "Alice")

# Update task status
platform.update_task_status(1, "In Progress")
platform.update_task_status(2, "In Progress")

# Complete task
platform.complete_task(1)

# Get task status
status = platform.get_task_status(1)
print(status)  # Output: Completed
