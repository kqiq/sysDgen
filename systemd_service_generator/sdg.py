
   # systemd_service_generator/generator.py 
   import os
   import json
   import argparse

   def generate_systemd_service(service_name, description, workingDir, exec_start, user="www-data"):
       service_file_content = f"""
       [Unit]
       Description={description}
       After=network.target

       [Service]
       User={user}
       Group={user}
       ExecStart={exec_start}
       Restart=always
       RestartSec=10
       WorkingDirectory={workingDir}

       [Install]
       WantedBy=multi-user.target
       """

       service_file_content = service_file_content.strip()

       service_file_path = f"/etc/systemd/system/{service_name}.service"

       try:
           with open(service_file_path, 'w') as service_file:
               service_file.write(service_file_content)
           print(f"Systemd service file created at {service_file_path}")

           # Reload systemd manager configuration
           os.system("systemctl daemon-reload")

           print("Systemd daemon reloaded.")

           print(f"enabling the service -> {service_name}")
           os.system(f"systemctl enable {service_name}")

           print(f"Service {service_name} enabled to start at boot.")

           print(f"starting the service -> {service_name}")
           os.system(f"systemctl start {service_name}")

           print(f"Service {service_name} started to start at boot.")

           os.system("systemctl daemon-reload")

           print(f"Service {service_name} created and activated !.")

       except PermissionError:
           print("Permission denied: You need to run this script with sudo or as root.")
       except Exception as e:
           print(f"An error occurred: {e}")

   def main():
       parser = argparse.ArgumentParser(description="Generate a systemd service file from a configuration file.")
       parser.add_argument("config_path", type=str, help="Path to the JSON configuration file")

       args = parser.parse_args()
       config_file_path = args.config_path

       try:
           with open(config_file_path, 'r') as config_file:
               config = json.load(config_file)

           service_name = config.get("service_name")
           description = config.get("description")
           exec_start = config.get("exec_start")
           user = config.get("user", "www-data")
           workingDir = config.get('workingDirectory')

           generate_systemd_service(service_name, description, workingDir, exec_start, user)

       except FileNotFoundError:
           print(f"Configuration file {config_file_path} not found.")
       except json.JSONDecodeError:
           print(f"Error decoding JSON from the configuration file {config_file_path}.")
       except Exception as e:
           print(f"An error occurred: {e}")

   if __name__ == "__main__":
       main()
