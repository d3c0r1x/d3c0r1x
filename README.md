# d3c0r1x — AI-first product builder / vibe coder

![](https://komarev.com/ghpvc/?username=d3c0r1x&color=58a6ff&style=flat-square&label=profile+views)
[![Portfolio](https://img.shields.io/badge/portfolio-d3c0r1x.github.io-58a6ff?style=flat-square)](https://d3c0r1x.github.io)
[![Resume](https://img.shields.io/badge/resume-PDF-3fb950?style=flat-square)](portfolio.pdf)
[![Telegram](https://img.shields.io/badge/contact-@d3c0r1x-2d333b?style=flat-square&logo=telegram)](https://t.me/d3c0r1x)

**I take a business task and ship a working product.** Given a problem, I design
the architecture, integrate the APIs and the models, debug what doesn't work,
write the tests and bring it to a state someone can actually use — with AI as a
development accelerator, not as a replacement for validation.

**Focus**

- AI integrations & LLM (guardrails, strict JSON schemas, fallback chains, budgets)
- Local AI: Ollama, vision models, OCR — for data that must not leave the machine
- API automation and integrations (marketplaces, banks, RSS, Open-Meteo, CBR)
- Python / FastAPI and TypeScript / React
- Telegram bots & Mini Apps
- Rapid prototyping: idea → working MVP → shipped service

## Selected projects

### 🛒 [Smart Shopper](https://github.com/d3c0r1x/smart-shopper) · [live demo](https://d3c0r1x.github.io/smart-shopper/)

**AI shopping assistant for Ozon, Yandex Market and Wildberries.** Free-form
text or a photo in — grounded recommendations out: every product, price and
review comes from a real marketplace adapter, never from the model.

*What it shows:* end-to-end product work. Hybrid search (semantic + lexical +
structural filtering), LLM gateway with fallback chains and a daily budget,
Review Intelligence that verifies each requirement against actual reviews,
one backend for two interfaces (a Telegram bot and a React Mini App sharing the
same session), 165 tests. [`docs/DECISIONS.md`](https://github.com/d3c0r1x/smart-shopper/blob/main/docs/DECISIONS.md)
explains why each choice was made.

### 🎨 [Paint by Numbers](https://github.com/d3c0r1x/paint-by-numbers) · [live demo](https://d3c0r1x.github.io/paint-by-numbers/)

**Photo → paint-by-numbers coloring page, entirely in the browser.** React +
TypeScript, guided filter → SLIC superpixels → auto-k k-means inside a Web
Worker, Canvas paint layers, IndexedDB projects, plus a native SwiftUI/PencilKit
pilot for iPad.

*What it shows:* client-side engineering — image algorithms, CIEDE2000/OKLab
color maths, Web Worker performance, offline storage, and the same pipeline
ported to Swift. 88 tests.

### 💰 [Finance Bot](https://github.com/d3c0r1x/finance-bot)

**Privacy-first finance assistant for Telegram.** Receipts are read by a
**local** vision model and independently verified by Tesseract against the
receipt's own arithmetic — data never leaves the laptop. Local LLM via Ollama,
SQLite, Tkinter control panel, CI that runs without any model.

*What it shows:* engineering where being wrong costs money. Two independent
receipt readers reconciled by arithmetic, median-based price tracking, honest
statements of what a report does *not* prove, one owner for every shared number
so the bot, the weekly digest and the panel can't disagree.

### ⚙️ [AI Automation Platform](https://github.com/d3c0r1x/ai-automation-platform)

**An agent that runs the task, not just describes it.** "Find 20 items in
category X under 5000 ₽, compare them, pick 5, build a table and send it" — the
platform plans tool calls, validates the plan before running it, executes against
APIs and a browser, pauses for human approval before anything leaves the machine,
and returns a report. Every step, argument and decision is visible.

*What it shows:* architecture where the plan is data, execution survives a
crash, and irreversible steps need a person. FastAPI + PostgreSQL + Redis +
background workers + pydantic tool schemas + Playwright + React dashboard +
Docker + CI that also runs the full PostgreSQL+Redis path. Works end-to-end with
no API keys: the deterministic planner takes over and the report says so.

## Second tier

| Project | What it covers |
|---|---|
| [telegram-stars-payment-gateway](https://github.com/d3c0r1x/telegram-stars-payment-gateway) | monetisation: plans, invoices, PreCheckout/SuccessfulPayment, subscriptions, refunds, server-side price validation |
| [marketplace-price-compare](https://github.com/d3c0r1x/marketplace-price-compare) | parallel API fan-out, normalisation, dedup, TTL cache, watch subscriptions |
| [ozon-seller-bot](https://github.com/d3c0r1x/ozon-seller-bot) | seller-side marketplace API, scheduled jobs, alerts, deterministic demo mode |
| [ozon-price-tracker](https://github.com/d3c0r1x/ozon-price-tracker) | price/stock monitoring, retry and cooldown logic, graceful anti-bot handling |
| [ai-review-analyst](https://github.com/d3c0r1x/ai-review-analyst) | strict JSON from LLM, provider fallback, retry on schema violation |

## How I work

AI tools (Cursor, ChatGPT, Codex, local models) are part of my stack — that is
the point of the role, not something to hide. In every project above I owned the
task decomposition, the architecture and technology choices, API integrations,
debugging, validation of generated code, test scenarios and the final product
behaviour. AI was used as an accelerator; correctness was verified by tests,
live runs against real APIs and real users' data.

Full portfolio and project cards: **[d3c0r1x.github.io](https://d3c0r1x.github.io)** ·
[PDF resume](portfolio.pdf) · [reach me on Telegram](https://t.me/d3c0r1x)

---

## 🇷🇺 По-русски

**AI-first продукт-билдер / вайб-кодер.** Беру бизнес-задачу и довожу её до
рабочего продукта: архитектура, интеграции API и моделей, отладка, тесты,
финальное поведение. AI-инструменты — ускоритель, а не замена проверке.

**Фокус:** интеграции AI/LLM (строгие схемы, fallback-цепочки, бюджеты) ·
локальный AI (Ollama, vision, OCR) для данных, которые не должны покидать
машину · автоматизация и интеграции API · Python/FastAPI · React/TypeScript ·
Telegram-боты и Mini Apps · быстрые MVP от идеи до работающего сервиса.

### Три проекта, которые стоит открыть

- **[Smart Shopper](https://github.com/d3c0r1x/smart-shopper)** · [демо](https://d3c0r1x.github.io/smart-shopper/) —
  ИИ-ассистент покупок: один backend, два интерфейса (бот и Mini App), гибридный
  поиск, проверка требований по отзывам, LLM gateway с бюджетом и fallback.
- **[Paint by Numbers](https://github.com/d3c0r1x/paint-by-numbers)** · [демо](https://d3c0r1x.github.io/paint-by-numbers/) —
  фото → раскраска по номерам целиком в браузере: Web Worker, SLIC + k-means,
  Canvas-слои, IndexedDB, порт ядра на Swift.
- **[Finance Bot](https://github.com/d3c0r1x/finance-bot)** — приватный
  финансовый ассистент: чеки читает локальная vision-модель, независимо
  проверяет Tesseract, данные не покидают ноутбук.

Витрина со всеми проектами — **[d3c0r1x.github.io](https://d3c0r1x.github.io)** ·
[PDF-резюме](portfolio.pdf) · [Telegram](https://t.me/d3c0r1x)

![](https://github-readme-stats.vercel.app/api?username=d3c0r1x&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=3fb950&text_color=e6edf3)
![](https://github-readme-stats.vercel.app/api/top-langs/?username=d3c0r1x&layout=compact&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=e6edf3)
