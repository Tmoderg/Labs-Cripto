import scapy.all as scapy
from colorama import Fore, Style

spanish_letter_freq = {
    'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68, 'f': 0.69, 'g': 1.01,
    'h': 0.70, 'i': 6.25, 'j': 0.44, 'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71,
    'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98, 't': 4.63, 'u': 3.93,
    'v': 0.90, 'w': 0.01, 'x': 0.22, 'y': 0.90, 'z': 0.52
}

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def calculate_letter_freq(text):
    letter_count = {}
    total_letters = 0

    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
            total_letters += 1

    letter_freq = {char: count / total_letters for char, count in letter_count.items()}
    return letter_freq

def calculate_similarity(freq1, freq2):
    return sum(abs(freq1[char] - freq2.get(char, 0)) for char in freq1)

def main():
    pcap_file = input("Ingrese el nombre del archivo pcapng: ")

    packets = scapy.rdpcap(pcap_file)
    payload = b""

    for packet in packets:
        if packet.haslayer(scapy.ICMP) and packet[scapy.ICMP].type == 8:  # ICMP Echo Request
            payload += packet[scapy.ICMP].load.replace(b':', b'')[:8]  # Considerar solo los primeros 8 bytes

    payload_str = payload.decode()

    best_message = ""
    best_shift = 0
    best_similarity = float('inf')

    for shift in range(26):
        decrypted_message = caesar_decrypt(payload_str, shift)
        letter_freq = calculate_letter_freq(decrypted_message)
        similarity = calculate_similarity(spanish_letter_freq, letter_freq)

        if similarity < best_similarity:
            best_similarity = similarity
            best_message = decrypted_message
            best_shift = shift

    for shift in range(26):
        decrypted_message = caesar_decrypt(payload_str, shift)
        if decrypted_message == best_message:
            print(Fore.GREEN + f"Shift {best_shift}: {decrypted_message}" + Style.RESET_ALL)
        else:
            print(f"Shift {shift}: {decrypted_message}")

    print("\nEl mensaje más probable en español es:", best_message)

if __name__ == "__main__":
    main()
