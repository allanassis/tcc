# Correctness Evaluation — jQuery (README-Gen)

Project column value: `jquey` (matches package folder). Tool: README-Gen
(structured ATRAK-grounded prompting, `gpt-4.1-mini-2025-04-14`).
READMEs evaluated in order: `data1.md`, `data2.md`, `data3.md`.

## Execution Environment

- Isolated temp project: `/tmp/eval-jquery`, `npm init -y`.
- `npm install jquery jsdom` → **jquery@4.0.0**, **jsdom@29.1.1** (exit 0).
- Browser-only DOM snippets executed under Node with jsdom: jQuery source
  (`node_modules/jquery/dist/jquery.js`, v4.0.0) loaded into a jsdom `window`
  via `window.eval(jqSrc)`; `$ = window.jQuery`. Fresh DOM per snippet.
- `$(document)...` snippets re-executed inside `window.eval(...)` so that
  `document`/`$` are true globals (faithful to browser scope).
- CDN URLs validated with `curl -sI`.
- API existence validated by live introspection of the jsdom-loaded jQuery
  (`typeof $.fn.<m> === 'function'` / `typeof $.<m> === 'function'`).

## Cross-checked sources

1. Repository: https://github.com/jquery/jquery (shallow clone at `/tmp/jquery`).
   - `package.json`: `"name":"jquery"`, `"version":"4.0.0"`, `"license":"MIT"`,
     **no `engines` field**.
   - `LICENSE.txt`: MIT license text (OpenJS Foundation).
2. Installed artifact: `node_modules/jquery` v4.0.0 (ships prebuilt `dist/`).
3. Official API docs: https://api.jquery.com
   - `jQuery.trim()`: *deprecated 3.5, removed 4.0* (categories Deprecated /
     Removed / Utilities).
   - `jQuery.proxy()`: *deprecated 3.3* (use `Function.prototype.bind`).
4. CDN: `https://code.jquery.com/jquery-3.7.0.min.js` → HTTP 200;
   `https://code.jquery.com/jquery-3.6.0.min.js` → HTTP 200.

### API introspection result (jQuery 4.0.0, jsdom)

Instance (`$.fn`): ready, each, html, text, append, prepend, remove, on, off,
trigger, hide, show, fadeIn, fadeOut, slideUp, slideDown, addClass,
removeClass, hasClass, attr, css, animate, click, focus, blur, load → **all
present**.
Static (`$.`): ajax, get, post, getJSON, extend, each, proxy → **present**;
**trim → absent (removed in 4.0)**.

---

# README 1 — `data1.md`

### Project Title (T)
- V1 title matches repo name — "jQuery" = repo `jquery`. **1**
- V2 not a different project. **1**
- V3 no hallucinated terminology. **1**
- **T = 3/3 = 100**

### Overview (O)
Overview: "fast, small, feature-rich JavaScript library … DOM traversal and
manipulation, event handling, CSS animation, Ajax," plus concept bullets.
- V1 primary functionality correctly described. **1**
- V2 supported by repo (`src/ajax`, `src/event`, `src/effects`, `src/manipulation`). **1**
- V3 no unsupported features (DOM, events, ajax, effects, cross-browser all real). **1**
- V4 domain correct (client-side JS library). **1**
- V5 terminology matches repo. **1**
- **O = 5/5 = 100**

### Installation (I) — executed
Paths: CDN (3.7.0), `npm install jquery`, `import $ from 'jquery'`, download.
- V1 dependencies declared — jQuery has no runtime deps; self-contained. **1**
- V2 commands execute unmodified — `npm install jquery` exit 0; CDN 3.7.0 HTTP 200;
  `import $ from 'jquery'` returns the jQuery function (v4.0.0) under jsdom. **1**
- V3 no unresolved dependency errors (0 vulnerabilities). **1**
- V4 environment requirements correct — no false version/engine claims
  (repo declares no `engines`). **1**
- V5 expected artifact produced — npm package ships prebuilt
  `dist/jquery.js`; import yields usable `$`. **1**
- **I = 5/5 = 100**

### Usage and Examples (U) — executed (10 snippets)

| # | Snippet | Method | Result | E_i |
|---|---|---|---|---|
| 1 | `$('p').css('color','red')` | jsdom | `rgb(255,0,0)` | 1 |
| 2 | `$(document).ready(fn)` | jsdom (global eval) | bound, no throw | 1 |
| 3 | `$(function(){...})` | jsdom | bound | 1 |
| 4 | `$('<div>…</div>').appendTo('body')` | jsdom | body contains text | 1 |
| 5 | `$('#my-element').html('New content')` | jsdom | `New content` | 1 |
| 6 | `$('.old-class').remove()` | jsdom | length 0 | 1 |
| 7 | `$('#button').on('click',fn)` | jsdom | bound | 1 |
| 8 | `$('body').on('click','.dynamic-button',fn)` | jsdom (global eval) | bound | 1 |
| 9 | `$.getJSON(url,fn)` | jsdom | returns jqXHR object | 1 |
| 10 | `$.ajax({…POST…})` | jsdom | returns jqXHR object | 1 |

All imports/usage documented (CDN/npm include shown). No exceptions; behavior
matches text. **U = 10/10 = 100**

### API Reference (A) — 21 elements
Core: `$()`/`jQuery()`, `.ready(handler)`, `.each(callback)`. DOM: `.html`,
`.text`, `.append`, `.prepend`, `.remove`. Event: `.on`, `.off`, `.trigger`.
Ajax: `$.ajax`, `$.get`, `$.post`, `$.getJSON`. Effects: `.hide`, `.show`,
`.fadeIn`, `.fadeOut`, `.slideUp`, `.slideDown`.

All 21 exist (introspection = present), names/params/types/returns correct,
behavior consistent with execution, none deprecated/removed. **A = 21/21 = 100**

### License (L)
- V1 MIT matches repo LICENSE.txt (MIT). **1**
- V2 "MIT" valid identifier. **1**
- V3 no conflicting license info. **1**
- **L = 3/3 = 100**

**C_R(data1) = (100+100+100+100+100+100)/6 = 100.00**

---

# README 2 — `data2.md`

### Project Title (T) = 100 (jQuery; no hallucination).

### Overview (O)
Selectors, DOM manipulation, event handling, effects, Ajax, utilities — all
correct and supported; domain and terminology correct. **O = 5/5 = 100**

### Installation (I) — executed
Paths: CDN (3.6.0 → HTTP 200), download+host, `npm install jquery` (exit 0),
`import $ from 'jquery'` (works). No false env claims. Artifact shipped
prebuilt by npm package. **I = 5/5 = 100**

### Usage and Examples (U) — executed (15 snippets)

| # | Snippet | Result | E_i |
|---|---|---|---|
| 1 | `$('p').text('Hello, jQuery!')` | `Hello, jQuery!` | 1 |
| 2 | `$('.highlight').addClass('active')` | hasClass true | 1 |
| 3 | `$('#mylist').append('<li>…</li>')` | 1 li | 1 |
| 4 | `$('button').on('click',fn)` | bound | 1 |
| 5 | `$('button').click(fn)` | bound | 1 |
| 6 | `$(document).on('click','.dynamic-element',fn)` | bound (global eval) | 1 |
| 7 | `$('#box').hide(500)` | ok | 1 |
| 8 | `$('.fade-me').fadeIn()` | ok | 1 |
| 9 | `$('#myDiv').animate({width:'300px'},1000)` | ok | 1 |
| 10 | `$('#result').load('ajax/test.html')` | returns jQuery obj | 1 |
| 11 | `$.get(url,fn)` | jqXHR | 1 |
| 12 | `$.post(url,{name:'John'},fn)` | jqXHR | 1 |
| 13 | `$.ajax({…GET,dataType:json…})` | jqXHR | 1 |
| 14 | `$(document).ready(fn)` | bound (global eval) | 1 |
| 15 | `$(function(){...})` | bound | 1 |

**U = 15/15 = 100**

### API Reference (A) — 33 elements
Core `$()` (1); Manipulation `.addClass`, `.removeClass`, `.hasClass`, `.attr`,
`.css`, `.html`, `.text`, `.append`, `.prepend`, `.remove` (10); Events `.on`,
`.off`, `.click`, `.focus`, `.blur`, `.trigger` (6); Effects `.hide`, `.show`,
`.fadeIn`, `.fadeOut`, `.slideUp`, `.slideDown`, `.animate` (7); Ajax `$.ajax`,
`$.get`, `$.post`, `$.getJSON`, `.load` (5); Utility `$.extend`, `$.each`,
`$.proxy`, `$.trim` (4). Total **33**.

| Element | Exists | Notes | A_i |
|---|---|---|---|
| 31 elements above (excluding proxy, trim) | yes | present, correct signatures/returns, not deprecated (`.click/.focus/.blur` are valid, not deprecated in 4.0) | 1 each |
| `$.proxy(fn, context)` | yes (4.0) | **deprecated 3.3** — documented as a current utility (rule 6 fail) | 0 |
| `$.trim(str)` | **no (removed 4.0)** | deprecated 3.5, removed 4.0 — documented as current (rules 1 & 6 fail) | 0 |

**A = 31/33 = 93.94**

### License (L) = 100 (MIT matches; valid; no conflict).

**C_R(data2) = (100+100+100+100+93.94+100)/6 = 98.99**

---

# README 3 — `data3.md`

### Project Title (T) = 100.

### Overview (O)
Domain Concepts: DOM manipulation, event handling, AJAX, animation, selectors,
chaining — all correct/supported; domain + terminology correct. **O = 100**

### Installation (I) — executed
CDN 3.6.0 (HTTP 200), `npm install jquery` (exit 0), `import $ from 'jquery'`
(works), download. **I = 100**

### Usage and Examples (U) — executed (5 snippets)

| # | Snippet | Result | E_i |
|---|---|---|---|
| 1 | `$('p').css('color','blue')` | `rgb(0,0,255)` | 1 |
| 2 | `$('#myDiv').addClass('active').slideDown().html('Hello, jQuery!')` (chaining) | class set + html set | 1 |
| 3 | `$('#btn').on('click',fn)` | bound | 1 |
| 4 | `$.ajax({…GET,json…})` | jqXHR | 1 |
| 5 | `$('#myElement').fadeOut(1000)` | ok | 1 |

**U = 5/5 = 100**

### API Reference (A) — 8 elements
`$()` (selector, context), `.css(property, value)`, `.on(events, selector,
data, handler)`, `.ajax(settings)` (→ `$.ajax`, returns jqXHR), `.addClass`,
`.removeClass`, `.html()`, `.fadeOut(duration, complete)`. All exist,
signatures/returns correct, behavior consistent, none deprecated/removed.
**A = 8/8 = 100**

### License (L) = 100 (MIT matches; valid; no conflict).

**C_R(data3) = 100.00**

---

## Section-score summary & averages

| readme | T | O | I | U | A | L | C_R |
|---|---|---|---|---|---|---|---|
| data1.md | 100 | 100 | 100 | 100 | 100 | 100 | 100.00 |
| data2.md | 100 | 100 | 100 | 100 | 93.94 | 100 | 98.99 |
| data3.md | 100 | 100 | 100 | 100 | 100 | 100 | 100.00 |
| **average** | 100 | 100 | 100 | 100 | **97.98** | 100 | **99.66** |

Average checks: api = (100+93.94+100)/3 = 97.98; correctness =
(100+98.99+100)/3 = 99.66. Consistent with per-README rows.
