# Import necessary libraries

import numpy as np

# Define the class for the resource manager

class ResourceManager:
    def __init__(self, available_resources):
        self.available_resources = available_resources
        self.task_queue = []
    
    def add_task(self, task):
        self.task_queue.append(task)
    
    def allocate_resources(self):
        # Sort the task queue based on urgency
        self.task_queue.sort(key=lambda x: x.urgency, reverse=True)
        
        # Allocate resources based on demand and urgency
        for task in self.task_queue:
            if self.available_resources >= task.demand:
                self.available_resources -= task.demand
                task.execute()
                self.task_queue.remove(task)
    
    def release_resources(self, released_resources):
        self.available_resources += released_resources

# Define the class for the task

class Task:
    def __init__(self, demand, urgency):
        self.demand = demand
        self.urgency = urgency
    
    def execute(self):
        # Code to execute the task
        pass

# Example usage

# Create a resource manager with available resources
resource_manager = ResourceManager(100)

# Create tasks with their demand and urgency
task1 = Task(20, 5)
task2 = Task(30, 3)
task3 = Task(10, 7)

# Add tasks to the resource manager
resource_manager.add_task(task1)
resource_manager.add_task(task2)
resource_manager.add_task(task3)

# Allocate resources based on demand and urgency
resource_manager.allocate_resources()

# Release resources after task completion
resource_manager.release_resources(20)
resource_manager.release_resources(30)
resource_manager.release_resources(10)
