# Semantic Retrieval Engine

**Find what you mean, not just what you type.**

A Python-based semantic search system that uses sentence embeddings and ChromaDB to retrieve contextually relevant information. It goes beyond keyword matching by understanding the meaning behind a user's query.

## Features

- **Semantic Search:** Finds relevant FAQs using sentence embeddings rather than exact keyword matches.
- **Vector Database:** Stores and retrieves embeddings using persistent ChromaDB storage.
- **Top-K Retrieval:** Returns the three closest matches ranked by cosine distance.
- **Relevance Filtering:** Uses a configurable distance threshold to reject weak matches.
- **Ambiguity Detection:** Identifies queries where the top results have similar distances.
- **Interactive Clarification:** Allows users to select the FAQ that best matches their intent.
- **Input Validation:** Handles empty queries, invalid selections, and cancellation.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application |
| Sentence Transformers | Text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Persistent vector storage |
| NumPy | Numerical operations |
| uv | Python project and dependency management |

## How It Works

1. **Data Ingestion:** FAQ questions are loaded from a JSON dataset.
2. **Embedding Generation:** Each question is converted into a 384-dimensional vector using `all-MiniLM-L6-v2`.
3. **Vector Storage:** Embeddings and associated metadata are stored in ChromaDB.
4. **Query Processing:** User queries are converted into embeddings using the same model.
5. **Similarity Search:** ChromaDB retrieves the three nearest FAQ matches using cosine distance.
6. **Relevance Filtering:** Results beyond the configured distance threshold are discarded.
7. **Ambiguity Detection:** The distance gap between the top two results is checked to identify potentially ambiguous queries.
8. **User Selection:** When ambiguity is detected, users can select the intended result instead of receiving an assumed answer.

## Project Structure

```text
semantic-retrieval-engine/
│
├── src/
│   ├── data/
│   │   ├── faqs.json
│   │   ├── test_queries.json
│   │   └── holdout_queries.json
│   │
│   ├── embeddings.py
│   ├── database.py
│   ├── similarity.py
│   ├── search.py
│   ├── main.py
│   └── evaluate.py
│
├── chroma_db/          # Generated persistent database
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.14 or compatible version as specified in `pyproject.toml`
- [uv](https://docs.astral.sh/uv/)

### 1. Clone the repository

```bash
git clone https://github.com/nsfwsabir/semantic-retrieval-engine.git

cd semantic-retrieval-engine
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Ingest the FAQ dataset

Generate embeddings and populate the ChromaDB collection:

```bash
uv run python src/database.py
```

### 4. Run the application

```bash
uv run python src/main.py
```

Enter a query and explore the retrieved results. Type `exit` to close the application.

## Example

**Query:**

```text
I cannot access my account
```

**Retrieved results:**

| Rank | Retrieved FAQ | Cosine Distance |
|---|---|---:|
| 1 | Locked account | 0.2306 |
| 2 | Password reset | 0.4087 |
| 3 | Account deletion | 0.4556 |

The engine ranks the locked-account FAQ first because it is the closest semantic match.

For a vague query such as:

```text
I need help with my account
```

the engine detects that the top results are relatively close and asks the user to clarify their intent.

## Configuration

The retrieval behavior can be adjusted in `src/search.py` and `src/main.py`.

| Parameter | Default | Description |
|---|---:|---|
| `top_k` | 3 | Number of nearest results |
| `max_distance` | 0.5 | Maximum accepted cosine distance in the search function |
| Ambiguity gap | 0.10 | Distance-gap threshold used to flag ambiguous queries |

Lower cosine distance indicates greater similarity. The ambiguity gap is a heuristic, not a confidence score.

## Evaluation

The system was evaluated using a separate holdout dataset containing 20 queries:

- 15 in-domain queries covering the FAQ dataset.
- 5 out-of-domain queries covering unrelated topics.

**Holdout evaluation results**

| Metric | Result |
|---|---:|
| Total queries | 20 |
| Correct predictions | 20 |
| Incorrect predictions | 0 |
| In-domain retrieval | 15/15 |
| Out-of-domain rejection | 5/5 |
| Hit Rate@1 | **100%** |

The evaluation achieved 100% on this particular holdout set using a cosine-distance threshold of 0.6.

*Note: This is a small evaluation dataset. The result demonstrates performance on the tested queries, not guaranteed accuracy on unseen real-world queries.*

To run the evaluation:

```bash
uv run python src/evaluate.py
```

The evaluation script uses the holdout dataset at `src/data/holdout_queries.json`.

## Future Scope

- Expand the FAQ dataset with more diverse queries.
- Explore hybrid keyword and semantic retrieval.
- Integrate a language model to generate context-aware responses.
- Extend retrieval to documents and larger knowledge bases.

## License

This project is open source. See the repository for licensing information.
