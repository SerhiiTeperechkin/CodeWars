import base64

def to_base_64(string):
    msg_bytes = string.encode('utf-8')
    base64_bytes = base64.b64encode(msg_bytes)
    return base64_bytes.decode('utf-8').replace('=', '')
    
def from_base_64(string):
    string += '=' * (len(string) % 4)
    base64_bytes = string.encode('utf-8')
    msg_bytes = base64.b64decode(base64_bytes)
    return msg_bytes.decode('utf-8')
