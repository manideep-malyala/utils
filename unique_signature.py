import uuid
from datetime import datetime

def unique_signature(k_bits=8):
    time_stamp = datetime.now().strftime('%Y%m%d%H%M%S')
    hex_uid = str(uuid.uuid4().hex)[:k_bits]
    return f"{time_stamp}-{hex_uid}"

print(unique_signature())
# 20250604202616-ed7cc457
