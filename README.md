# CheeseIA

> Applied AI experiment for automatically analyzing and categorizing product reviews.

**Python · LLMs · NLP · Structured Classification · Batch Processing**

| | |
|---|---|
| **Type** | Applied AI / NLP project |
| **Focus** | Review analysis and classification |
| **Input** | Product review text + rating |
| **Output** | Structured analysis and quality-oriented categorization |
| **Status** | Public technical experiment |

## Overview

CheeseIA explores a practical applied-AI workflow: transforming unstructured product reviews into structured information that can be categorized and processed programmatically.

Rather than using an LLM only as a conversational interface, the project treats AI as an **analysis component inside a software workflow**.

## Use case

A collection of product reviews can contain useful signals about quality, presentation and overall customer experience, but extracting those signals manually does not scale.

CheeseIA provides a small abstraction for:

- analyzing an individual review;
- processing reviews in batches;
- categorizing review content;
- organizing results by quality-related criteria.

## Processing flow

```text
Review + Rating
      │
      ▼
 AI Analysis Layer
      │
      ▼
Structured Categories
 ┌────┼──────────┐
 │    │          │
Quality  Presentation  Experience
      │
      ▼
Batch Processing / Ordering
```

## Categories

Current analysis focuses on:

- product quality;
- product presentation;
- overall experience.

## Basic usage

```python
from avaliacao_analyzer import AvaliacaoAnalyzer

analyzer = AvaliacaoAnalyzer()

result = analyzer.analisar_avaliacao(
    "Produto excelente!",
    5,
)

reviews = [
    ("Produto excelente!", 5),
    ("A embalagem poderia melhorar.", 3),
]

results = analyzer.processar_lote(reviews)
ordered = analyzer.ordenar_por_qualidade(results)
```

## Setup

```bash
git clone https://github.com/jdrpires/CheeseIA.git
cd CheeseIA

pip install -r requirements.txt
cp .env.example .env
```

Configure the required AI provider credentials through local environment variables.

> Never commit API keys or provider credentials to the repository.

## Engineering perspective

The important concept in this project is not the prompt itself. It is the boundary between probabilistic AI output and deterministic application behavior.

For production-oriented AI systems, this pattern can evolve toward:

- structured schemas for model output;
- confidence/validation rules;
- deterministic fallback behavior;
- observability of model calls;
- evaluation datasets;
- human review for ambiguous classifications.

## Why this project is public

CheeseIA is part of my public engineering portfolio and demonstrates an early applied-AI pattern: embedding LLM/NLP capabilities into a repeatable software process.

---

**Jean Pires** · [GitHub](https://github.com/jdrpires) · [Portfolio](https://github.com/jdrpires/jdrpires)
