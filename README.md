# LLM-Based Learning Resource Allocation
## Project Overview

This project leverages Large Language Models (LLMs) to enhance the allocation of educational resources to low-level learning objectives, addressing challenges faced by educators in curating and delivering content. The system is designed to automate the mapping of course objectives to relevant internal and external learning materials, providing students with a personalized and efficient learning experience.

## Key Features

Automated Content Matching: Utilizes a fine-tuned LLM to generate questions based on course objectives and retrieve the most relevant educational resources.

Knowledge Graph Visualization: Implements Neo4J to visualize the relationships between learning objectives and educational content.

Multi-Source Data Integration: Incorporates course textbooks, Canvas slides, and YouTube videos through NLP processing and embedding techniques.

Personalized Learning Experience: The web-based interface enables students to interact dynamically with course materials, filtering by topic and content type.

Scalability: Initially developed for Emory University's BIO 141 and BIO 142 courses, the system is designed to be adaptable across institutions and subjects.

## Methodology

### Data Processing:
Textbooks processed using PyMuPDF to extract and format content.

Course slides converted to text with slide number labeling.

YouTube API used to fetch educational videos, processed with OpenAI's Whisper for audio-to-text conversion.

### Embedding & Retrieval:
Texts are transformed into vector embeddings using the 'instructor-xl' model.

Cosine similarity is applied to match questions with top resources.

### Visualization & User Interface:
Knowledge graph constructed with Neo4J for visual representation.

R Shiny web app developed for user interaction and streamlined access.

## Future Enhancements
Expand resource indexing to include multimedia content such as PDFs and images.

Improve question generation using more sophisticated LLM models.

Implement automatic edge detection in the knowledge graph to enhance relationships between content.

Introduce relevance-based document selection thresholds to improve precision.

## Technologies Used

Programming Languages: Python, R

Libraries & Tools: PyMuPDF, Whisper (OpenAI), instructor-xl, Neo4J, R Shiny

APIs: YouTube API

## Contributors
Christopher Wang

Eric Steinberg

Rayvant Sahni

Sam Liu

Sam Wang

Zach Daube
