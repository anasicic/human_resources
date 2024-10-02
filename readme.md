# Human Resources

**Human Resources** je web aplikacija temeljena na MTV (Model-Template-View) arhitekturi, izrađena u Djangu. Aplikacija omogućava spremanje i pregled podataka o zaposlenicima.

## Sadržaj

- [Pokretanje servera](#pokretanje-servera)
- [Struktura aplikacije](#struktura-aplikacije)
- [Funkcionalnosti](#funkcionalnosti)
- [Tehnologije](#tehnologije)

---

## Pokretanje servera

Kako biste pokrenuli projekat lokalno, pratite sljedeće korake:

1. **Klonirajte repozitorij**:

    Ako projekt preuzimate sa GitHub-a, klonirajte repozitorij koristeći `git clone`:

    ```bash
    git clone https://github.com/anasicic/human_resources.git
    ```

2. **Idite u direktorij projekta**:

    Nakon što je projekt kloniran, uđite u direktorij projekta:

    ```bash
    cd human_resources
    ```

3. **Instalirajte potrebne pakete**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Stvorite migracijske datoteke za bazu podataka**:

    ```bash
    python manage.py makemigrations
    ```

5. **Izvršite migraciju kako biste primijenili promjene u bazi podataka**:

    ```bash
    python manage.py migrate
    ```

6. **Pokrenite razvojni server**:

    ```bash
    python manage.py runserver
    ```

7. **Otvorite preglednik i idite na**:

    ```url
    http://127.0.0.1:8000/
    ```

---

## Struktura aplikacije

Aplikacija se sastoji od dvije aplikacije: `employee` i `user`. Obje aplikacije koriste zajednički `base.html`, koji definira kostur svih stranica.

- **Baza podataka**: Aplikacija koristi SQLite za pohranu podataka.
- **Frontend**: Frontend je izrađen pomoću HTML, CSS i Bootstrap.

---

## Funkcionalnosti

### 1. Prijava korisnika

- Pri pokretanju aplikacije, korisnicima se prikazuje sučelje za prijavu (Login).
- Neregistrirani korisnici mogu se registrirati putem forme na linku "Register".
- **Funkcionalnost**: Korisnička autentifikacija (prijava, registracija, odjava).

### 2. Prikaz podataka o zaposlenicima

- Prikazuje osnovne podatke o zaposlenicima, uključujući ime, prezime, odjel i vrstu ugovora.
- Klikom na ime zaposlenika otvara se detaljan prikaz sa dodatnim informacijama.

### 3. Administratorske ovlasti

- Administrator može dodavati i brisati zaposlenike putem administracijskog panela.
- **Funkcionalnost**: Administratorske funkcije (dodavanje i brisanje zaposlenika).

### 4. Ažuriranje podataka o zaposlenicima

- Korisnici mogu ažurirati podatke zaposlenika putem forme, uz obavijest o uspjehu nakon promjena.

### 5. Dodavanje novog zaposlenika

- Korisnici mogu unositi nove zaposlenike putem forme na početnoj stranici.

### 6. Korisnički profil

- Korisnici mogu ažurirati svoje podatke putem stranice "Profile".

### 7. Odjava

- Korisnik se može odjaviti klikom na "Logout".

---

## Tehnologije

- **Django** - Web framework za backend
- **SQLite** - Baza podataka
- **HTML, CSS, Bootstrap** - Frontend tehnologije za izradu sučelja
