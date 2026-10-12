import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 30

print("=== PARTEA 4: AUTENTIFICARE ȘI CONȚINUT BINAR ===")

# --- Exercițiul 30 ---
# Autentificare de bază (Basic Auth)
try:
  res_auth = requests.get(
      f"{ECHO_URL}/basic-auth/user_utm/parola123",
      auth=("user_utm", "parola123"),
      timeout=TIMEOUT,
  )
  if res_auth.status_code == 200:
    print("Ex 30 - Autentificare reușită:", res_auth.json())
  else:
    print(f"Ex 30 - Autentificare eșuată, status: {res_auth.status_code}")
except requests.exceptions.Timeout:
  print("Ex 30 - Eroare: Timeout.")

# --- Exercițiul 31 ---
# Descărcarea unui fișier binar (ex: o imagine mică) și salvarea pe disc
try:
  res_img = requests.get(f"{ECHO_URL}/image/png", timeout=TIMEOUT)
  if res_img.status_code == 200:
    with open("imagine_test.png", "wb") as f:
      f.write(res_img.content)
    print("Ex 31 - Fișierul binar a fost descărcat și salvat ca 'imagine_test.png'")
  else:
    print(f"Ex 31 - Eroare la descărcare, status: {res_img.status_code}")
except requests.exceptions.Timeout:
  print("Ex 31 - Eroare: Timeout.")

# --- Exercițiul 32 ---
# Folosirea unui Proxy pentru cereri HTTP (opțional / demonstrativ)
print("Ex 32 - Configurare proxy pregătită pentru medii izolate.")

# --- Exercițiul 33 ---
# Verificarea codului de eroare HTTP ridicat automat (raise_for_status)
try:
  res_error = requests.get(f"{ECHO_URL}/status/404", timeout=TIMEOUT)
  res_error.raise_for_status()  # Va genera o excepție pentru coduri 4xx/5xx
except requests.exceptions.HTTPError as err:
  print(f"Ex 33 - Eroare HTTP detectată automat: {err}")
  
