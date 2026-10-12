# Student: Pavlov Alexandru-Lorenzo

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10 

import requests
print(requests.__version__)

# ---Exercitiul 2 ---
response = requests.get(BASE_URL, timeout=TIMEOUT)
print(response.status_code)

from requests import get
response = get(BASE_URL, timeout=TIMEOUT)
print(response.status_code)

# Avantaj import requests: se vede clar de unde vine functia (requests.get).
# Avantaj from requests import get: codul e mai scurt, scrii doar get().

# ---Exercitiul 3 ---
import requests as rq
response = rq.get(BASE_URL, timeout=TIMEOUT)
print(response.status_code)

# Alias-ul ajuta cand numele e lung (de exemplu import pandas as pd).
# Alias-ul incurca cand e ales ciudat (rq), pentru ca altii nu il recunosc usor.

# ---Exercitiul 4 ---
import urllib.request

# Adaugam User-Agent pentru a evita eroarea 403 Forbidden

req = urllib.request.Request(BASE_URL, headers={"User-Agent": "Mozilla/5.0"})

with urllib.request.urlopen(req, timeout=TIMEOUT) as raspuns:
    print(raspuns.status)
    corp = raspuns.read().decode("utf-8")
    print(corp[:200])
    
# --- Exercițiul 5 ---
print(dir(requests))
# Nume alese din rezultat:
# 1. requests.get este o funcție
# 2. requests.Response este o clasă
# 3. requests.exceptions este un modul

# --- Exercițiul 6 ---
help(requests.get)
# Parametrul care setează timpul maxim de așteptare este 'timeout'.
response_timeout = requests.get(BASE_URL, timeout=TIMEOUT)

# --- Exercițiul 7 ---
import time

start_time = time.perf_counter()
res_perf = requests.get(BASE_URL, timeout=TIMEOUT)
end_time = time.perf_counter()

durata_masurata = end_time - start_time
print(f"Măsurat cu time.perf_counter(): {durata_masurata:.4f} secunde")
print(
    f"Măsurat de requests (elapsed): {res_perf.elapsed.total_seconds():.4f}"
    " secunde"
)
# Comentariu: perf_counter măsoară timpul total (inclusiv procesarea Python și rețeaua locală),
# în timp ce response.elapsed măsoară doar timpul scurs de la trimiterea cererii până la primirea antetelor de la server.

# --- Exercițiul 8 ---
try:
  import bs4
except ImportError:
  print("Instalați modulul cu: pip install beautifulsoup4")    
