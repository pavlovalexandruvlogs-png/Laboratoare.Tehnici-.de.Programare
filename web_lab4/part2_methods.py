# Laborator: functii, metode si importuri pe web - Partea 2
# Student: Pavlov Alexandru-Lorenzo

import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 15  # secunde

# --- Exercitiul 9 ---
# Elemente de baza ale raspunsului
response = requests.get(BASE_URL,timeout=TIMEOUT)

print(response.status_code) # Atribuit care returneaza codul de stare HTTP
print(response.ok) # Atribuit care returneaza True daca status_code < 400
print(response.url) # Atribuit care returneaza URL-ul final al paginii
print(response.encoding) # Atribuit care returneaza codificarea textului

# --- Exercițiul 10 ---
# Tratarea erorilor cu o metodă
try:
  response.raise_for_status()

  response_invalid = requests.get(
      BASE_URL + "/this-page-does-not-exist", timeout=TIMEOUT
  )
  response_invalid.raise_for_status()

except requests.HTTPError as e:
  print(
      f"[Eroare prinsă cu succes]: Pagina solicitată a generat o eroare: {e}"
  )
  
  # --- Exercițiul 11 ---
# Trimiterea de anteturi (Headers) personalizate
headers_personalizate = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ro-RO,ro;q=0.9",
}
res_headers = requests.get(BASE_URL, headers=headers_personalizate, timeout=TIMEOUT)
print("Status cu antet personalizat:", res_headers.status_code)

# --- Exercițiul 12 ---
# Trimiterea de parametri în URL (Query Parameters) folosind un dicționar
params = {"search": "python", "page": 1}
# Folosim ECHO_URL (https://httpbin.org) pentru a vedea cum ajung parametrii pe server
res_params = requests.get(f"{ECHO_URL}/get", params=params, timeout=TIMEOUT)
print("URL-ul generat cu parametri:", res_params.url)

# --- Exercițiul 13 ---
# Inspectarea răspunsului sub formă de text brut
print("Primele 100 caractere text:", res_headers.text[:100])

# --- Exercițiul 14 ---
# Inspectarea răspunsului sub formă de biți (bytes)
print("Tipul datelor in bytes:", type(res_headers.content))

# --- Exercițiul 15 ---
# Parsarea răspunsului JSON folosind .json()
res_json = requests.get(f"{ECHO_URL}/json", timeout=TIMEOUT)
print("Titlul din JSON:", res_json.json().get("slideshow", {}).get("title"))

# --- Exercițiul 16 ---
# Verificarea istoricului de redirect-uri (.history)
res_redirect = requests.get(f"{ECHO_URL}/redirect/1", timeout=TIMEOUT)
print("Număr de redirect-uri:", len(res_redirect.history))
print("URL final după redirect:", res_redirect.url)

# --- Exercițiul 17 ---
# Dezactivarea redirect-urilor (allow_redirects=False)
res_no_redir = requests.get(f"{ECHO_URL}/redirect/1", allow_redirects=False, timeout=TIMEOUT)
print("Status fără redirect:", res_no_redir.status_code)

# --- Exercițiul 18 ---
# Stream-ul de date (streaming responses) pentru fișiere mari
res_stream = requests.get(f"{ECHO_URL}/stream/1", stream=True, timeout=TIMEOUT)
print("Status stream:", res_stream.status_code)

# --- Exercițiul 19 ---
# Timpul scurs de la cerere până la primirea răspunsului (elapsed)
print("Timp de răspuns (elapsed):", res_stream.elapsed.total_seconds(), "secunde")

# --- Exercițiul 20 ---
# Vizualizarea anteturilor primite de la server (response headers)
print("Antet Content-Type primit:", res_stream.headers.get("Content-Type"))