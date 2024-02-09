class Task:
    def __init__(self, task_id, task_name, assigned_to, status):
        self.task_id = task_id
        self.task_name = task_name
        self.assigned_to = assigned_to
        self.status = status

class TaskTracker:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_id, task_name, assigned_to):
        task = Task(task_id, task_name, assigned_to, "Pending")
        self.tasks.append(task)

    def update_task_status(self, task_id, status):
        for task in self.tasks:
            if task.task_id == task_id:
                task.status = status
                break

    def get_task_status(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task.status
        return None

    def get_assigned_tasks(self, assigned_to):
        assigned_tasks = []
        for task in self.tasks:
            if task.assigned_to == assigned_to:
                assigned_tasks.append(task)
        return assigned_tasks

    def get_all_tasks(self):
        return self.tasks


# Example usage
task_tracker = TaskTracker()

# Create tasks
task_tracker.create_task(1, "Task 1", "User A")
task_tracker.create_task(2, "Task 2", "User B")
task_tracker.create_task(3, "Task 3", "User C")

# Update task status
task_tracker.update_task_status(1, "In Progress")
task_tracker.update_task_status(2, "Completed")

# Get task status
task_status = task_tracker.get_task_status(1)
print(f"Task 1 status: {task_status}")

# Get assigned tasks
user_tasks = task_tracker.get_assigned_tasks("User B")
for task in user_tasks:
    print(f"Task {task.task_id}: {task.task_name}, Status: {task.status}")

# Get all tasks
all_tasks = task_tracker.get_all_tasks()
for task in all_tasks:
    print(f"Task {task.task_id}: {task.task_name}, Status: {task.status}")
