import socket
import subprocess

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
  url = "www.testdevlab.com"
  ip = get_ip(url)
  
  print(f"The IP address of {url} is {ip}")

  # List of commands to run
  commands = [
      ["nikto", "-h", ip],
      # Next one, need to think best way to use IP more dinamicly
      ["gobuster", "dir", "-u", "http://159.223.1.24", "-w", "usr/share/seclists/Discover/Web-Content/common.txt"],
      ["nmap", "-sV", "-p-", "-v", ip]
  ]

  # Run each command
  for command in commands:
      print("============================================")
      print(f"Running {command[0]} scan...")
      print("============================================")
      run_subprocess(command)

  # Main function
if __name__ == "__main__":
  main()