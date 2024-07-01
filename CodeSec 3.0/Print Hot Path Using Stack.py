from collections import defaultdict

def parse_trace_log(trace_log):
    logs = []
    for line in trace_log.split('\n'):
        if line.strip():
            parts = line.split()
            timestamp = int(parts[0])
            event_type = parts[1]
            function_name = parts[2]
            logs.append((timestamp, event_type, function_name))
    return logs

def find_hot_path(logs):
    stack = []
    call_times = defaultdict(int)
    active_calls = {}

    for timestamp, event_type, function_name in logs:
        if event_type == 'start':
            stack.append((function_name, timestamp))
        elif event_type == 'end':
            if stack:
                start_function, start_time = stack.pop()
                if start_function == function_name:
                    duration = timestamp - start_time
                    current_path = tuple(func for func, _ in stack + [(function_name,)])
                    call_times[current_path] += duration
                else:
                    raise ValueError(f"Unmatched end event for function: {function_name}")

    hot_path = max(call_times, key=call_times.get)
    return hot_path, call_times[hot_path]

def main(trace_log):
    logs = parse_trace_log(trace_log)
    hot_path, hot_path_time = find_hot_path(logs)
    print("Hot Path:", " -> ".join(hot_path))
    print("Execution Time:", hot_path_time, "ms")

# Example trace log input
trace_log = """
10 start anand
20 start login
30 start send
50 end send
60 end login
70 start read
80 start fread
100 end fread
120 start fread
140 end fread
160 start fread
180 end fread
200 end read
250 end anand
"""

main(trace_log)
