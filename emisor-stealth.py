import scapy.all as scapy
import sys
import time

def encrypt_cesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def send_icmp_packet(data, seq_num):
    ip = "8.8.8.8"
    icmp_id = 12345  # Identificador

    packet = scapy.IP(dst=ip) / scapy.ICMP(id=icmp_id, seq=seq_num) / data
    scapy.send(packet)

def main():
    if len(sys.argv) != 3:
        print("Uso: python programa.py <texto> <corrimiento>")
        return

    text = sys.argv[1]
    shift = int(sys.argv[2])

    encrypted_text = encrypt_cesar(text, shift)
    seq_num = 1

    for char in encrypted_text:
        # Asegurar que el caracter cifrado ocupe al menos 1 byte
        char_data = bytes([ord(char)]) + b'\x00' * (8 - len(char.encode()))
        data = char_data + b'\x10'+ b'\x11'+ b'\x12'+ b'\x13'+ b'\x14' + b'\x15' + b'\x16' + b'\x17' + b'\x18' + b'\x19' + b'\x1a'+ b'\x1b' + b'\x1c' + b'\x1d' + b'\x1e' + b'\x1f'+ b'\x20' + b'\x21' + b'\x22' + b'\x23' + b'\x24' + b'\x25' + b'\x26' + b'\x27' + b'\x28' + b'\x29'+ b'\x2a' + b'\x2b' + b'\x2c' + b'\x2d' + b'\x2e' + b'\x2f'+ b'\x30' + b'\x31' + b'\x32' + b'\x33' + b'\x34' + b'\x35' + b'\x36' + b'\x37'          # 8 bytes con el caracter y 40 bytes de relleno
        send_icmp_packet(data, seq_num)
        seq_num += 1
        time.sleep(1)  # Esperar 1 segundo entre paquetes

if __name__ == "__main__":
    main()
