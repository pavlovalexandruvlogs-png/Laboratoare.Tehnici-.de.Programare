import re
import base64
import hashlib
from urllib.parse import unquote

# A1. Conversie Hex - Bytes
def a1_demo():
    b = b"Salut"
    hex_str = b.hex()
    refacut = bytes.fromhex(hex_str)
    return hex_str, refacut

# A2. Recunoasterea stratului
def ghici_strat(s: str) -> str:
    if "%" in s:
        return "url"
    if re.fullmatch(r"[0-9a-fA-F]+", s) and len(s) % 2 == 0:
        return "hex"
    if re.fullmatch(r"[A-Za-z0-9+/=]+", s):
        return "base64"
    return "necunoscut"

# A3. Desfacere stratului
def desfa(s: str):
    strat = ghici_strat(s)
    if strat == "base64":
        return strat, base64.b64decode(s)
    elif strat == "hex":
        return strat, bytes.fromhex(s)
    elif strat == "url":
        return strat, unquote(s).encode('utf-8')
    return strat, s.encode('utf-8')

# A4. Verificare daca un bufer de octeti este text citibil
def citibil(b: bytes) -> bool:
    return all(32 <= c <=126 for c in b)

def desfa_multiplu(val: str, max_incercari=8):
    for _ in range(max_incercari):
        strat, b = desfa(val)
        if citibil(b):
            print(f"Decodat cu succes ({strat}): {b.decode('utf-8')}")
            return b.decode('utf-8', errors='ignore')
    return val

# A5. Spargerea XOR (1 octet) 
def spargere_xor(cale_fisier="probe/xor.bin"):
    with open(cale_fisier, "rb") as f:
        data = f.read()  
        
    for k in range(256):
        clar = bytes(b ^ k for b in data)
        if citibil(clar):
            print(f"Cheie XOR gasita:{k} (0x{k:02x}) -> Text: {clar.decode('utf-8')}")
            return k, clar.decode('utf-8')
    return None, None

# A6. Spargere Hash-ului prin Dictionar
def sparge_hash(cale_hash="probe/hashuri.txt", cale_dict="probe/wordlist.txt"):
    with open(cale_hash, "r") as f:
        tinta = f.readline().strip()
        
    lungime = len(tinta)
    
    with open(cale_dict, "r", encoding="latin1") as f:
        for line in f:
            cuv = line.strip()
            if lungime == 32:
                h = hashlib.md5(cuv.encode()).hexdigest()
            elif lungime == 40:
                h = hashlib.sha1(cuv.encode()).hexdigest() 
            elif lungime == 64:
                h = hashlib.sha256(cuv.encode()).hexdigest() 
            else:
                continue
            
            if h == tinta:
                print(f"Parola gasita: {cuv}") 
                return cuv
    return None 

if __name__ == "__main__":
    import sys
    print("Modulul forensics a fost incarcat cu succes!")
    
    # 1. Testare Conversie Hex -> Bytes
    print("\n--- Test A1 ---")
    hex_str, refacut = a1_demo()
    print(f"Hex; {hex_str} | Refacut: {refacut}")
    
    # 2. Testare Identificare Strat
    print("\n--- Test A2 ---")
    print("Strat detectat:", ghici_strat("S2VsYW1hdA=="))
    
    # 3. Testare Decodare Strat
    print("\n--- Test A3 ---")
    strat, rez = desfa("S2VsYW1hdA==")
    print(f"Strat: {strat} | Rezultat: {rez}")
    
   # 4. Testare Decodare directa
   print("\n--- Test Decodare ---")
   strat, rez = desfa("U2FsdXQgZm9yZW5zaWNz")
   print(f"Strat detectat: {strat} | Rezultat: {rez}")
   
                     
            