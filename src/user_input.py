def get_user_input():
    """Prompt the user for machine details."""
    name = input("Enter machine name (or 'done' to finish): ").strip()
    if name.lower() == 'done':
        return None
    
    os = input("Enter OS (Ubuntu/CentOS): ").strip()
    cpu = input("Enter CPU (e.g., 2): ").strip()
    ram = input("Enter RAM (e.g., 4GB): ").strip()

    return {"name": name, "os": os, "cpu": cpu, "ram": ram}
