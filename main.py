import json

# Function to get machine details from the user
def get_machine_details():
    machines = []
    while True:
        # Get the machine name
        name = input("Please enter machine name (or 'done' to finish): ")
        if name.lower() == 'done':
            break

        # Get other machine details
        os = input("Enter the operating system (e.g., Ubuntu or CentOS): ")
        cpu = input("Enter CPU configuration (e.g., 2vCPU): ")
        ram = input("Enter RAM size (e.g., 4GB): ")

        # Create a dictionary for the machine details
        machine_data = {"name": name, "os": os, "cpu": cpu, "ram": ram}
        machines.append(machine_data)

    return machines

# Save the machine data to a JSON file
def save_to_json(machines):
    with open("configs/instances.json", "w") as file:
        json.dump(machines, file, indent=4)

# Running the processes
if __name__ == "__main__":
    machines = get_machine_details()
    save_to_json(machines)
