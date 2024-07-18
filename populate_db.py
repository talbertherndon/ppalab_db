from pymongo import MongoClient
from bson import ObjectId
from database import system_collection
import random

# Sample data
vendors = ["Intel", "AMD", "NVIDIA"]
families = ["RPL", "Zen", "Ampere"]
product_names = ["i9-13900K", "Ryzen 9 5950X", "RTX 3090"]
system_types = ["RVP", "Desktop", "Workstation"]
memory_types = ["DDR4", "DDR5"]
memory_speeds = ["3200MHz", "3600MHz", "4000MHz"]
statuses = ["Up", "Down", "Maintenance"]

def generate_random_system():
    return {
        "vendor": random.choice(vendors),
        "family": random.choice(families),
        "product_name": random.choice(product_names),
        "system_type": random.choice(system_types),
        "memory_type": random.choice(memory_types),
        "memory_size": random.choice([16, 32, 64, 128]),
        "memory_speed": random.choice(memory_speeds),
        "qdf": f"Q{random.randint(100000, 999999)}",
        "kvm": f"KVM{random.randint(1, 20)}",
        "kvm_port": random.randint(1, 10),
        "power_level": random.randint(50, 300),
        "status": random.choice(statuses),
        "link": f"http://kvm-link-{random.randint(1000, 9999)}.example.com"
    }

# Generate and insert 50 random systems
for _ in range(50):
    system = generate_random_system()
    system_collection.insert_one(system)

print("Database populated with 50 random systems.")