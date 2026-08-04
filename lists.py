servers = ["web01", "web02", "web03"]

servers.append(input("Enter a new server name: "))
print(servers)

for server in servers:
    print(f"Checking {server} ({len(server)} characters)")
