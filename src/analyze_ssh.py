from collections import Counter

log_file = "data/sample_auth.log"

failed_attempts = Counter()

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip_address = parts[parts.index("from") + 1]
            failed_attempts[ip_address] += 1

print(failed_attempts)
print("Failed SSH logins by IP:")
print("------------------------")

for ip, count in failed_attempts.items():
    print(f"{ip}: {count} failed attempts")

# Detection rule: flag IPs with 3 or more failed attempts
threshold = 3

print("\nPotential suspicious activity:")
print("------------------------------")

for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"WARNING: {ip} has {count} failed login attempts")
