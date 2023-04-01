import ipaddress
import time

# Read IP ranges from list.txt
with open('ipd.txt', 'r') as file:
    ip_ranges = file.read().splitlines()

# Start the timer
start_time = time.time()
# Stop the timer and print the elapsed time
elapsed_time = time.time() - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")
# Generate a list of IPs for each range and save them to output.txt
with open('output.txt', 'a') as output_file:
    for ip_range in ip_ranges:
        network = ipaddress.ip_network(ip_range)
        for ip in network:
            output_file.write(str(ip) + '\n')


