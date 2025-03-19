import json
from src.user_input import get_user_input
from configs.validation import validate_instance

CONFIG_PATH = "configs/instances.json"

def save_instances(instances):
    """Save instances to a JSON file."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(instances, f, indent=4)
    print(f" Data saved to {CONFIG_PATH}")

def main():
    machines = []
    while True:
        instance_data = get_user_input()
        if instance_data is None:
            break  # Exit loop if user stops input
        
        if validate_instance(instance_data):
            machines.append(instance_data)
        else:
            print(" Invalid input. Please try again.")

    if machines:
        save_instances(machines)

if __name__ == "__main__":
    main()
