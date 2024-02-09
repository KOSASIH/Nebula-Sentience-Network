import heapq

class Task:
    def __init__(self, task_id, urgency):
        self.task_id = task_id
        self.urgency = urgency

class Resource:
    def __init__(self, resource_id):
        self.resource_id = resource_id
        self.tasks = []
    
    def add_task(self, task):
        heapq.heappush(self.tasks, (task.urgency, task.task_id))
    
    def get_next_task(self):
        if self.tasks:
            _, task_id = heapq.heappop(self.tasks)
            return task_id
        return None

class ResourceManager:
    def __init__(self, num_resources):
        self.resources = [Resource(i) for i in range(num_resources)]
    
    def allocate_resource(self, task):
        resource = min(self.resources, key=lambda r: len(r.tasks))
        resource.add_task(task)
    
    def get_next_task(self, resource_id):
        return self.resources[resource_id].get_next_task()

# Example usage
num_resources = 5
resource_manager = ResourceManager(num_resources)

# Allocate tasks to resources
task1 = Task(1, 3)
task2 = Task(2, 2)
task3 = Task(3, 1)
task4 = Task(4, 2)

resource_manager.allocate_resource(task1)
resource_manager.allocate_resource(task2)
resource_manager.allocate_resource(task3)
resource_manager.allocate_resource(task4)

# Get next task for each resource
for i in range(num_resources):
    next_task = resource_manager.get_next_task(i)
    if next_task is not None:
        print(f"Resource {i} executing task {next_task}")
    else:
        print(f"Resource {i} has no tasks to execute")
