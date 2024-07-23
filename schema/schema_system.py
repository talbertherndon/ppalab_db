from typing import Dict


def individual_serial(system) -> dict:
    return {
        "id": str(system["_id"]),
        "vendor": system["vendor"],
        "family": system["family"],
        "product_name": system["product_name"],
        "system_type": system["system_type"],
        "memory_type": system["memory_type"],
        "memory_size": system["memory_size"],
        "memory_speed": system["memory_speed"],
        "system_category": system["system_category"],
        "qdf": system.get("qdf"),  # Using .get() in case QDF is not present
        "kvm": system["kvm"],
        "kvm_port": system.get("kvm_port"),  # Using .get() in case KVM port is not present
        "power_level": system["power_level"],
        "status": system["status"],
        "link": system["link"]
    }

def list_serial(systems) -> list:
    return [individual_serial(system) for system in systems]
