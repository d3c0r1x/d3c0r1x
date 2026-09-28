# d3c0r1x — AI Product Developer / Vibe Coder

[![Portfolio](https://img.shields.io/badge/portfolio-d3c0r1x.github.io-58a6ff?style=flat-square)](https://d3c0r1x.github.io) ·
[![Telegram](https://img.shields.io/badge/contact-@d3c0r1x-2d333b?style=flat-square&logo=telegram)](https://t.me/d3c0r1x)

**AI-assisted developer focused on building working products and business automation.**

I take a concrete task, turn it into a working system, connect APIs and AI models, debug the result, add tests and document how it works. I use Cursor, ChatGPT, Codex and local models as development accelerators; generated code still has to run and be validated.

## What I build

- AI/LLM integrations, structured outputs, tool calling and fallback logic
- Business-process automation and agentic workflows
- Python / FastAPI backends and background workers
- React / TypeScript interfaces and Telegram Mini Apps
- Telegram bots and integrations
- Local AI, Vision and OCR
- MVPs from idea → prototype → tested service

## Flagship projects

These are the projects I use to represent my work. Each README contains architecture, setup, examples, tests and limitations.

### 🛒 [Smart Shopper](https://github.com/d3c0r1x/smart-shopper) · [live demo](https://d3c0r1x.github.io/smart-shopper/)

**Интересный личный проект, над которым я работал длительное время.**

AI shopping assistant for Ozon, Yandex Market and Wildberries.

**Text/photo → real marketplace data → filtering/ranking → review analysis → recommendation.**

Shows LLM integration, grounding, hybrid search, API adapters, Telegram + React Mini App, shared session state, Vision, fallbacks and security/testing.

### ⚙️ [AI Automation Platform](https://github.com/d3c0r1x/ai-automation-platform)

**Интересный личный проект, над которым я работал длительное время.**

Task-running automation MVP:

**natural language → validated plan → queue → tools → progress → report**, with a human approval gate before external side effects.

Shows FastAPI, Pydantic tool contracts, Redis, PostgreSQL/SQLite, workers, Playwright, SSE, React dashboard, retries, checkpoints, Docker and CI.

### 💰 [Finance Bot](https://github.com/d3c0r1x/finance-bot)

**Интересный личный проект, над которым я работал длительное время.**

Local-first Telegram finance assistant. Receipt photos are processed with a local Vision model, independently checked by Tesseract and then validated arithmetically.

Shows local AI, Vision/OCR, data reconciliation, SQLite, scheduled jobs, budgeting, reports, desktop UI and reusable service logic.

### 🎨 [Paint by Numbers](https://github.com/d3c0r1x/paint-by-numbers) · [live demo](https://d3c0r1x.github.io/paint-by-numbers/)

**Интересный личный проект, над которым я работал длительное время.**

Browser application that converts a photo into a numbered painting and lets the user paint it directly in the browser.

Shows React/TypeScript, Canvas, Web Workers, IndexedDB, SLIC, k-means, colour-difference algorithms, performance work and an experimental SwiftUI/PencilKit client.

### ⛓️ [MEXC × DEX Arbitrage Monitor](https://github.com/d3c0r1x/arbitrage-monitor)

**Интересный личный проект, над которым я работал длительное время.**

Research/monitoring system for CEX↔DEX and DEX↔DEX opportunities with on-chain quotes, fees, slippage, trade-size sweep, watcher, dashboard and safety controls.

Shows async Python, Web3/EVM, market-data integration, numerical calculations, concurrency, operational safeguards and iterative V1→V6 development.

## Supporting project

### 🛍️ [Marketplace Price Compare](https://github.com/d3c0r1x/marketplace-price-compare)

**Единственный представитель серии небольших marketplace-прототипов.**

Compact engineering case: parallel marketplace adapters, common data model, normalization, deduplication, price comparison, scheduled price-watch and SQLite persistence.

The separate ai-review-analyst and ozon-price-tracker repositories are kept only as historical/supporting prototypes; their ideas were later developed inside the larger projects above.

## Additional applied component

[Telegram Stars Payment Gateway](https://github.com/d3c0r1x/telegram-stars-payment-gateway) — focused payment/subscription component with Telegram Stars, trial periods, refunds and server-side payload validation.

## How I work

**task → decomposition → architecture → AI-assisted implementation → run/debug → tests → documentation → refinement**

AI is an accelerator, not a substitute for validation. Important logic is checked with tests, live runs or deterministic demo data.

## Learning archive

The repositories marked as archived on GitHub are **EXCLUSIVELY LEARNING PROJECTS** from an earlier stage. They are intentionally not part of the main portfolio.

Start here for the work I currently use to represent myself:

- [Portfolio](https://d3c0r1x.github.io)
- [Smart Shopper](https://github.com/d3c0r1x/smart-shopper)
- [AI Automation Platform](https://github.com/d3c0r1x/ai-automation-platform)
- [Finance Bot](https://github.com/d3c0r1x/finance-bot)
- [Paint by Numbers](https://github.com/d3c0r1x/paint-by-numbers)
- [MEXC × DEX Arbitrage Monitor](https://github.com/d3c0r1x/arbitrage-monitor)

## Contact

Portfolio: https://d3c0r1x.github.io  
GitHub: https://github.com/d3c0r1x  
Telegram: https://t.me/d3c0r1x