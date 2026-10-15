import base64

if __name__ == "__main__":
    print("--- Laborator 5: Testare Rulare --- ")
    test_str = "U2FsdXQgZm9yZWzaWNz"
    decodat = base64.b64decode(test_str).decode('utf-8')
    print("Rezultat decodat:", decodat)