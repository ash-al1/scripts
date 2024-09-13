import socket

rtsp_paths = [
    '/', '/live', '/stream1', '/channel/1', '/video', '/h264', '/mpeg4', '/main', '/cam/realmonitor',
]

ip = "24.220.96.74"
port = 554

def send_describe_request(ip, port, path):
    describe_request = (
        f"DESCRIBE rtsp://{ip}:{port}{path} RTSP/1.0\r\n"
        "CSeq: 1\r\n"
        "User-Agent: TestClient\r\n"
        "Accept: application/sdp\r\n\r\n"
    )
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((ip, port))
            s.send(describe_request.encode())
            
            response = s.recv(4096).decode()
            return response
    except socket.error as e:
        print(f"Socket error: {e}")
        return None

def find_rtsp_stream(ip, port, paths):
    for path in paths:
        print(f"Trying path: {path}")
        response = send_describe_request(ip, port, path)
        
        if response:
            print(f"Response for {path}: \n{response}")
            if "200 OK" in response:
                print(f"Stream found at path: {path}")
                return path
            elif "401 Unauthorized" in response:
                print("Authorization required, check credentials.")
                break
            elif "404 Stream Not Found" in response:
                print(f"Stream not found at {path}. Trying next...")
            else:
                print(f"Unexpected response at {path}: {response}")
        else:
            print(f"No response for {path}.")
    
    print("No valid stream path found.")
    return None

correct_path = find_rtsp_stream(ip, port, rtsp_paths)

if correct_path:
    print(f"The correct RTSP stream is located at: rtsp://{ip}:{port}{correct_path}")
else:
    print("Unable to find a valid RTSP stream.")

