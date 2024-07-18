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
        "qdf": system.get("qdf"),  # Using .get() in case QDF is not present
        "kvm": system["kvm"],
        "kvm_port": system.get("kvm_port"),  # Using .get() in case KVM port is not present
        "power_level": system["power_level"],
        "status": system["status"],
        "link": system["link"]
    }

def list_serial(systems) -> list:
    return [individual_serial(system) for system in systems]


def individual_serial(accounting: Dict) -> Dict:
    return {
        "id": str(accounting["_id"]),
        "name": accounting["name"],
        "run_type": accounting["run_type"],
        "purpose": accounting["purpose"],
        "user_email": accounting["user_email"],
        "workloads": accounting["workloads"],
        "use_existing_image": accounting["use_existing_image"],
        "skuCustom": accounting.get("skuCustom", {}),
        "skuOotb": accounting.get("skuOotb", {}),
        "regressionTest": accounting.get("regressionTest", "No"),
        "configs": accounting.get("configs", {}),
        "schedule": accounting.get("schedule", "1m"),
        "start_date": accounting["start_date"].isoformat(),
        "end_date": accounting["end_date"].isoformat(),
        "type": accounting.get("type", "New")
    }