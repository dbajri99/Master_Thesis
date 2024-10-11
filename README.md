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
#### Data Retrieval Scripts Setup and Usage
To run the data retrieval scripts for ACL Anthology and arXiv, first ensure Python is installed on your system. Install necessary dependencies with pip install requests beautifulsoup4 tqdm arxiv. For the ACL script, navigate to the script's directory and run python "ACL retriever.ipynb" to fetch and save papers in a JSON format (e.g., acl2023.json). Similarly, for the arXiv script, execute python "arXiv retriever.ipynb" to retrieve and store articles (e.g., data_collected_Jan2022-Feb2022.json). Both scripts allow customization of query parameters, such as date ranges and fields, to suit specific research needs.

### Code Description
This repository contains a collection of Jupyter Notebooks that form the experimental pipeline of this thesis project:

- Filter_Papers.ipynb: Located in the "filtering_dataset" folder, this notebook filters scientific papers from a JSON dataset based on specified keywords found in the titles or abstracts. The filtering process uses regular expressions for efficient matching, and the results are exported to a new JSON file for further analysis.
- gpt_prompting_techniques.ipynb: Found in the "LLM_paper_ratings" folder, this notebook details various prompting techniques used to assess papers with GPT models. It experiments with different methods to determine how well these models can evaluate and rate the discussion depth of LLM limitations within academic papers.
