# Piano di Implementazione — Email Automation DECĒIT

**Data:** 4 Maggio 2026  
**Contesto:** Brand streetwear italiano, Shopify, 0-50 iscritti, 0-5 vendite/mese  
**Stack scelto:** Shopify Flow (gratis) + Shopify Messaging (gratis, 10.000 email/mese)  
**Abandoned cart:** Già attivo nativamente su Shopify  
**Obiettivo primario:** Evento Cosmico (10 Maggio) → prime vendite ricorrenti

---

## FASE 1: 📅 Automazione Post-Evento Cosmico (4-10 Maggio)

### Obiettivo
Convertire i partecipanti all'evento del 10 maggio in clienti — follow-up automatici che portano al DECĒIT Store.

### 1A — Tagging automatico in Shopify Flow

**Trigger:** Quando un customer viene creato con tag `evento-cosmico`

Crea un Flow in **Shopify Admin → Settings → Flow**:

```
TRIGGER: Customer created
  CONDITION: Tags contains "evento-cosmico"
  ACTION: Add customer tag "cosmico-maggio-2026"
  ACTION: Add to marketing list "Evento Cosmico 10 Maggio"
```

### 1B — Sequenza email automatica (via Shopify Flow + Shopify Messaging)

Crea 3 email template in **Marketing → Email templates**:

#### 📧 Email 1 — "Grazie + prossimi passi"
*Inviata: 1 ora dopo l'iscrizione*

| Elemento | Contenuto |
|----------|-----------|
| **Oggetto** | "Grazie per esserci stato ✦ DECĒIT × COSMICO" |
| **Testo** | Ringraziamento partecipazione + foto evento + "La tua Tee Cosmico sarà disponibile al DECĒIT Store a breve" |
| **CTA** | "SCOPRI LA COLLEZIONE" → /collections/ss26 |
| **Vibes** | Calda, autentica, foto dell'evento |

```
Flow trigger:
  TRIGGER: Customer tagged "evento-cosmico"
  WAIT: 1 hour
  ACTION: Send email template "Cosmico - Grazie"
```

#### 📧 Email 2 — "La tua Tee è pronta" (disponibilità capo)
*Inviata: quando la Tee Cosmico è effettivamente disponibile (da attivare manualmente dal team)*

| Elemento | Contenuto |
|----------|-----------|
| **Oggetto** | "La tua Tee Cosmico ti aspetta in negozio ✦ DECĒIT" |
| **Testo** | "La tua t-shirt è pronta! Vieni a ritirarla al DECĒIT Store — via Abbrescia 42, Bari. Porta con te la conferma." |
| **CTA** | "VEDI MAPPA / VENGO AL NEGOZIO" |
| **Extra** | Orari negozio + foto della tee finita |

```
Flow trigger:
  TRIGGER: Customer tagged "cosmico-maggio-2026"
  WAIT: Until manually triggered (or set specific date)
  ACTION: Send email template "Cosmico - Tee Pronta"
```

#### 📧 Email 3 — "Non perderti le novità" (7 giorni dopo il ritiro)
*Inviata: 7 giorni dopo la notifica di disponibilità*

| Elemento | Contenuto |
|----------|-----------|
| **Oggetto** | "[Nome], hai già visto la nuova collezione?" |
| **Testo** | "Chi ha partecipato a Cosmico merita un trattamento speciale. Ecco un 10% sul tuo prossimo ordine." |
| **CTA** | "SFOGLIA LA COLLEZIONE" → /collections/ss26 |
| **Offerta** | Codice sconto 10% valido 30 giorni (personalizzato o generico tipo COSMICO10) |

```
Flow trigger:
  TRIGGER: Customer tagged "cosmico-maggio-2026"
  WAIT: 7 days after "Tee Pronta" email sent
  ACTION: Send email template "Cosmico - Sconto Fedeltà"
```

### 1C — Canale WhatsApp (già attivo)

Il canale WhatsApp è già stato configurato nella pagina di conferma cosmico. 
- Assicurati di pubblicare contenuti REGOLARMENTE dopo l'evento (minimo 2-3 volte a settimana)
- Contenuti: foto evento, disponibilità tee, nuove collezioni

---

## FASE 2: 🚀 Welcome Series — Automazione Permanente (11-18 Maggio)

### Obiettivo
Ogni nuovo iscritto alla newsletter riceve una sequenza automatica che lo porta all'acquisto.

### 2A — Shopify Flow: Nuovo iscritto newsletter

```
TRIGGER: Customer added to marketing list
  CONDITION: Email marketing status = "subscribed"
  ACTION: Add customer tag "newsletter-welcome"
```

### 2B — Sequenza Welcome (4 email via Flow + Messaging)

#### 📧 Email 1 — "Benvenuto + sconto" (immediata)
*Oggetto:* "Benvenuto in DECĒIT — ecco il tuo 10%"  
*Contenuto:* 
- Ciao [Nome],
- Grazie per esserti iscritto. DECĒIT è dailywear per chi lotta con la verità.
- Usa il codice **WELCOME10** per il 10% sul tuo primo ordine.
- [Bottone: "SCOPRI LA COLLEZIONE"]
- I capi forti: Struggle Denim Longshirt, Stuck in a Loop Sweatshirt

#### 📧 Email 2 — "Chi siamo" (2 giorni dopo)
*Oggetto:* "DECĒIT non è solo un brand"  
*Contenuto:*
- Breve brand story: fondato 2022, Sud Italia, artisti, illustratori, designer
- "Dailywear for people who struggle with the truth" — cosa significa
- Foto del team/lookbook
- [Bottone: "LEGGI LA NOSTRA STORIA"]

#### 📧 Email 3 — "I bestseller" (4 giorni dopo)
*Oggetto:* "I capi che tutti vogliono"  
*Contenuto:*
- 2-3 prodotti bestseller con foto
- Perché funzionano: design, vestibilità, qualità
- Recensioni/social proof
- [Bottone: "SHOP NOW"]

#### 📧 Email 4 — "Ultimo avviso" (7 giorni dopo)
*Oggetto:* "Il tuo 10% sta per scadere"  
*Contenuto:*
- Urgenza sul codice sconto
- Cosa potresti aver perso
- Spedizione gratuita sopra €90
- 30 giorni per reso
- [Bottone: "ACQUISTA ORA"]

### 2C — Configurazione Flow per Welcome

```
# Flow 1: Welcome Email 1
TRIGGER: Customer tagged "newsletter-welcome"
  ACTION: Send email "Welcome - Benvenuto + Sconto"

# Flow 2: Welcome Email 2 (branch condizionale)
TRIGGER: Customer tagged "newsletter-welcome"
  WAIT: 2 days
  CONDITION: Customer has NOT placed an order in last 48 hours
    → YES: Send email "Welcome - Chi Siamo"
    → NO: Exit (non serve più la welcome, hanno già comprato)

# Flow 3: Welcome Email 3
TRIGGER: Customer tagged "newsletter-welcome"
  WAIT: 4 days
  CONDITION: Customer has NOT placed an order in last 4 days
    → YES: Send email "Welcome - Bestseller"
    → NO: Exit

# Flow 4: Welcome Email 4
TRIGGER: Customer tagged "newsletter-welcome"
  WAIT: 7 days
  CONDITION: Customer has NOT placed an order
    → YES: Send email "Welcome - Ultimo Avviso"
    → NO: Exit
```

---

## FASE 3: 🛒 Ottimizzare Abandoned Cart + Post-Purchase (19-25 Maggio)

### 3A — Abandoned Cart (già attivo, da ottimizzare)

Shopify ha già l'abandoned cart nativo. Verifica sia configurato:

**Settings → Checkout → Abandoned checkouts:**
- ✅ Abilita automatic email
- Timing: 1 ora dopo abbandono (ideal: 30-60 minuti per fashion)
- Oggetto: "[Nome], hai lasciato qualcosa nel carrello"
- Contenuto: mostra i prodotti nel carrello, CTA "COMPLETA ORDINE"
- **Non offrire sconti** in questa email — addestra i clienti ad abbandonare apposta

**Opzione avanzata con Flow (se vuoi 2 email):**

```
TRIGGER: Abandoned checkout created
  WAIT: 24 hours
  CONDITION: Checkout has NOT been recovered
    → YES: Send email "Ancora interessato? I tuoi capi ti aspettano"
    → (offri free shipping come incentivo)
```

### 3B — Post-Purchase Flow (4 email)

#### 📧 Email 1 — "Grazie dell'ordine" (immediata)
*Oggetto:* "Grazie [Nome], il tuo ordine è confermato ✦ DECĒIT"  
*Contenuto:* Dettagli ordine, tracking (se disponibile), "indossa con orgoglio"

#### 📧 Email 2 — "Come ti trovi?" (3 giorni dopo consegna)
*Oggetto:* "Come ti sta il [Prodotto]?"  
*Contenuto:* 
- Richiesta recensione/feedback
- Cura del capo (istruzioni lavaggio specifiche)
- [Bottone: "LASCIA UNA RECENSIONE"]

#### 📧 Email 3 — "Anche questo ti potrebbe piacere" (14 giorni dopo)
*Oggetto:* "Chi ha comprato [Prodotto] ha visto anche..."  
*Contenuto:*
- Cross-sell: capi che completano l'outfit
- Esempio: se ha comprato una tee, proponi la shirt o il sweatshirt coordinato
- [Bottone: "SCOPRI"]

#### 📧 Email 4 — "Bentornato" (30 giorni dopo)
*Oggetto:* "[Nome], bentornato in DECĒIT"  
*Contenuto:*
- Novità dalla nuova collezione
- 10% sul prossimo ordine (fedeltà)
- [Bottone: "SHOP NEW ARRIVALS"]

```
Flow: Post-Purchase
TRIGGER: Order fulfilled
  WAIT: 3 days
  ACTION: Send email "Post-Purchase - Feedback"
  
  WAIT: 14 days (da fulfilled)
  ACTION: Send email "Post-Purchase - Cross-sell"
  
  WAIT: 30 days (da fulfilled)
  CONDITION: Customer has NOT placed new order
    → YES: Send email "Post-Purchase - Bentornato + Sconto"
```

---

## FASE 4: 📋 Cattura Email sul Sito (Maggio)

### 4A — Ottimizzare newsletter esistente

La homepage ha già un form newsletter funzionante. Due miglioramenti rapidi:

1. **Aggiungi popup exit-intent** — quando l'utente sta per lasciare il sito, mostra un popup:
   - "Aspetta! 10% sul tuo primo ordine"
   - Solo campo email (non chiedere nome — cala conversioni del 30%)
   - Design coerente con brand (colori #17453C, #F5CDBE)

2. **Aggiungi form newsletter nel footer di TUTTE le pagine** (verifica sia già presente nel tema Dawn)

### 4B — Popup semplice (via tema Shopify o app gratuita)

Se il tema Dawn non ha popup nativo, usa **Shopify Email** o un'app gratuita:
- **Privy** (free tier: fino a 100 iscritti)
- **Justuno** (free tier base)
- Oppure aggiungi manualmente un piccolo script nel tema (soluzione più pulita)

---

## FASE 5: 📊 Segmentazione e Scalabilità (Giugno+)

### 5A — Tag System in Shopify

Organizza i customer con tag automatici tramite Flow:

| Tag | Trigger | Scopo |
|-----|---------|-------|
| `newsletter-welcome` | Nuovo iscritto marketing list | Welcome series |
| `evento-cosmico` | Iscrizione evento cosmico | Follow-up evento |
| `cosmico-maggio-2026` | Sotto-tag evento | Segmentazione evento |
| `first-purchase` | Primo ordine completato | Post-purchase + win-back |
| `repeat-customer` | Secondo ordine | Fedeltà/VIP |
| `high-value` | Ordine > €150 | Offerte premium |
| `inactive-60d` | Nessun ordine da 60 giorni | Win-back campaign |

### 5B — Win-Back (Giugno)

Per clienti che non hanno più comprato da 60+ giorni:

```
TRIGGER: Customer tagged "inactive-60d"
  WAIT: Trigger when tag added
  ACTION: Send email "Ci manchi — 15% per tornare da noi"
  
  WAIT: 7 days (if no purchase)
  ACTION: Send email "Ultima occasione — il tuo sconto scade tra 3 giorni"
```

### 5C — Quando passare a Klaviyo/Omnisend

**Passa quando**:
- Lista > 500 contatti (limite Mailchimp free)
- Email genera > 5 vendite/mese
- Vuoi SMS automation (fondamentale per fashion, 98% open rate)
- Il ROI delle email giustifica €20-30/mese di tool

**A quel punto:**
- Omnisend (~€16/mese a 500 contatti) — miglior rapporto qualità/prezzo, SMS incluso
- Klaviyo (~€20/mese) — best-in-class per DTC, predictive analytics

---

## ROADMAP RIEPILOGATIVA

| Settimana | Cosa fare | Tool |
|-----------|-----------|------|
| **4-9 Maggio** | Crea i Flow e template email Cosmico | Shopify Flow + Messaging |
| **10 Maggio** | 🎉 Evento Cosmico — raccogli iscrizioni | Pagina live / QR code |
| **11-18 Maggio** | Crea Welcome Series (4 email) | Shopify Flow + Messaging |
| **19-25 Maggio** | Ottimizza Abandoned Cart + Post-Purchase | Shopify flow |
| **26-31 Maggio** | Popup cattura email + ottimizzazioni | Tema + Flow |
| **Giugno** | Segmentazione, Win-Back, review risultati | Flow Analytics |

---

## KPI DA MONITORARE

| Metric | Target 30 giorni | Target 90 giorni |
|--------|-----------------|------------------|
| Iscritti newsletter | +50 | +200 |
| Welcome conversion | 5-10% | 8-12% |
| Abandoned cart recovery | 5-8% | 8-15% |
| Email revenue share | 5-10% | 15-25% |
| Vendite totali/mese | 5-15 | 20-50 |

---

## PROSSIMI PASSI IMMEDIATI (FATTI OGGI)

1. ✅ **Verifica Shopify Flow sia attivo** — Settings → Apps → Flow
2. ✅ **Verifica Shopify Email (Messaging) sia attivo** — Marketing → Email templates
3. ✅ **Verifica Abandoned Cart sia attivo** — Settings → Checkout
4. **Crea i 3 flow per Evento Cosmico** (sopra, Fase 1)
5. **Crea i 4 template email per Welcome** (sopra, Fase 2)
6. **Prepara il QR code** per la pagina /cosmico (già in fustella)
7. **Pubblica contenuti sul canale WhatsApp** prima e dopo l'evento

---

*Piano generato il 4 Maggio 2026 — Sisyphus AI*
