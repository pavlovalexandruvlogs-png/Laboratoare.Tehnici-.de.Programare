import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 30  # Mărim timeout-ul la 30 de secunde

print("=== PARTEA 3: METODE HTTP ȘI CORPUL CERERII ===")

# --- Exercițiul 21 ---
try:
  res_post = requests.post(f"{ECHO_URL}/post", timeout=TIMEOUT)
  print("Ex 21 - Status POST simplu:", res_post.status_code)
except requests.exceptions.Timeout:
  print("Ex 21 - Eroare: Timpul de așteptare a expirat (Timeout).")

# --- Exercițiul 22 ---
try:
  form_data = {"username": "student_utm", "proiect": "web_lab"}
  res_form = requests.post(f"{ECHO_URL}/post", data=form_data, timeout=TIMEOUT)
  
  if res_form.status_code == 200:
    print("Ex 22 - Date formular primite de server:", res_form.json().get("form"))
  else:
    print(f"Ex 22 - Serverul a returnat un status neașteptat: {res_form.status_code}")
    
except (requests.exceptions.Timeout, requests.exceptions.JSONDecodeError):
  print("Ex 22 - A apărut o eroare de timeout sau răspunsul nu este un JSON valid.")

# --- Exercițiul 23 și 24 ---
try:
  json_payload = {
      "student": "Pavlov Alexandru-Lorenzo",
      "laborator": 3,
      "status": "In Progress",
  }
  res_json_post = requests.post(
      f"{ECHO_URL}/post", json=json_payload, timeout=TIMEOUT
  )
  print(
      "Ex 23 - JSON recepționat de server:", res_json_post.json().get("json")
  )
  print(
      "Ex 24 - Header Content-Type trimis:",
      res_json_post.json().get("headers", {}).get("Content-Type"),
  )
except requests.exceptions.Timeout:
  print("Ex 23/24 - Eroare: Timpul de așteptare a expirat (Timeout).")

# --- Exercițiul 25 ---
try:
  update_data = {"id": 101, "titlu": "Capitol Nou"}
  res_put = requests.put(f"{ECHO_URL}/put", data=update_data, timeout=TIMEOUT)
  print("Ex 25 - Status PUT:", res_put.status_code)
except requests.exceptions.Timeout:
  print("Ex 25 - Eroare: Timpul de așteptare a expirat (Timeout).")
  
# --- Exercițiul 26 ---
try:
  res_delete = requests.delete(f"{ECHO_URL}/delete", timeout=TIMEOUT)
  print("Ex 26 - Status DELETE:", res_delete.status_code)
except requests.exceptions.Timeout:
  print("Ex 26 - Eroare: Timeout.")

# --- Exercițiul 27 ---
try:
  patch_data = {"status": "Completat parțial"}
  res_patch = requests.patch(
      f"{ECHO_URL}/patch", data=patch_data, timeout=TIMEOUT
  )
  print("Ex 27 - Status PATCH:", res_patch.status_code)
except requests.exceptions.Timeout:
  print("Ex 27 - Eroare: Timeout.")

# --- Exercițiul 28 ---
try:
  cookies_trimise = {"sesiune_id": "xyz123abc", "preferinta": "dark_mode"}
  res_cookies = requests.get(
      f"{ECHO_URL}/cookies", cookies=cookies_trimise, timeout=TIMEOUT
  )
  if res_cookies.status_code == 200:
    print(
        "Ex 28 - Cookie-uri primite de la server:",
        res_cookies.json().get("cookies"),
    )
  else:
    print(f"Ex 28 - Serverul a returnat statusul: {res_cookies.status_code}")
except (requests.exceptions.Timeout, requests.exceptions.JSONDecodeError):
  print("Ex 28 - Eroare la procesarea răspunsului.")

# --- Exercițiul 29 ---
try:
  sesiune = requests.Session()
  sesiune.cookies.set("user_login", "activ")
  res_sess = sesiune.get(f"{ECHO_URL}/cookies", timeout=TIMEOUT)
  if res_sess.status_code == 200:
    print("Ex 29 - Cookie din sesiune:", res_sess.json().get("cookies"))
  else:
    print(f"Ex 29 - Serverul a returnat statusul: {res_sess.status_code}")
except (requests.exceptions.Timeout, requests.exceptions.JSONDecodeError):
  print("Ex 29 - Eroare la procesarea răspunsului.")