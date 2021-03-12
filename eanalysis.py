import os

"""
Python 3.6 or above is required

unit: 
    KiB = 1024 * byte           <- current one
    MiB = 1024 * 1024 * byte

x-axis: seq;
y-axis: each process in, each process out, clients in, clients out, servers in, servers out,
y-axis: clients in&out, servers in&out, master in, master out, master in&out
"""


"""
select the first *nettop.out file in the log dir
"""


def find_log_path(log_dir="./logs"):
    for filename in os.listdir(log_dir):
        if filename.endswith("nettop.out"):
            return os.path.join(log_dir, filename)


"""
    returns the number of lines should be in a chunk (NS + NC + 1)
"""


def get_chunk_size(f_path):
    out = f_path[f_path.rfind("NS"):]
    out = out.split("-")
    NS = int(out[0][2:])
    NC = int(out[1][2:])
    return NS + NC + 1


"""
    divide the log file to chunks, each chunk can be used to generate a snap

    ok_chunk: a chunk -- a list of lists -- has chunk_size outer lists is a ok_chunk

    first time see line.startswith("time"), do nothing
    the last (partial) chunk of log will not be returned
"""


def divide_log(f_path):
    chunks = []
    with open(f_path) as f:
        chunk = []
        for line in f:
            if line.startswith("time") and chunk != []:
                chunks.append(chunk)
                chunk = []
            else:
                chunk.append(line.split())

    # remove not-ok-chunks
    first_ok = 0
    last_ok = len(chunks)-1
    chunk_size = get_chunk_size(f_path)

    while len(chunks[first_ok]) != chunk_size:
        first_ok += 1
    while len(chunks[last_ok]) != chunk_size:
        last_ok -= 1
    chunks = chunks[first_ok:last_ok+1]
    print("first_ok =", first_ok, "last_ok =", last_ok,
          "len(chunks) =", len(chunks), "chunk_size = ", chunk_size)

    # sanity check
    for i, chunk in enumerate(chunks):
        for line in chunk:
            assert len(line) == 4
        assert len(chunk) == len(chunks[0])
    return chunks


def create_snap_list(chunks, unit="MB"):
    snap_list = []
    for i, chunk in enumerate(chunks):
        snap = {"seq": i}
        for quad in chunk:
            if unit == "MB":
                snap[f"{quad[1]}-in"] = round(int(quad[2]) / (1024 * 1024), 2)
                snap[f"{quad[1]}-out"] = round(int(quad[3]) / (1024 * 1024), 2)
            elif unit == "KB":
                snap[f"{quad[1]}-in"] = round(int(quad[2]) / 1024, 2)
                snap[f"{quad[1]}-out"] = round(int(quad[3]) / 1024, 2)
            else:
                snap[f"{quad[1]}-in"] = quad[2]
                snap[f"{quad[1]}-out"] = quad[3]
        snap_list.append(snap)
    return snap_list


def write_snaps_to_file(log_path, snap_list):
    with open(log_path.replace("out", "txt"), "w") as f:
        for key in snap_list[0].keys():
            f.write(key + "\t")
        f.write("\n")
        for snap in snap_list:
            for val in snap.values():
                f.write(str(val) + "\t")
            f.write("\n")


def analysis():
    log_path = find_log_path()
    divided = divide_log(log_path)
    snaps = create_snap_list(divided, unit="KB")
    write_snaps_to_file(log_path, snaps)

analysis()