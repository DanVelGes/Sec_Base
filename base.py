import socket
import subprocess

import re

# Get IP
def get_ip(url):
  try:
    ip = socket.gethostbyname(url)
    return ip
  except:
    return "Unable to resolve hostname"

# Run subprocess and print output
def run_subprocess(command):
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  while True:
      line = process.stdout.readline()
      if not line:
          break
      print(line.decode().strip())

# Main function
def main():
  url = "www.URL.com"
  ip = get_ip(url)
  
  print(f"The IP address of {url} is {ip}")

  # List of commands to run
  commands = [

      # Need to figure out how tu make output file to add IP dinamicly
      ["nikto", "-h", ip, "-o", "nikto-output.txt"],
      # Next one, need to think best way to use IP more dinamicly
      ["gobuster", "dir", "-u", "http://IP", "-w", "usr/share/seclists/Discover/Web-Content/common.txt"],
      ["nmap", "-sV", "-p-", "-v", ip]
  ]

  # Run each command
  for command in commands:
      print("============================================")
      print(f"Running {command[0]} scan...")
      print("============================================")
      run_subprocess(command)

### Using Re-gex and grom TXT file we extract ports and save them in separated one

# # Extract port numbers from the nmap output
# port_numbers = re.findall(r"\d+/\w+", nmap_output)

# # Write the port numbers to a new file
# with open("nmap-ports.txt", "w") as f:
#   for port in port_numbers:
#     f.write(port + "\n")

  # Main function
if __name__ == "__main__":
  main()