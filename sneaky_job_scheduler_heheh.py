import time
import sys
import subprocess

# This script runs my wife's command to the cluster at the specified time to avoid using Newton's
# stupid fucking broken scheduling system that makes her so mad! >:O Stupid Newton! Always on fire...

# GIVE MY WIFE A NODE!!! D:<

# Format for execution is as follows:
#    sneaky_job_scheduler_heheh.py "<command>" "<time>"

# Valid formats for time:
#    "<hour>:<minute> <AM/PM>"
#    "<hour>:<minute> <am/pm>"
#    "<hour_military>:<minute>"

# Process the time string >:3
def parse_time(time_str):
     
     # Split the time string into hours and minutes
     hours, minutes = time_str.split(':')
    
     # Check if the time is in AM/PM format
     if 'AM' in minutes or 'PM' in minutes or 'am' in minutes or 'pm' in minutes:
          minutes, minutes_ampm = minutes.split()

          # Check for stupid time AM/PM
          if int(hours) > 12 or int(hours) < 1:
               print("Ah, ah, ah! Woah, buddy! That time makes no sense! Ah, ah, ah! You are Goku.")
               print("I'm fucking LEAVING this bitch. Peace!")
               exit()

          # Convert hours to military time if it's PM
          if minutes_ampm == 'PM' or minutes_ampm == 'pm':
               hours = str((int(hours) + 12) % 24)
               
          # Account for the fucking rule where the zeroth hour of the day is marked as 12
          # for some stupid reason. It was probably the fucking Romans or the Egyptians
          if (minutes_ampm == 'AM' or minutes_ampm == 'am') and hours == "12":
               hours = '0'
               
     else:
          # Ensure that hours and minutes are two digits
          hours = hours.zfill(2)
          minutes = minutes.zfill(2)
          
     # Check for stupid time
     if int(hours) > 23 or int(hours) < 0 or int(minutes) > 60 or int(minutes) < 0:
          print("Ah, ah, ah! Woah, buddy! That time makes no sense! Ah, ah, ah! You are Goku.")
          print("I'm fucking LEAVING this bitch. Peace!")
          exit()

     # Return hours and minutes as integers
     return hours, minutes

# Example usage: Run the command "ls -l" at 10:30 AM
# run_command_at_specific_time(13, 15, "ls -l")

def run_command_at_specific_time(hour, minute, command):
     
     # Display current time
     print(f"\rCommand execute time: {hour}:{minute}", flush=True)
     while True:
          # Get current time
          current_time = time.localtime()
          print(f"\rCurrent time: {current_time.tm_hour:02d}:{current_time.tm_min:02d}", end='', flush=True)

          # Check if it's time to run the command
          if current_time.tm_hour == hour and current_time.tm_min == minute:
               print("\n\n===================================================")
               print("It's finally time! >:3!!! Executing the command...")
               print("===================================================\n")
               subprocess.run(command, shell=True)
               break  # Exit the loop after executing the command

          # Wait for one minute before checking again
          time.sleep(5)
          
def main():
     
     # Get parameters. 
     args = sys.argv
     command = args[1]
     time_str = args[2]
     
     # Get 24 hour time format and check for malicious input (DON'T TRY TO BREAK MY CODE! >:O)
     hour, minute = parse_time(time_str)
     
      # Run script if all looks good >:3
     run_command_at_specific_time(int(hour), int(minute), command)

if __name__ == "__main__":
    main()
