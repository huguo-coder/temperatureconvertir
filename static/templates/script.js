async function controllacredenziali() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    if (!username || !password )
        return alert("Scrivi un nome e una password");
   const res = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `username=${username}&password=${password}`
    });

    const json = await res.json();

    if (json.messaggio == 1){
        document.getElementById("risultato").innerText = "Accesso effettuato";
    }
    else {
        document.getElementById("risultato").innerText = "Accesso negato";
    }
}

document.getElementById('bottone').addEventListener('click', controllacredenziali);