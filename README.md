# Reddit Complexity LLM (WIP)

A specialized language model designed to analyze and quantify linguistic complexity in Reddit comments. This project serves as a foundational step in exploring the relationship between language, conceptual complexity, and socioeconomic patterns.

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Dataset](#dataset)
- [Evaluation Metrics](#evaluation-metrics)
- [Tools and Libraries](#tools-and-libraries)
- [License](#license)

---

## Overview

The Reddit Complexity LLM is an NLP research project designed to assess linguistic complexity in Reddit comments. By leveraging a custom evaluation metric, the model quantifies features such as syntax intricacy, noun usage, and semantic diversity. This project lays the groundwork for broader research into the interplay between language and socioeconomic factors.

## Key Features

1. **Custom Evaluation Metrics**: Measures linguistic complexity using features such as:
   - Syntax complexity (e.g., subordination, recursion).
   - Structural patterns in comments.
   - Noun usage and frequency.
   - Topic diversity and semantic richness.

2. **Transformer-Based Architecture**: Utilizes a transformer-based model fine-tuned for analyzing Reddit comments.

3. **Scalable and Extensible**: Designed to accommodate large datasets and adapt to additional features for advanced linguistic analysis.

## Architecture

The core architecture leverages transformer models, integrating:
- **Multi-Head Self-Attention**: Captures contextual relationships within Reddit comments.
- **Positional Encoding**: Preserves word order and syntax structure.
- **Layer Normalization**: Stabilizes training dynamics.
- **Custom Output Layer**: Outputs complexity scores based on defined evaluation metrics.

## Dataset

The dataset consists of scraped Reddit comments using the [PRAW](https://praw.readthedocs.io/en/stable/) library. Key preprocessing steps include:
- Tokenization using `SpaCy`.
- Removal of non-linguistic artifacts such as URLs, emojis, and markdown formatting.
- Syntax parsing to extract sentence-level features.

### Example Datasets
- **Subreddits**: r/Dallas, r/Plano, r/Frisco.
- **Data Structure**: Each comment includes metadata (e.g., subreddit, timestamp, user ID) and linguistic annotations.

## Evaluation Metrics

The custom evaluation metric includes:
- **Syntax Complexity**: Counts of subordination, conditional clauses, and recursion.
- **Noun Usage**: Frequency of abstract vs. concrete nouns.
- **Topic Diversity**: Entropy-based measures of topical variation within comment clusters.
- **Readability**: Uses established indices like Flesch-Kincaid and Gunning Fog.

## Tools and Libraries

- **Reddit API (PRAW)**: For data scraping.
- **PyTorch**: Framework for model training and evaluation.
- **SpaCy**: For NLP preprocessing.
- **Transformers**: Hugging Face library for transformer-based models.
- **NumPy/Pandas**: For data manipulation.
- **Matplotlib/Seaborn**: For data visualization.

---

## Contact
Feel free to reach out for collaborations or inquiries:
- **Email**: prachidalal084@gmail.com
- **LinkedIn**: [Prachi Dalal](https://www.linkedin.com/in/prachidalal2/)
- **GitHub**: [@prachidalal0](https://github.com/prachidalal0)

---

## License
This project is licensed under the [MIT License](LICENSE).
