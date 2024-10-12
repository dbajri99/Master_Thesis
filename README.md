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
- gpt_prompting_techniques.ipynb: This Jupyter notebook, located in the LLM_paper_ratings folder, employs advanced GPT-4.o prompting techniques to evaluate the depth of discussions on LLM limitations in academic papers. Ensure you have the openai and tqdm packages installed (pip install openai tqdm). Before running, update the notebook with your OpenAI API key.
- Open_Source_Model_Prompting_Techniques.ipynb: In the open_source_prompting_techniques folder, the Open_Source_Model_Prompting_Techniques.ipynb uses the "Mistral-7B-Instruct-v0.2" model from HuggingFace to rate academic papers on language model limitations. Ensure dependencies (tqdm, json, csv, langchain_community.llms) are installed and set the HuggingFace API token. Open the notebook, run cells to input a prompt number (1-3), and execute the assessment. Results are saved in a CSV file, summarizing titles, LLM discussions, ratings, and evidence.
- data_analysis.ipynb: For the data_analysis.ipynb notebook, ensure the dataset results_time_series_acl_all_papers.csv is correctly placed in your project directory. Install necessary Python packages like pandas, numpy, matplotlib, and seaborn using pip or conda. Open the notebook, execute all cells to process the data, perform analyses, and generate visualizations showing trends in ACL and Arxiv papers discussing LLM limitations. Modify the analysis period or visualization styles directly within the notebook as needed. Visual outputs can be viewed within the notebook or saved as images for external use.
- limitations_clustering.ipynb: Applies clustering algorithms to the analyzed papers to categorize discussed LLM limitations into a coherent taxonomy. This notebook synthesizes the findings into structured groups, aiding in the understanding and visualization of common themes and issues within the field.







