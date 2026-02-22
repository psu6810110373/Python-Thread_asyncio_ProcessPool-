import concurrent.futures
import time
import os

def save_to_log(log_data):
    with open("server_logs.txt", "a", encoding="utf-8") as f:
        f.write(log_data + "\n")
    return f"เขียนข้อมูล '{log_data}' ลงไฟล์แล้ว"

if __name__ == "__main__":
    scan_results = [
        "google.com - ONLINE", 
        "github.com - ONLINE", 
        "invalid-domain.local - OFFLINE"
    ]
    
    if os.path.exists("server_logs.txt"):
        os.remove("server_logs.txt")
        
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as thread_pool:
        results = list(thread_pool.map(save_to_log, scan_results))
        
    for res in results:
        print(res)
        
    print(f"เวลาทำงาน: {time.time() - start_time:.2f} วินาที")