# Answer Evaluation Engine

## Overview

A FastAPI-based Answer Evaluation Engine that evaluates candidate answers using a hybrid approach combining rule-based checks and semantic similarity scoring.

## Features

* Empty answer detection
* Irrelevant answer detection
* Semantic similarity scoring
* Confidence score generation
* Feedback generation
* Supports DSA, DBMS, and OS domains

## Tech Stack

* Python
* FastAPI
* Sentence Transformers
* Scikit-Learn
* Pytest

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python -m uvicorn app:app --reload
```

## API Documentation

```text
http://127.0.0.1:8000/docs
```

## Example Request

```json
{
  "question": "What is Binary Search?",
  "answer": "Binary Search is a searching algorithm that works on sorted arrays and runs in O(log n)."
}
```

## Example Response

```json
{
  "score": 8.3,
  "feedback": "Answer appears relevant and reasonably complete.",
  "confidence": 0.8
}
```
