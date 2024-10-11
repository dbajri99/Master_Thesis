## Master Thesis on Large Language Model Limitations
### Project Overview
This repository contains the script conducted for my master's thesis, focusing on identifying and analyzing limitations of Large Language Models (LLMs). The study examines approximately 145,800 academic papers from ArXiv and ACL Anthology, ranging from 2022 to 2024, to create a taxonomy of LLM limitations.

In this project, we use methods such as zero-shot and few-shot learning applied to OpenAI GPT-3.5 Turbo, GPT 4.o [gpt-4o-2024-05-13] and two opensource models: LLaMa2 [meta-llama/Llama-2-7b-chat-hf] and Mistral [”mistralai/Mistral-7B-Instruct-v0.2], LLM-based embeddings using OpenAI's feature [text-embedding-ada-002], BERTopic clustering combined to HDBSCAN, and the semi-supervised clustering using few-shot learning approach by using the OpenAI's GPT-3.5 Turbo to evaluate and categorize these limitations into clusters like reasoning failures, bias propagation, hallucination risks, privacy concerns, and resource constraints.
The taxonomy categorizes LLM challenges into five areas: Cognitive and Logical Limitations, Ethical and Social Limitations, Technical and Operational Limitations, Application-Specific Limitations, and Performance and Reliability. 

### Data Crawling Scripts
This section includes Python scripts for automated data retrieval from interacting with arXiv and ACL Anthology APIs, targeting papers published from the beginning of 2022 to the start of 2024. The scripts, housed in this repository's "data_crawling" folder, facilitate systematic collection and structuring of data into JSON format. This format includes essential details such as titles, authors, publication dates, summary (abstracts), and full-text links.
#### ACL retriever.ipynb
- Dynamic URL Construction: Automatically generates URLs based on specified conference names and years.
- Data Scraping: Extracts key details such as titles, authors, publication dates, summaries, and PDF links.
- Progress Tracking: Utilizes tqdm to provide real-time progress feedback during data retrieval.
- HTML Structure Adaptation: Efficiently handles different HTML structures across multiple data sources.
#### ArXiv retriever.ipynb
- Dynamic Query Building: Constructs search queries based on user-specified fields ("cs.CL", "cs.LG", 'cs.AI', 'cs.CV'), categories, and date ranges.
- Robust Handling: Efficiently processes large volumes of data, with built-in mechanisms for retries and pagination.
