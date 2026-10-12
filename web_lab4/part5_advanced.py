import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 30

print("=== PARTEA 5: SESIUNI AVANSATE ȘI MULTIPART UPLOAD ===")

# --- Exercițiul 34 ---
# Folosirea unei Sesiuni cu anteturi personalizate (Headers) globale
try:
  session = requests.Session()
  session.headers.update({
      "User-Agent": "UTM-Security-Lab/1.0",
      "X-Student": "Pavlov Alexandru-Lorenzo",
  })

  res_session = session.get(f"{ECHO_URL}/headers", timeout=TIMEOUT)
  if res_session.status_code == 200:
    print(
        "Ex 34 - Antet primit de server (User-Agent):",
        res_session.json().get("headers", {}).get("User-Agent"),
    )
  else:
    print(f"Ex 34 - Status neașteptat: {res_session.status_code}")
except (requests.exceptions.Timeout, requests.exceptions.JSONDecodeError):
  print("Ex 34 - Eroare la procesarea cererii.")

# --- Exercițiul 35 ---
# Încărcarea unui fișier binar folosind Multipart-FormData (files=...)
try:
  # Folosim fișierul imagine_test.png descărcat anterior la Ex 31
  with open("imagine_test.png", "rb") as f:
    files_payload = {"file": ("imagine_test.png", f, "image/png")}
    res_upload = requests.post(
        f"{ECHO_URL}/post", files=files_payload, timeout=TIMEOUT
    )

  if res_upload.status_code == 200:
    print(
        "Ex 35 - Fișier încărcat cu succes prin POST (files). Fișiere primite"
        " de server:",
        list(res_upload.json().get("files", {}).keys()),
    )
  else:
    print(f"Ex 35 - Eroare la upload, status: {res_upload.status_code}")
except (
    FileNotFoundError,
    requests.exceptions.Timeout,
    requests.exceptions.JSONDecodeError,
):
  print(
      "Ex 35 - Eroare: Fișierul nu a fost găsit sau a apărut o problemă de"
      " rețea."
  )

# --- Exercițiul 36 ---
# Controlul manual al redirect-urilor și inspectarea istoricului
try:
  res_history = requests.get(
      f"{ECHO_URL}/redirect/2", allow_redirects=True, timeout=TIMEOUT
  )
  print(f"Ex 36 - Număr total de redirect-uri urmate: {len(res_history.history)}")
  for resp in res_history.history:
    print(
        f"  -> Pas intermediar: URL: {resp.url} | Status: {resp.status_code}"
    )
  print(f"  -> URL final: {res_history.url}")
except requests.exceptions.Timeout:
  print("Ex 36 - Eroare: Timeout.")
  
print("=== PARTEA 5 (FINALĂ): PARAMETRI, FORMULARE ȘI VERIFICARE CONȚINUT ===")

# --- Exercițiul 37 ---
# Trimiterea de parametri URL compleți cu ajutorul dicționarului `params`
try:
  query_params = {
      "course": "Securitate Informatica",
      "group": "SI-266",
      "lab": "Python Requests",
  }
  res_params = requests.get(
      f"{ECHO_URL}/get", params=query_params, timeout=TIMEOUT
  )
  if res_params.status_code == 200:
    print("Ex 37 - Parametri URL trimiși cu succes. URL-ul construit de server:")
    print("  ->", res_params.json().get("url"))
  else:
    print(f"Ex 37 - Status neașteptat: {res_params.status_code}")
except requests.exceptions.Timeout:
  print("Ex 37 - Eroare: Timeout.")

# --- Exercițiul 38 ---
# Trimiterea datelor sub formă de formular (Form URL-Encoded) prin POST
try:
  form_data = {"username": "student_utm", "status": "active"}
  res_form = requests.post(f"{ECHO_URL}/post", data=form_data, timeout=TIMEOUT)
  if res_form.status_code == 200:
    print("Ex 38 - Date trimise ca form-encoded cu succes.")
    print("  -> Formular recepționat de server:", res_form.json().get("form"))
  else:
    print(f"Ex 38 - Status neașteptat: {res_form.status_code}")
except requests.exceptions.Timeout:
  print("Ex 38 - Eroare: Timeout.")

# --- Exercițiul 39 ---
# Verificarea tipului de conținut (Content-Type) din răspunsul serverului
try:
  res_type = requests.get(f"{ECHO_URL}/json", timeout=TIMEOUT)
  if res_type.status_code == 200:
    content_type = res_type.headers.get("Content-Type")
    print(f"Ex 39 - Content-Type detectat: {content_type}")
    if "application/json" in content_type:
      print("  -> Răspunsul este un JSON valid, putem folosi .json()")
  else:
    print(f"Ex 39 - Status neașteptat: {res_type.status_code}")
except requests.exceptions.Timeout:
  print("Ex 39 - Eroare: Timeout.")
  
