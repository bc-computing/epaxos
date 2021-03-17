import os

def find_total_requests(log_dir="./logs"):
    for filename in os.listdir(log_dir):
        if filename.endswith("-nettop.out"): # finds the first profile
            profile_name = filename[:len(filename)-len("-nettop.out")]
            num_of_clients = int(profile_name.split("-")[1][2:])
            requests_per_client = int(profile_name.split("-")[2][2:])
            return num_of_clients * requests_per_client

def find_client_log_names(log_dir="./logs"):
    for filename in os.listdir(log_dir):
        if filename.endswith("-nettop.out"): # finds the first profile
            profile_name = filename[:len(filename)-len("-nettop.out")]
            num_of_clients = int(profile_name.split("-")[1][2:])
            return [f"{profile_name}-client{i}.out"for i in range(num_of_clients)]

def find_max_runtime(log_dir="./logs"):
    time_list = []
    for fn in find_client_log_names(log_dir):
        with open(os.path.join(log_dir, fn)) as f:
            last = f.readlines()[-1].strip()
            time = float(last.split()[2])
            time_list.append(time)
    return max(time_list)

reqs = find_total_requests()
tim = find_max_runtime()
print("throughput", round(reqs / tim, 2), "requests/sec")