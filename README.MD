   # systemd_service_generator

   A tool to generate systemd service files from a configuration file.

   ## Installation

   ```bash
   pip install systemd_service_generator
   ```

   ## Usage

   ```bash
   sdg path/to/config.json
   ```

   ## Configuration File

   The configuration file should be a JSON file with the following structure:

   ```json
   {
       "service_name": "your_service_name",
       "description": "Your service description",
       "exec_start": "/path/to/your/executable",
       "user": "optional_user",
       "workingDirectory": "/path/to/working/directory"
   }
   ```