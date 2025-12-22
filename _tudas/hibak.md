---
layout: page
title: Gyakori hibák és következmények
---

Tanuljunk a hibákból! Itt gyűjtöm össze a leggyakoribb gondozási hibákat és azok következményeit.

<style>
/* Évszak szekció stílus */
.season-section {
  margin: 3rem 0;
  animation: fadeInUp 0.6s ease;
}

.season-header {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-primary, #1f2937);
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 3px solid #22c55e;
}

/* Táblázat konténer */
.error-table-container {
  overflow-x: auto;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  background: var(--card-bg, #ffffff);
  animation: fadeInUp 0.7s ease;
}

/* Táblázat alap stílus */
.error-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  font-size: 1rem;
}

/* Fejléc stílus */
.error-table thead {
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
  color: white;
}

.error-table thead th {
  padding: 1.25rem 1.5rem;
  text-align: left;
  font-weight: 600;
  font-size: 1.1rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.error-table thead th:first-child {
  border-top-left-radius: 12px;
}

.error-table thead th:last-child {
  border-top-right-radius: 12px;
}

/* Sor stílus */
.error-table tbody tr {
  transition: all 0.3s ease;
  border-bottom: 1px solid var(--border-color, #e5e7eb);
}

.error-table tbody tr:hover {
  background: linear-gradient(90deg, rgba(34, 197, 94, 0.05) 0%, rgba(34, 197, 94, 0.02) 100%);
  transform: scale(1.01);
  box-shadow: 0 4px 12px rgba(34, 197, 94, 0.1);
}

.error-table tbody tr:last-child {
  border-bottom: none;
}

/* Cella stílus */
.error-table tbody td {
  padding: 1.25rem 1.5rem;
  color: var(--text-primary, #1f2937);
  line-height: 1.6;
}

/* Hiba oszlop (piros hangsúly) */
.error-table tbody td:first-child {
  font-weight: 600;
  color: #dc2626;
  position: relative;
  padding-left: 2rem;
}

.error-table tbody td:first-child::before {
  content: "⚠️";
  position: absolute;
  left: 0.75rem;
  font-size: 1.2rem;
}

/* Következmény oszlop (narancssárga hangsúly) */
.error-table tbody td:nth-child(2) {
  color: #ea580c;
  font-weight: 500;
}

/* Javítás oszlop (zöld hangsúly) */
.error-table tbody td:last-child {
  color: #16a34a;
  font-weight: 600;
  position: relative;
  padding-left: 2rem;
}

.error-table tbody td:last-child::before {
  content: "✓";
  position: absolute;
  left: 0.75rem;
  font-size: 1.2rem;
  color: #22c55e;
}

/* Animációk */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Reszponzív design */
@media (max-width: 768px) {
  .error-table {
    font-size: 0.9rem;
  }

  .error-table thead th,
  .error-table tbody td {
    padding: 1rem;
  }

  .season-header {
    font-size: 1.5rem;
  }
}

/* Megjegyzés box stílus */
.note-box {
  background: linear-gradient(135deg, #fef3c7 0%, #fef9e7 100%);
  border-left: 4px solid #f59e0b;
  padding: 1.25rem 1.5rem;
  border-radius: 8px;
  margin: 2rem 0;
  animation: fadeInUp 0.8s ease;
}

.note-box strong {
  color: #b45309;
  display: block;
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.note-box p {
  margin: 0;
  color: #78350f;
  line-height: 1.6;
}
</style>

## 🌱 Tavasz

<div class="error-table-container">
  <table class="error-table">
    <thead>
      <tr>
        <th>🚫 Hiba</th>
        <th>💔 Következmény</th>
        <th>🩹 Javítás</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Túl korai átültetés (fagyveszély)</td>
        <td>Gyökérsérülés, lassú indulás</td>
        <td>Várakozás április végéig</td>
      </tr>
      <tr>
        <td>Túl erős metszés</td>
        <td>Visszaszáradás, gyenge növekedés</td>
        <td>Türelem, regeneráció 1 év</td>
      </tr>
      <tr>
        <td>Tápanyaghiány</td>
        <td>Sárguló levelek, gyenge hajtások</td>
        <td>Bonsai tápoldattal öntözés 2 hetente</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="note-box">
  <strong>💡 Jó tanács:</strong>
  <p>Tavasszal mindig várjuk meg, amíg az éjszakai hőmérséklet tartósan 5°C fölé emelkedik, mielőtt nagyobb beavatkozásokat végzünk.</p>
</div>

---

## ☀️ Nyár

<div class="error-table-container">
  <table class="error-table">
    <thead>
      <tr>
        <th>🚫 Hiba</th>
        <th>💔 Következmény</th>
        <th>🩹 Javítás</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Túl erős metszés</td>
        <td>Visszaszáradás, stressz</td>
        <td>Türelem, árnyékolás, 1 év regeneráció</td>
      </tr>
      <tr>
        <td>Nyári átültetés</td>
        <td>Súlyos levélhullás, sokk</td>
        <td>Árnyék, gyakori permetezés, türelem 1 év</td>
      </tr>
      <tr>
        <td>Elégtelen öntözés (kiszáradás)</td>
        <td>Levélperzselődés, ágak elhalása</td>
        <td>Fokozatos vízpótlás, soha ne árasztás</td>
      </tr>
      <tr>
        <td>Túlöntözés (pangó víz)</td>
        <td>Gyökérrothadás, levélfoltok</td>
        <td>Jó drénázs biztosítása, ritkább öntözés</td>
      </tr>
      <tr>
        <td>Délutáni öntözés (forró levélen)</td>
        <td>Napégés, levélfoltok</td>
        <td>Csak reggel vagy este öntözzünk</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="note-box">
  <strong>💡 Jó tanács:</strong>
  <p>Nyáron a japán juharok különösen érzékenyek. A déli tűző nap ellen használjunk árnyékoló hálót (50-70%), és soha ne metszünk erősen!</p>
</div>

---

## 🍂 Ősz

<div class="error-table-container">
  <table class="error-table">
    <thead>
      <tr>
        <th>🚫 Hiba</th>
        <th>💔 Következmény</th>
        <th>🩹 Javítás</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Túl későn beszüntetett trágyázás</td>
        <td>Nem érik be a hajtások, fagykár</td>
        <td>Augusztus végétől ne trágyázzunk</td>
      </tr>
      <tr>
        <td>Túl korai téli elhelyezés</td>
        <td>Korai rügyduzzadás tavasszal</td>
        <td>Csak tartós 0°C alatti hőnél be</td>
      </tr>
      <tr>
        <td>Levélhullás előtti átültetés</td>
        <td>Gyökérsérülés, lassú regeneráció</td>
        <td>Tavaszig várakozás</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="note-box">
  <strong>💡 Jó tanács:</strong>
  <p>Az ősz a pihenés időszaka. Hagyjuk a fát természetes módon felkészülni a télre: ne metszünk, ne trágyázunk szeptember után.</p>
</div>

---

## ❄️ Tél

<div class="error-table-container">
  <table class="error-table">
    <thead>
      <tr>
        <th>🚫 Hiba</th>
        <th>💔 Következmény</th>
        <th>🩹 Javítás</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Fűtetlen helyiségben tartás</td>
        <td>Kiszáradás, ágvégsérülés</td>
        <td>Szellőztetett, de fagymentes hely</td>
      </tr>
      <tr>
        <td>Túl meleg téli elhelyezés</td>
        <td>Korai rügyfakadás</td>
        <td>Hűvös hely (0-5°C ideális)</td>
      </tr>
      <tr>
        <td>Elégtelen téli öntözés</td>
        <td>Gyökér kiszáradása</td>
        <td>Havi 1-2x öntözés, ellenőrizni a földet</td>
      </tr>
      <tr>
        <td>Téli metszés túl korán</td>
        <td>Fagykár a friss sebeknél</td>
        <td>Február vége / március eleje a legjobb</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="note-box">
  <strong>💡 Jó tanács:</strong>
  <p>A téli pihenőidőszak kritikus. A japán juharoknak szükségük van a hidegre (0-5°C), de védjük őket az erős fagytól és a kiszáradástól!</p>
</div>
