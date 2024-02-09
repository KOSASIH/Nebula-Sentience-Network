class Task:
    def __init__(self, task_id, task_name, assigned_to=None, status='In Progress'):
        self.task_id = task_id
        self.task_name = task_name
        self.assigned_to = assigned_to
        self.status = status

    def assign_task(self, assigned_to):
        self.assigned_to = assigned_to

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return f'Task ID: {self.task_id}\nTask Name: {self.task_name}\nAssigned To: {self.assigned_to}\nStatus: {self.status}'


class CollaborationPlatform:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_id, task_name):
        task = Task(task_id, task_name)
        self.tasks.append(task)

    def assign_task(self, task_id, assigned_to):
        task = self.get_task_by_id(task_id)
        if task:
            task.assign_task(assigned_to)
        else:
            print(f'Task with ID {task_id} does not exist.')

    def update_task_status(self, task_id, status):
        task = self.get_task_by_id(task_id)
        if task:
            task.update_status(status)
        else:
            print(f'Task with ID {task_id} does not exist.')

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks


# Example usage
collaboration_platform = CollaborationPlatform()

# Create tasks
collaboration_platform.create_task(1, 'Implement feature A')
collaboration_platform.create_task(2, 'Test feature B')
collaboration_platform.create_task(3, 'Document feature C')

# Assign tasks
collaboration_platform.assign_task(1, 'John')
collaboration_platform.assign_task(2, 'Sarah')

# Update task status
collaboration_platform.update_task_status(1, 'In Progress')
collaboration_platform.update_task_status(2, 'Completed')

# Get all tasks
all_tasks = collaboration_platform.get_all_tasks()
for task in all_tasks:
    print(task)
    print('--------------------------')
