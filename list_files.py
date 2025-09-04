import subprocess

def list_directory_contents():
    """
    Runs the 'ls -l' shell command and prints its output.
    """
    # The command to run as a list of strings
    command = ["ls", "-l"]

    # Use subprocess.run() to run the command and capture the output
    # `capture_output=True` stores the output and error streams
    # `text=True` decodes the output as a string instead of bytes
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the command was successful (return code 0 means success)
    if result.returncode == 0:
        print("Command ran successfully. Here is the output:")
        print(result.stdout)
    else:
        print("Command failed with an error. Here is the error:")
        print(result.stderr)

# Run the function
list_directory_contents()