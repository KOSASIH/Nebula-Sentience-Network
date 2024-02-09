class Resource:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.available_capacity = capacity

class Task:
    def __init__(self, id, demand, urgency):
        self.id = id
        self.demand = demand
        self.urgency = urgency

class ResourceManager:
    def __init__(self, resources):
        self.resources = resources

    def allocate_resources(self, tasks):
        allocated_resources = []
        sorted_tasks = sorted(tasks, key=lambda x: x.urgency, reverse=True)

        for task in sorted_tasks:
            for resource in self.resources:
                if resource.available_capacity >= task.demand:
                    allocated_resources.append((task.id, resource.id))
                    resource.available_capacity -= task.demand
                    break

        return allocated_resources

# Example usage
resources = [
    Resource(1, 100),
    Resource(2, 200),
    Resource(3, 150)
]

tasks = [
    Task(1, 50, 3),
    Task(2, 100, 2),
    Task(3, 75, 1)
]

resource_manager = ResourceManager(resources)
allocated_resources = resource_manager.allocate_resources(tasks)

print(allocated_resources)
