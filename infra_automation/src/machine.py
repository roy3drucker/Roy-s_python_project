class Machine:
    def __init__(self, name, ip, os, cpu, ram):
        self.name = name
        self.ip = ip
        self.os = os 
        self.cpu = cpu 
        self.ram = ram

    def get_dict(self):
        return {
            "name": self.name,
            "ip": self.ip,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }
    
    def aprroved_schema(self):
        return {
            "type": "object",
            "properties": {
                "ip": {
                    "type": "string",
                    "format": "ipv4"
                },
                "os": {
                    "type": "string",
                    "enum": ["Ubuntu", "CentOS"]  # Extend this list if needed
                },
                "cpu": {
                    "type": "string",
                    "pattern": r"^\d+vCPU$"  # Ensures format like "2vCPU"
                },
                "ram": {
                    "type": "integer",
                    "minimum": 1  # RAM must be at least 1GB
                }
            },
            "required": ["ip", "os", "cpu", "ram"]
        }