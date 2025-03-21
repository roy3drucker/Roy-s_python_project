import json
import logging
import subprocess
import jsonschema
from jsonschema import validate
from src.machine import Machine


EXISTS_MACHINES_PATH = "configs/instances.json"
LOGS_PATH = "logs/provisioning.log"


def logging_setup():
    """
    Set up the logging configuration
    """

    logging.basicConfig(
        filename=LOGS_PATH,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Setting up logger")


def set_up_machine_object(name):
    """
    Set up a new machine object with the user input
    """

    # Get machine details from the user
    ip = input("Enter the IP address: ")
    os = input("Enter the operating system: ")
    cpu = input("Enter CPU configuration: ")
    ram = int(input("Enter RAM size in GB: "))

    # Create a new machine object
    new_machine = Machine(name, ip, os, cpu, ram)

    logging.info("User machine object details:")
    logging.info(new_machine.get_dict())

    return new_machine


def validate_machine(new_machine):
    """
    Validate the machine details
    """
    
    machine_details = new_machine.get_dict()

    try:
        # Validate the machine details Using jsonschema validation
        validate(instance=machine_details, schema=new_machine.aprroved_schema())
        logging.info("Valid machine configuration!")

    except jsonschema.exceptions.ValidationError as e:
        logging.error(f"Validation Error: {e.message}")

    # Open old machine file
    with open(EXISTS_MACHINES_PATH, "r") as file:
        machines = json.load(file)
        for machine in machines:
            # Check if the machine with the same IP address already exists
            if machine["ip"] == machine_details["ip"]:
                logging.error(f"Machine with ip address: {machine_details['ip']} already exists.")
                return False
    return True
   

def save_to_json(new_machines):
    """
    Function to save the new machines to the existing machines file
    """

    # Open the file with existing machines
    with open(EXISTS_MACHINES_PATH, "r") as file:
        old_machines = json.load(file)
        logging.info(f"Old machines: {old_machines}")

    # Add new machines to the existing machines
    old_machines.extend(new_machines)
    logging.info(f"Adding new machines: {new_machines}")
    
    # Save the updated machines to the file
    with open(EXISTS_MACHINES_PATH, "w") as file:
        json.dump(old_machines, file, indent=4)

    logging.info("New machines added to the file.")
   

def run_nginx_installtion():
    """
    Run the Nginx installation script
    """

    script_path = "Scripts/nginx_installtion.sh"

    try:
        # Run script using subprocess
        result = subprocess.run(["bash", script_path], check=True, capture_output=True, text=True)
        logging.info("Bash script output:")
        logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Error executing Bash script:")
        logging.error(e.stderr)
        exit(1)


def setup_manager():
    """
    Main function to manage the machine setup
    """

    logging.info("Starting machine setup manager")
    new_machines = []
    
    while True:
        # Get machine name from the user or finish the setup
        name = input("Please enter machine name (or 'done' to finish): ")

        if name.lower() == 'done':
            break
        
        # Set up a new machine object
        new_machine_object = set_up_machine_object(name)

        # Validate the machine details
        verify_machine = validate_machine(new_machine_object)
        logging.info(f"Machine validation status: {verify_machine}")

        # Verify if the machine details are valid
        if verify_machine:
            new_machines.append(new_machine_object.get_dict())

    logging.info(f"Finish setting up machine now save it to {EXISTS_MACHINES_PATH}")

    # Save the new machines to the file
    save_to_json(new_machines)
    
    # Ask the user if they want to install Nginx
    print("This script can also install Nginx for you.")
    install_script = input("Do you want to install Nginx? (yes/no): ")
    if install_script.lower() == "yes":
        run_nginx_installtion()

    logging.info("Machine setup manager finished")


if __name__ == "__main__":
    """
    Main function to run the machine setup manager
    """

    logging_setup()
    setup_manager()
    