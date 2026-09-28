"""Генерация одностраничного PDF-резюме (A4) из данных портфолио.

Запускается локально и из GitHub Action (.github/workflows/resume.yml).
Содержимое зеркалит профильный README; при изменении портфолио правится здесь.
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BG, TEXT, MUTED, ACCENT = "#ffffff", "#1f2328", "#57606a", "#0969da"

fig = plt.figure(figsize=(8.27, 11.69))  # A4
fig.patch.set_facecolor(BG)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")


def t(x, y, s, size=10, color=TEXT, weight="normal", va="top"):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight, va=va,
            fontfamily="DejaVu Sans", transform=ax.transAxes)


# Шапка
t(0.07, 0.965, "d3c0r1x", 26, TEXT, "bold")
t(0.07, 0.928, "AI вайб-кодер и прототипист — прототипы и MVP от идеи до работающего сервиса", 12.5, ACCENT, "bold")
t(0.07, 0.903, "github.com/d3c0r1x  ·  d3c0r1x.github.io  ·  Python/FastAPI · Telegram · LLM/Vision · маркетплейсы", 9.5, MUTED)
ax.plot([0.07, 0.93], [0.888, 0.888], color="#d0d7de", linewidth=1, transform=ax.transAxes)

# Направления
t(0.07, 0.862, "НАПРАВЛЕНИЯ", 11, TEXT, "bold")
t(0.07, 0.838,
  "AI-сервисы и автоматизация · интеграция API и AI-моделей (OpenRouter, YandexGPT, Ollama) · Telegram-боты и Mini Apps\n"
  "backend на Python/FastAPI · LLM, Vision, prompt engineering · MVP от идеи до прототипа · отладка AI-кода\n"
  "данные Ozon, Wildberries, Яндекс Маркета", 9.5, MUTED)

# Проекты
t(0.07, 0.768, "КЛЮЧЕВЫЕ ПРОЕКТЫ", 11, TEXT, "bold")
projects = [
    ("Smart Shopper — AI-ассистент покупок (Telegram-бот + Mini App)",
     "Поиск по тексту и фото через LLM с grounding на данные Ozon / Я.Маркета / WB. OpenRouter, строгий JSON на pydantic, общее состояние сессии."),
    ("Ozon Seller Bot — MVP для продавцов (полный роадмап 5/5)",
     "Сводка магазина, контроль остатков, алерты цен/рейтингов по снапшотам, график выручки, FBS-отправления. Seller API + детерминированный демо-режим без ключей."),
    ("Finance Bot — учёт расходов с Vision-LLM",
     "Фото чека читают локальная qwen3-vl (Ollama) и Tesseract; победитель по арифметике. Бюджеты, долги, отчёты, панель Tkinter, CI с тремя наборами тестов."),
    ("Marketplace Price Compare / Ozon & WB Price Trackers",
     "Параллельный поиск по трём маркетплейсам, watch-подписки на снижение цены, алерты по порогам, история в SQLite, curl_cffi против антибота."),
    ("AI Review Analyst · Stars Payment Gateway · Paint by Numbers",
     "Анализ отзывов LLM с ретраями по схеме · платный доступ через Telegram Stars/ЮKassa · раскраска по номерам: SLIC + k-means в Web Worker (React/TS, демо на Pages)."),
]
y = 0.742
for name, desc in projects:
    t(0.07, y, "• " + name, 10.5, TEXT, "bold")
    t(0.10, y - 0.024, desc, 9.3, MUTED)
    y -= 0.062

# Стек и практики
t(0.07, y - 0.01, "СТЕК И ПРАКТИКИ", 11, TEXT, "bold")
t(0.07, y - 0.034,
  "Python 3.11+ · FastAPI · aiogram 3 · TypeScript · React/Vite · OpenRouter/YandexGPT/Ollama · pydantic\n"
  "SQLite (aiosqlite) · APScheduler · matplotlib · Docker · GitHub Actions (CI в каждом проекте) · pytest\n"
  "Практики: детерминированные демо-режимы без секретов, строгие JSON-схемы, миграции без простой, README с роадмапами", 9.5, MUTED)

# Как работаю
t(0.07, y - 0.104, "КАК РАБОТАЮ", 11, TEXT, "bold")
t(0.07, y - 0.128,
  "Идея и рамка недели → архитектура со спорами с LLM → вайб-кодинг малыми итерациями (промпт → дифф → запуск) →\n"
  "чтение AI-кода как код-ревью → CI и демо без ключей → MVP с реальным пользователем. 12+ проектов в портфолио.", 9.5, MUTED)

# Футер
t(0.5, 0.035, "Актуальная версия: d3c0r1x.github.io · Обновлено: сентябрь 2026", 8.5, MUTED, va="bottom")

fig.savefig("portfolio.pdf", format="pdf", facecolor=BG)
print("OK portfolio.pdf")
