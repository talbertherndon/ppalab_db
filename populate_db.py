from pymongo import MongoClient
from config.database import system_collection

def insert_systems(systems):
    for system in systems:
        system_collection.insert_one(system)
    print(f"Database populated with {len(systems)} systems.")

client_systems = [
    {
        "system_id": "1",
        "vendor": "Intel",
        "family": "RPL",
        "product_name": "i9-13900K",
        "system_type": "RVP",
        "memory_type": "DDR5",
        "memory_size": "32GB",
        "memory_speed": "3200MHz",
        "qdf": "NA",
        "kvm": "1",
        "kvm_port": "4",
        "power_level": "125W",
        "status": "Up",
        "link": "Direct link to the machine on KVM",
        "system_category": "client"
    },
    {
        "system_id": "2",
        "vendor": "Intel",
        "family": "LNL",
        "product_name": "Ultra7-266V",
        "system_type": "RVP",
        "memory_type": "LPDDR5",
        "memory_size": "16GB",
        "memory_speed": "8600MHz",
        "qdf": "Q5HJ",
        "kvm": "1",
        "kvm_port": "17",
        "power_level": "17W",
        "status": "Up",
        "link": "",
        "system_category": "client"
    },
    {
        "system_id": "3",
        "vendor": "Intel",
        "family": "LNL",
        "product_name": "Ultra9-",
        "system_type": "RVP",
        "memory_type": "LPDDR5",
        "memory_size": "32GB",
        "memory_speed": "8600MHz",
        "qdf": "L0LG",
        "kvm": "1",
        "kvm_port": "16",
        "power_level": "30W",
        "status": "Up",
        "link": "",
        "system_category": "client"
    },
    {
        "system_id": "4",
        "vendor": "Intel",
        "family": "ARL",
        "product_name": "Ultra9-285K",
        "system_type": "RVP",
        "memory_type": "DDR5",
        "memory_size": "64GB",
        "memory_speed": "5600MHz",
        "qdf": "Q5HA",
        "kvm": "1",
        "kvm_port": "7",
        "power_level": "125W",
        "status": "Up",
        "link": "",
        "system_category": "client"
    },
    {
        "system_id": "5",
        "vendor": "Intel",
        "family": "MTL",
        "product_name": "Ultra9-165U",
        "system_type": "RVP",
        "memory_type": "LPDDR5",
        "memory_size": "32GB",
        "memory_speed": "6400MHz",
        "qdf": "Q42C",
        "kvm": "1",
        "kvm_port": "18",
        "power_level": "15W",
        "status": "Up",
        "link": "",
        "system_category": "client"
    },
    {
        "system_id": "6",
        "vendor": "Intel",
        "family": "MTL",
        "product_name": "Ultra7-165H",
        "system_type": "RVP",
        "memory_type": "LPDDR5",
        "memory_size": "32GB",
        "memory_speed": "6400MHz",
        "qdf": "Q21W",
        "kvm": "1",
        "kvm_port": "8",
        "power_level": "28W",
        "status": "Up",
        "link": "",
        "system_category": "client"
    }
]

data_center_systems = [
    {
        "system_id": "7",
        "vendor": "Intel",
        "family": "EMR",
        "product_name": "8592+",
        "system_type": "RVP",
        "memory_type": "DDR5",
        "memory_size": "512GB",
        "memory_speed": "5600 MT/s",
        "qdf": "Q2SR",
        "kvm": "",
        "kvm_port": "",
        "power_level": "350W",
        "status": "Up",
        "link": "vnc 143.183.30.140",
        "system_category": "datacenter"
    },
    {
        "system_id": "8",
        "vendor": "Intel",
        "family": "GNR-AP",
        "product_name": "TBD",
        "system_type": "RVP",
        "memory_type": "DDR5-MCR",
        "memory_size": "1536GB",
        "memory_speed": "8800 MT/s",
        "qdf": "Q4WC",
        "kvm": "",
        "kvm_port": "",
        "power_level": "550W",
        "status": "Up",
        "link": "https://143.183.30.182/?next=/login#/",
        "system_category": "datacenter"
    },
    {
        "system_id": "9",
        "vendor": "AMD",
        "family": "Genoa",
        "product_name": "9654",
        "system_type": "OEM",
        "memory_type": "DDR5",
        "memory_size": "1536GB",
        "memory_speed": "4800 MT/s",
        "qdf": "",
        "kvm": "",
        "kvm_port": "",
        "power_level": "360W",
        "status": "Up",
        "link": "https://143.183.30.139/",
        "system_category": "datacenter"
    },
    {
        "system_id": "10",
        "vendor": "AMD",
        "family": "Bergamo",
        "product_name": "9754",
        "system_type": "OEM",
        "memory_type": "DDR5",
        "memory_size": "1536GB",
        "memory_speed": "4800 MT/s",
        "qdf": "",
        "kvm": "",
        "kvm_port": "",
        "power_level": "360W",
        "status": "Up",
        "link": "https://143.183.30.169/",
        "system_category": "datacenter"
    }
]

# Insert client systems
insert_systems(client_systems)

# Insert data center systems
insert_systems(data_center_systems)

print("All systems have been inserted into the database.")