# Привет, я d3c0r1x 👋

**AI вайб-кодер и прототипист.** Самостоятельно довожу прототипы и MVP от идеи до рабочего продукта, используя AI-инструменты: Cursor, ChatGPT, OpenRouter и другие LLM. Идея → промпт → рабочий код → отладка → работающий сервис.

## Чем я занимаюсь

- разработка AI-сервисов и автоматизация рутинных процессов;
- интеграция внешних API и AI-моделей (OpenRouter, YandexGPT, OpenAI-совместимые API, Ollama);
- создание Telegram-ботов и Telegram Mini Apps;
- разработка backend на Python/FastAPI;
- работа с LLM, Vision-моделями и prompt engineering;
- создание и тестирование MVP — от идеи до рабочего прототипа;
- отладка и доработка AI-сгенерированного кода;
- интеграция сервисов маркетплейсов и работа с данными Ozon, Wildberries и Яндекс Маркета.

## Стек

**Языки и backend:** Python 3.11+, FastAPI, TypeScript, React
**Telegram:** aiogram 3, Telegram Mini App (React + Vite), Telegram Stars
**AI/LLM:** OpenRouter (OpenAI-совместимые API), YandexGPT, Ollama (локальные LLM и Vision-модели), prompt engineering, строгий JSON на pydantic
**Интеграции:** Ozon, Wildberries, Яндекс Маркет, Open-Meteo, ЦБ РФ, RSS/Atom, PDF
**Данные и инфраструктура:** SQLite (aiosqlite), APScheduler, Docker, GitHub Actions, pytest

## Реализованные проекты

### [Smart Shopper](https://github.com/d3c0r1x/smart-shopper) — AI-ассистент для поиска и анализа товаров на маркетплейсах

«ChatGPT для маркетплейсов»: свободный текст или фото — а рекомендация опирается только на реальные данные Ozon, Яндекс Маркета и Wildberries (принцип grounding), без выдуманных товаров. LLM-слой через OpenRouter со строгой JSON-схемой на pydantic. Один backend — два интерфейса: Telegram-бот и Telegram Mini App на React с общим состоянием сессии: «а подешевле», «только чёрные» уточняют прошлый поиск, а не начинают его заново.

### [Marketplace Price Compare](https://github.com/d3c0r1x/marketplace-price-compare) — сравнение товаров и цен между маркетплейсами

Запрос уходит во все маркетплейсы параллельно (`asyncio.gather`), выдача объединяется, сортируется по цене, лучшая помечается. Подписки на запрос (`/watch`): уведомление, когда лучшая цена упала или достигла порога. TTL-кэш выдач, дедупликация по паре «маркетплейс + ID».

### [AI Review Analyst](https://github.com/d3c0r1x/ai-review-analyst) — автоматический анализ отзывов покупателей с помощью LLM

Топ-3 проблемы и топ-3 преимущества товара по последним 50 отзывам с Wildberries. Модель обязана вернуть строгий JSON: при несоответствии схеме бот повторно запрашивает её с описанием конкретной ошибки (pydantic + ретраи), отзывы кэшируются для снижения нагрузки на API.

### [Ozon Price Tracker](https://github.com/d3c0r1x/ozon-price-tracker) — Telegram-бот для отслеживания цен и остатков

Периодическая проверка по расписанию с уведомлениями: цена упала или выросла, достигнут персональный порог, товар снова в наличии или заканчивается. TTL-кэш карточек, индексы SQLite, кулдаун уведомлений против спама.

### [Telegram Stars Payment Gateway](https://github.com/d3c0r1x/telegram-stars-payment-gateway) — интеграция платежей и платного доступа в Telegram

Доступ к AI-аналитике только после оплаты подписки Telegram Stars (или тестовый режим ЮKassa): обработка `PreCheckoutQuery` и `SuccessfulPayment`, тарифы на инлайн-кнопках, журнал платежей, возвраты с отзывом доступа, пробный период один раз на пользователя и автоматическое отключение подписки по истечении срока.

### [Ozon Seller Bot](https://github.com/d3c0r1x/ozon-seller-bot) — MVP-бот для продавцов Ozon

Сводка магазина в Telegram: выручка и заказы, контроль остатков (🔴 нет в наличии, 🟡 заканчивается), топ товаров по выручке. Клиент Seller API с детерминированным демо-режимом: без ключей бот работает на воспроизводимых данных и честно помечает их как демо — функционал можно показать без доступа к магазину.

## Остальные проекты

| Репозиторий | Описание |
|---|---|
| [finance-bot](https://github.com/d3c0r1x/finance-bot) | Учёт расходов и кредитов: чтение чеков локальной Vision-моделью (Ollama) + Tesseract, бюджет, долги, панель на Tkinter |
| [paint-by-numbers](https://github.com/d3c0r1x/paint-by-numbers) | Веб-приложение на TypeScript: фото → раскраска по номерам с рисованием кистью ([демо](https://d3c0r1x.github.io/paint-by-numbers/)) |
| [wb-price-tracker](https://github.com/d3c0r1x/wb-price-tracker) | Отслеживание цен Wildberries с уведомлениями |
| [pdf-sales-reports](https://github.com/d3c0r1x/pdf-sales-reports) | PDF-отчёты по продажам: CSV → pandas → matplotlib → reportlab → Telegram |
| [arbitrage-monitor](https://github.com/d3c0r1x/arbitrage-monitor) | Мониторинг цен маркетплейсов для поиска арбитражных ниш (версии V1–V6) |

## Портфолио

Все 12 учебных проектов: [learning-projects](https://github.com/d3c0r1x/learning-projects)

## 🇬🇧 About me in English

**AI vibe coder & prototyper.** I take prototypes and MVPs from idea to a working product on my own, using AI tools: Cursor, ChatGPT, OpenRouter and other LLMs. Idea → prompt → working code → debugging → shipped service.

**What I do:** AI services and workflow automation · external API and AI model integration (OpenRouter, YandexGPT, OpenAI-compatible APIs, Ollama) · Telegram bots and Telegram Mini Apps · Python/FastAPI backends · LLM, Vision models and prompt engineering · MVP development from idea to working prototype · debugging and refactoring AI-generated code · marketplace integrations with Ozon, Wildberries and Yandex Market data.

**Key projects:** [Smart Shopper](https://github.com/d3c0r1x/smart-shopper) (LLM shopping assistant: search by text and photo across marketplaces, Telegram bot + Mini App) · [Marketplace Price Compare](https://github.com/d3c0r1x/marketplace-price-compare) (parallel price comparison across WB, Ozon and Yandex Market) · [AI Review Analyst](https://github.com/d3c0r1x/ai-review-analyst) (LLM-based review analysis with strict JSON schemas) · [Ozon Price Tracker](https://github.com/d3c0r1x/ozon-price-tracker) (price and stock monitoring with alerts) · [Telegram Stars Payment Gateway](https://github.com/d3c0r1x/telegram-stars-payment-gateway) (subscriptions and paid access in Telegram).

**Full portfolio:** [landing page](https://d3c0r1x.github.io/d3c0r1x/) · [all repositories](https://github.com/d3c0r1x?tab=repositories)
