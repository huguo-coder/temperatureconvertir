from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# ======================
# LOGIN (GET)
# ======================
@app.get("/login", response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# ======================
# LOGIN (POST)
# ======================
@app.post("/login", response_class=HTMLResponse)
def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    
    if username == "alunno" and password == "1234":
        return templates.TemplateResponse("convertitore.html", {
            "request": request,
            "risultato": ""
        })
    
    return "<h3>Credenziali errate! <a href='/login'>Riprova</a></h3>"

# ======================
# PAGINA CONVERTITORE (GET)
# ======================
@app.get("/convertitore", response_class=HTMLResponse)
def conv_get(request: Request):
    return templates.TemplateResponse("convertitore.html", {
        "request": request,
        "risultato": ""
    })

# ======================
# CONVERSIONE (POST)
# ======================
@app.post("/convertitore", response_class=HTMLResponse)
def conv_post(
    request: Request,
    temp: float = Form(...),
    azione: str = Form(...)
):
    risultato = ""

    if azione == "f_to_c":
        res = (temp - 32) * 5 / 9
        risultato = f"{temp} °F = {res:.2f} °C"

    elif azione == "c_to_f":
        res = (temp * 9 / 5) + 32
        risultato = f"{temp} °C = {res:.2f} °F"

    return templates.TemplateResponse("convertitore.html", {
        "request": request,
        "risultato": risultato
    })