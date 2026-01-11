# Color Customization Guide

Ez a dokumentáció részletesen bemutatja, hogyan módosíthatod a blogod színeit a posztokban.

## 📍 Hol találhatók a színbeállítások?

### Fő színpaletta: `_layouts/post.html`

A posztok színeit CSS változókkal kezeljük, amelyek a `_layouts/post.html` fájl **33-52. sorában** vannak definiálva.

## 🎨 Színváltozók magyarázata

### Light Mode Színek (33-42. sor)

```css
:root {
  --bonsai-primary: #126863ff;      /* Fő szín - H1, H2 címek, kiemeléseknél */
  --bonsai-accent: #8b7355;         /* Kiegészítő szín - H3 címeknél */
  --bonsai-light: #f5f3f0;          /* Világos háttér - blockquote, callout */
  --bonsai-border: #e0ddd8;         /* Szegélyszín - elválasztók, keretek */
  --bonsai-text: #3a3a3a;           /* Főszöveg színe - bekezdések */
  --bonsai-text-muted: #6b6b6b;     /* Halványított szöveg - subtitle, meta, idézetek */
  --bonsai-shadow: rgba(0, 0, 0, 0.08); /* Árnyék */
}
```

### Dark Mode Színek (44-52. sor)

```css
[data-mode="dark"] {
  --bonsai-primary: #7fa85f;        /* Fő szín dark mode-ban */
  --bonsai-accent: #b89968;         /* Kiegészítő szín dark mode-ban */
  --bonsai-light: #1a1a1a;          /* Sötét háttér */
  --bonsai-border: #404040;         /* Szegélyszín dark mode-ban */
  --bonsai-text: #e9e8e8;           /* Főszöveg világos színe */
  --bonsai-text-muted: #a0a0a0;     /* Halványított szöveg világos */
  --bonsai-shadow: rgba(0, 0, 0, 0.3); /* Sötét árnyék */
}
```

## 🖌️ Elemek és színeik

### 1. Poszt címek (H1 - Title)
- **Fájl**: `_layouts/post.html` (128-135. sor)
- **Light mode**: `var(--bonsai-primary)` → `#126863ff`
- **Dark mode**: `var(--bonsai-primary)` → `#7fa85f`

```css
.bonsai-post-title {
  color: var(--bonsai-primary);
}
```

### 2. Subtitle (alcím)
- **Fájl**: `_layouts/post.html` (137-144. sor)
- **Szín**: `var(--bonsai-text-muted)`

```css
.bonsai-post-subtitle {
  color: var(--bonsai-text-muted);
}
```

### 3. Főszöveg (bekezdések)
- **Fájl**: `_layouts/post.html` (179-188. sor)
- **Szín**: `var(--bonsai-text)`

```css
.bonsai-content {
  color: var(--bonsai-text) !important;
}
```

### 4. H2 Címek
- **Fájl**: `_layouts/post.html` (199-207. sor)
- **Szín**: `var(--bonsai-primary)`

```css
.bonsai-content h2 {
  color: var(--bonsai-primary);
}
```

### 5. H3 Címek
- **Fájl**: `_layouts/post.html` (209-216. sor)
- **Light mode**: `var(--bonsai-accent)` → `#8b7355`
- **Dark mode**: `var(--bonsai-primary)` → `#7fa85f`

```css
.bonsai-content h3 {
  color: var(--bonsai-accent);
}

[data-mode="dark"] .bonsai-content h3 {
  color: var(--bonsai-primary);
}
```

### 6. H4 Címek
- **Fájl**: `_layouts/post.html` (218-225. sor)
- **Szín**: `var(--bonsai-text)`

```css
.bonsai-content h4 {
  color: var(--bonsai-text);
}
```

### 7. Blockquote (idézetek - `> sometext`)
- **Fájl**: `_layouts/post.html` (232-243. sor, 600-619. sor)
- **Light**: Szöveg `#6b6b6b`, Háttér `#f5f3f0`
- **Dark**: Szöveg `#a0a0a0`, Háttér `rgba(255,255,255,0.03)`

```css
.bonsai-content blockquote {
  color: var(--bonsai-text-muted);
  background: var(--bonsai-light);
}

[data-mode="dark"] .bonsai-content blockquote {
  color: #a0a0a0 !important;
  background: rgba(255, 255, 255, 0.03);
}
```

### 8. Lista elemek
- **Fájl**: `_layouts/post.html` (269-270. sor, 288-290. sor)
- **Bullet és számozás színe**: `var(--bonsai-primary)`

```css
.bonsai-content ul li::before {
  color: var(--bonsai-primary);
}

.bonsai-content ol li::before {
  color: var(--bonsai-primary);
}
```

## 🔧 Hogyan módosíts színeket?

### 1. Egyszerű módszer - CSS változók módosítása

1. Nyisd meg a `_layouts/post.html` fájlt
2. Menj a **33-52. sorokhoz**
3. Módosítsd a kívánt színkódokat
4. Mentsd el a fájlt
5. Restart Jekyll (`jekyll serve` újraindítása)
6. Frissítsd a böngészőt

### 2. Példa - Kék színsémára váltás

```css
:root {
  --bonsai-primary: #1e3a8a;      /* Sötétkék */
  --bonsai-accent: #3b82f6;       /* Világoskék */
  --bonsai-light: #eff6ff;        /* Halvány kék háttér */
  --bonsai-border: #bfdbfe;       /* Kék szegély */
  --bonsai-text: #1f2937;         /* Sötétszürke szöveg */
  --bonsai-text-muted: #6b7280;   /* Halványabb szürke */
  --bonsai-shadow: rgba(30, 58, 138, 0.08);
}

[data-mode="dark"] {
  --bonsai-primary: #60a5fa;      /* Világoskék */
  --bonsai-accent: #93c5fd;       /* Még világosabb kék */
  --bonsai-light: #1e293b;        /* Sötétkék háttér */
  --bonsai-border: #334155;       /* Szürkéskék szegély */
  --bonsai-text: #e5e7eb;         /* Fehéres szöveg */
  --bonsai-text-muted: #9ca3af;   /* Szürke */
  --bonsai-shadow: rgba(96, 165, 250, 0.3);
}
```

### 3. Példa - Meleg színsémára váltás

```css
:root {
  --bonsai-primary: #b45309;      /* Narancsbarna */
  --bonsai-accent: #f59e0b;       /* Arany */
  --bonsai-light: #fef3c7;        /* Krémszín */
  --bonsai-border: #fde68a;       /* Arany szegély */
  --bonsai-text: #292524;         /* Barna szöveg */
  --bonsai-text-muted: #78716c;   /* Halvány barna */
  --bonsai-shadow: rgba(180, 83, 9, 0.08);
}

[data-mode="dark"] {
  --bonsai-primary: #fbbf24;      /* Világos arany */
  --bonsai-accent: #fcd34d;       /* Sárga */
  --bonsai-light: #292524;        /* Sötétbarna háttér */
  --bonsai-border: #44403c;       /* Barna szegély */
  --bonsai-text: #fafaf9;         /* Fehéres */
  --bonsai-text-muted: #d6d3d1;   /* Halvány fehér */
  --bonsai-shadow: rgba(251, 191, 36, 0.3);
}
```

## 📚 További globális színbeállítások

### Globális dark mode szövegszínek
- **Fájl**: `_includes/custom-styles.html` (20-76. sor)
- Ezek a szabályok minden oldalra érvényesek (home, category, tags, stb.)

```css
[data-mode="dark"] body,
[data-mode="dark"] p,
[data-mode="dark"] li {
  color: #e9e8e8 !important;
}
```

## 💡 Tippek

1. **Használj színpalettagenerátort**: [coolors.co](https://coolors.co) vagy [color.adobe.com](https://color.adobe.com)
2. **Teszteld mindkét módban**: Mindig nézd meg light és dark mode-ban is
3. **Kontrasztarány**: Használj legalább 4.5:1 arányú kontrasztot olvashatóságért
4. **Változók előnye**: Csak 4-5 helyen kell módosítani, az egész blog megváltozik

## 🔍 Hibaelhárítás

**Ha nem látod a változásokat:**
1. Hard refresh (`Ctrl+Shift+R` vagy `Cmd+Shift+R`)
2. Töröld a böngésző cache-ét
3. Restart Jekyll server
4. Ellenőrizd, hogy a színkódok helyesek-e (# karakter kell elé)

---

**Utolsó frissítés**: 2026-01-11
**Készítette**: Claude Sonnet 4.5 & j1m
