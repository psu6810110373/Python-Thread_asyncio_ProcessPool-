import asyncio
import time

async def check_sever(host, port=443):
    try :
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(host,port), timeout= 3.0
        ) 
        writer.close()
        await writer.wait_closed()
        return f"{host} ONLINE"
    except Exception:
        return f"{host} OFFLINE"
    
async def scan_servers(hosts):
    task = [check_sever(host) for host in hosts]
    return await asyncio.gather(*task)


if __name__ == '__main__':
    hosts_to_check = ["google.com", "github.com", "python.org", "invalid-domain-test.local"]
    start_time = time.time()
    results = asyncio.run(scan_servers(hosts_to_check))
    for res in results :
        print(res)
    print(f"เวลาทำงาน: {time.time() - start_time:.2f} วินาที")