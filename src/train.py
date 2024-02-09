import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

import syft as sy
from syft.frameworks.torch.fl import utils

# Define the decentralized learning algorithm using federated learning

# Step 1: Create a hook for PyTorch and initialize workers
hook = sy.TorchHook(torch)
alice = sy.VirtualWorker(hook, id="alice")
bob = sy.VirtualWorker(hook, id="bob")
workers = [alice, bob]

# Step 2: Load and preprocess the dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(
    root="data",
    train=True,
    transform=transform,
    download=True
)

# Step 3: Split the dataset into shards and distribute them to workers
federated_train_dataset = train_dataset.federate(workers)
federated_train_loader = sy.FederatedDataLoader(
    federated_train_dataset,
    batch_size=64,
    shuffle=True
)

# Step 4: Define the model architecture
model = nn.Sequential(
    nn.Linear(784, 512),
    nn.ReLU(),
    nn.Linear(512, 10),
    nn.LogSoftmax(dim=1)
)

# Step 5: Define the loss function and optimizer
criterion = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Step 6: Train the model using federated learning
def train(model, train_loader, optimizer, criterion):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            loss = loss.get().item()  # Get the loss value from the remote worker
            print('Loss: {:.6f}'.format(loss))

# Step 7: Run the training process on each worker
for epoch in range(5):
    model = model.send(alice)
    train(model, federated_train_loader, optimizer, criterion)
    model = model.get()  # Retrieve the updated model from the remote worker

    model = model.send(bob)
    train(model, federated_train_loader, optimizer, criterion)
    model = model.get()  # Retrieve the updated model from the remote worker

# Step 8: Aggregate the model updates using secure aggregation
model = utils.federated_avg(models=[model.send(alice), model.send(bob)])

# Step 9: Evaluate the aggregated model
test_dataset = datasets.MNIST(
    root="data",
    train=False,
    transform=transform,
    download=True
)

test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

def test(model, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader.dataset)
    accuracy = 100.0 * correct / len(test_loader.dataset)
    print('Test Loss: {:.6f}, Accuracy: {:.2f}%'.format(test_loss, accuracy))

model = model.get()  # Retrieve the aggregated model from the remote workers
test(model, test_loader)
