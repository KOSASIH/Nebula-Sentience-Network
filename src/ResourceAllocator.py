import psutil
import time

class PowerMonitor:
    def __init__(self):
        self.previous_power = psutil.cpu_percent()
    
    def get_power_consumption(self):
        current_power = psutil.cpu_percent()
        power_consumption = current_power - self.previous_power
        self.previous_power = current_power
        return power_consumption
    
class ResourceAllocator:
    def __init__(self, max_power_consumption):
        self.max_power_consumption = max_power_consumption
    
    def allocate_resources(self, participants, available_resources):
        total_power_consumption = sum(participant.power_consumption for participant in participants)
        if total_power_consumption <= self.max_power_consumption:
            return available_resources
        
        total_resources = sum(participant.resources for participant in participants)
        allocated_resources = {}
        for participant in participants:
            power_ratio = participant.power_consumption / total_power_consumption
            resource_allocation = power_ratio * total_resources
            allocated_resources[participant.id] = resource_allocation
        
        return allocated_resources
    
class PowerManager:
    def __init__(self):
        self.power_limit = None
    
    def set_power_limit(self, power_limit):
        self.power_limit = power_limit
    
    def manage_power(self, participants):
        for participant in participants:
            if participant.power_consumption > self.power_limit:
                participant.reduce_power_consumption()
            else:
                participant.increase_power_consumption()

# Example usage
participants = [
    Participant(id=1, power_consumption=20, resources=4),
    Participant(id=2, power_consumption=30, resources=6),
    Participant(id=3, power_consumption=40, resources=8)
]

max_power_consumption = 80

power_monitor = PowerMonitor()
resource_allocator = ResourceAllocator(max_power_consumption)
power_manager = PowerManager()

while True:
    power_consumption = power_monitor.get_power_consumption()
    allocated_resources = resource_allocator.allocate_resources(participants, available_resources)
    power_manager.set_power_limit(max_power_consumption)
    power_manager.manage_power(participants)
    
    # Use the allocated resources for computation
    
    time.sleep(1)
