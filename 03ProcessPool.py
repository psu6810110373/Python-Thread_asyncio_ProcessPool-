import concurrent.futures
import hashlib
import time

def secure_hash_log(log_data):
    hashed = log_data.encode()
    for _ in range(500_000):
        hashed = hashlib.sha256(hashed).digest()
    return f"SHA-256 ของ '{log_data.split(' ')[0]}' -> {hashed.hex()[:16]}..."

if __name__ == "__main__":
    scan_results = [
        "google.com - ONLINE", 
        "github.com - ONLINE", 
        "invalid-domain.local - OFFLINE"
    ]
    
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as process_pool:
        results = list(process_pool.map(secure_hash_log, scan_results))
        
    for res in results:
        print(res)
        
    print(f"เวลาทำงาน: {time.time() - start_time:.2f} วินาที")