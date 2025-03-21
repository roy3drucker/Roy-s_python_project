import json
import logging
import subprocess
import jsonschema
from jsonschema import validate
from src.machine import Machine


EXISTS_MACHINES_PATH = "configs/instances.json"
LOGS_PATH = "logs/provisioning.log"


def set_up_machine_object(name):
    ip = input("Enter the IP address: ")
    os = input("Enter the operating system (e.g., Ubuntu or CentOS): ")
    cpu = input("Enter CPU configuration (e.g., 2vCPU): ")
    ram = int(input("Enter RAM size in GB: "))
    new_machine = Machine(name, ip, os, cpu, ram)
    
    logging.info("User machine object details:")
    logging.info(new_machine.get_dict())

    return new_machine


def validate_machine(new_machine):
    machine_details = new_machine.get_dict()

    try:
        validate(instance=machine_details, schema=new_machine.aprroved_schema())
        logging.info("Valid machine configuration!")

    except jsonschema.exceptions.ValidationError as e:
        logging.error(f"Validation Error: {e.message}")

    with open(EXISTS_MACHINES_PATH, "r") as file:
        machines = json.load(file)
        for machine in machines:
            if machine["ip"] == machine_details["ip"]:
                logging.ERROR(f"Machine with ip address: {machine_details['ip']} already exists.")
                return False
    return True
   

def save_to_json(new_machines):
    old_machines = []
    with open(EXISTS_MACHINES_PATH, "r") as file:
        old_machines = json.load(file)
        logging.info(f"Old machines: {old_machines}")
    
    old_machines.extend(new_machines)
    logging.info(f"Adding new machines: {new_machines}")

    with open(EXISTS_MACHINES_PATH, "w") as file:
        json.dump(old_machines, file, indent=4)

    logging.info("New machines added to the file.")
   

def run_bash_script():
    script_path = "Scripts/nginx_installtion.sh"

    try:
        result = subprocess.run(["bash", script_path], check=True, capture_output=True, text=True)
        logging.info("Bash script output:")
        logging.info(result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Error executing Bash script:")
        logging.error(e.stderr)
        exit(1)


def logging_setup():
    logging.basicConfig(
        filename=LOGS_PATH,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Setting up logger")


def setup_manager():
    logging.info("Starting machine setup manager")
    new_machines = []
    
    while True:
        name = input("Please enter machine name (or 'done' to finish): ")

        if name.lower() == 'done':
            break
        
        new_machine_object = set_up_machine_object(name)
        verify_machine = validate_machine(new_machine_object)
        logging.info(f"Machine validation status: {verify_machine}")

        if verify_machine:
            new_machines.append(new_machine_object.get_dict())

    logging.info(f"Finish setting up machine now save it to {EXISTS_MACHINES_PATH}")
    save_to_json(new_machines)
    
    print("This script can also install Nginx for you.")
    install_script = input("Do you want to install Nginx? (yes/no): ")
    if install_script.lower() == "yes":
        run_bash_script()

    logging.info("Machine setup manager finished")


if __name__ == "__main__":
    logging_setup()
    setup_manager()
    