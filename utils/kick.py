import multiprocessing
import time
from rich import print
from rich.console import Console

console = Console()
max_threads = 10
threads_count = min(multiprocessing.cpu_count(), max_threads)

def deauth_Method_1(target_addr, packages_size):
    # Windows doesn't support `l2ping`, so this is a placeholder.
    print(f"Simulating Deauth attack on {target_addr} with {packages_size} packets...")

def _kick_(target_addr, packages_size, threads_count, start_time=1):
    for i in range(start_time, 0, -1):
        console.print(f'[red] :rocket: Starting Deauth attack in {i} seconds...')
        time.sleep(1)
    console.print('[red] :rocket: Attack Started')

    with multiprocessing.Pool(processes=threads_count) as pool:
        results = [pool.apply_async(deauth_Method_1, args=(target_addr, packages_size)) for _ in range(threads_count)]
        [result.get() for result in results]
