import pyshark

keyMap = {
    '04': 'a', '05': 'b', '06': 'c', '07': 'd', '08': 'e', '09': 'f', '0a': 'g', '0b': 'h', '0c': 'i', '0d': 'j',
    '0e': 'k', '0f': 'l', '10': 'm', '11': 'n', '12': 'o', '13': 'p', '14': 'q', '15': 'r', '16': 's', '17': 't',
    '18': 'u', '19': 'v', '1a': 'w', '1b': 'x', '1c': 'y', '1d': 'z', '1e': '1', '1f': '2', '20': '3', '21': '4',
    '22': '5', '23': '6', '24': '7', '25': '8', '26': '9', '27': '0', '28': '\n', '2a': '\x08', '2c': ' ',
    '34': '"', '36': ',', '37': '.', '38': '?', '2d': '_', '2e': '!', '2f': '@', '30': '#', '31': '$', '33': ';',
    '30': '}', '2f': '{'
}

totFlag = []

f = pyshark.FileCapture('kren.pcap')

for p in f:
    try:
        payload = p.layers[-1].get_field_value('data')[-2:]  # Ambil 1 byte terakhir dari data
        
        char = keyMap.get(payload)
        
        if char:
            totFlag.append(char)
    except Exception as e:
        print(f"Error: {e}")
        continue

flags_str = ''.join(totFlag)

with open('flag.txt', 'w') as file:
    file.write(flags_str)

print('flag.txt')
print(flags_str)
