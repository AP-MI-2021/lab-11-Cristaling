# Laborator 11 - Săptămâna 11

În cadrul laboratorului 11, fiecare student va primi cerințele pentru al doilea examen parțial. Acesta valorează `30%` din media notelor pe laborator.

Va trebui să acceptați assignmentul și să încărcați rezolvarea în repository-ul creat astfel.

Pentru rezolvarea cerințelor se recomandă să parcurgeți cursurile, seminarele și laboratoarele de până acum. De asemenea, se recomandă să folosiți la test fișierele existente în acest repository (pentru care trebuie să adăugați teste și specificații), dar acest lucru nu este obligatoriu.

În timpul testului puteți folosi orice resurse, dar nu aveți voie să comunicați între voi sau cu terțe persoane și nici să accesați repository-urile de github ale colegilor voștri.

Să vă asigurați că puteți face share screen și că aveți webcam și microfon funcționale. Fără acestea este posibil să vă fie refuzat accesul la test.

Timpul de lucru va fi de: **1 oră și 30 minute**, care se poate prelungi cu `20` de minute dacă permit condițiile.

Programul se evaluează exact în forma în care este submis pe github la expirarea timpului de lucru.

Orice erori la pornirea programului înseamnă notarea testului cu 1.

Mai jos aveți un exemplu de subiect. Acesta NU este ce veți primi la examen, este doar un model.

--- 

Scrieți un program cu meniu de tip consolă. Programul va reține datele într-un fișier. Vor fi suportate următoarele funcționalități:
1. [1p] Adăugare localitate: id, nume (string nenul), tip (`sat`, `oraș`, `municipiu`).
2. [2p] Adăugare rută autocar: id, id_oraș_pornire, id_oraș_oprire (trebuie să existe și să fie distincte ca pereche), preț, dus-întors (`true` / `false`). 
3. [2p] Afișarea localităților ordonate crescător după numărul de rute dus-întors care pornesc din ele. Se va afișa și acest număr.
4. [2p] Afișarea tuturor rutelor care se opresc într-o localitate minicipiu. Se vor afișa și denumirile localităților între care e definită ruta.
5. [3p] Export JSON: se creează un fișier JSON cu un obiect în care cheile sunt numele localităților, iar valoarea unei chei `X` este o listă cu numele localităților în care ajung direct autocare care pornesc din `X`.  

    De exemplu, pentru localitățile `oradea, cluj-napoca, chinteni, arad` și rutele `oradea->cluj-napoca, oradea->chinteni, cluj-napoca->chinteni, chinteni->cluj-napoca, chinteni->arad`, un export valid ar fi:  

    ```
    {
         "oradea": ["cluj-napoca", "chinteni"],
         "chinteni": ["cluj-napoca", "arad"],
         "cluj-napoca": [“chinteni"],
         "arad": []
    }
    ```

Punctajul pe fiecare cerință se acordă astfel:
- 25% corectitudinea implementării.
- 25% arhitectură stratificată și interfață utilizator user friendly.
- 25% specificații scrise corect (unde se aplică) și denumiri sugestive.
- 25% teste relevante și scrise corect (unde se poate).
- studenții de la Matematică pot obține punctaj maxim fără să scrie teste (procentajul aferent se redistribuie la corectitudine), fără să rețină datele în fișiere și fără să folosească repository, dar dacă fac aceste lucruri pot obține `3` puncte bonus. Aceste bonusuri se acordă proporțional cu funcționalitățile rezolvate. 
- studenții de la Mate-info și Fizică-info pot obține `1` punct bonus dacă au maxim `3` warning-uri PEP 8 și `2` puncte bonus dacă nu au niciun warning PEP 8. Aceste bonusuri se acordă doar pentru punctaje inițiale `>= 7`.
- o cerință nefuncțională se notează cu `0`. 
- nereținerea datelor în fișiere de către studenții de la mate-info și fizică-info duce la o penalizare de `50%` din punctajul obținut conform baremului. 
- o implementare non-OOP duce la o penalizare de `50%` din punctajul obținut conform baremului.

