# Supplementary Technical Documentation

## (1) LLMs and How They Can Run Locally 

See the original [repo](https://github.com/kenminsoo/llm_textbook_support) for technical implementation of LLM application.

### 1. **Purpose**

The objective here is to utilize Large Language Models (LLMs) in a local environment, primarily within educational institutions. By running LLMs locally, educational entities can mitigate ongoing costs associated with subscription-based models and dependence on external server infrastructures. This approach allows for the generation of study guide questions, answering student queries, and evaluating student responses, thereby enhancing the educational experience through AI-driven personalization and support.

### 2. **Basic Theory**

#### a. **Understanding Large Language Models (LLMs):**
- LLMs like GPT-3 or BERT are advanced AI models designed to understand, generate, and interact with human language. They are trained on vast amounts of text data and can perform a variety of language tasks like translation, summarization, question answering, etc.
- These models use neural network architectures, particularly transformer models, which allow them to process and generate language in a contextually relevant manner.

#### b. **Local vs. Cloud-Based Deployment:**
- **Cloud-Based Deployment:** Traditionally, LLMs are hosted on cloud servers due to their substantial computational requirements. This setup usually involves subscription fees and reliance on the service provider's server uptime and data policies.
- **Local Deployment:** Running LLMs locally entails setting up the model on an institution's own hardware infrastructure. This method can be more cost-effective over time (sunk cost) and offers greater control over data privacy and usage.

### 3. **Implementation**

#### a. **Setting Up LLMs Locally:**
- **Hardware Requirements:** Running an LLM locally requires significant computational resources. This includes powerful CPUs, GPUs (or TPUs), and substantial memory and storage capacity.
- **Software Setup:** Setting up involves installing the necessary machine learning frameworks (like TensorFlow or PyTorch), obtaining the LLM model (either pre-trained or training from scratch if resources allow), and configuring it for the specific tasks.

#### b. **Applications in Education:**
- **Creating Study Guides:** LLMs can generate customized study materials based on the curriculum, adapting to different learning styles and difficulties.
- **Answering Student Queries:** They can provide real-time assistance to students, clarifying doubts, and offering detailed explanations.
- **Evaluating Student Responses:** LLMs can be trained to assess student answers, providing instant feedback and even grading assignments, though with a critical understanding of their limitations.

#### c. **Addressing Inaccuracy Issues:**
- Large Language Models, while powerful, are known to occasionally produce inaccurate or biased information. To mitigate this:
  - **Regular Updates and Monitoring:** Continuously update the model with accurate and diverse data sources. Regularly monitor its outputs for quality and accuracy.
  - **Human Oversight:** Implement a system where educators can review and correct the outputs of the model, especially for critical tasks like student evaluation.
  - **Supplementary Tools:** Combine the LLM with other educational tools and resources to ensure a well-rounded and accurate learning experience.

## (2) Knowledge Graphs and Utilizing NetworkX to Build These Knowledge Graphs

### 1. **Purpose**

The purpose of this task is to construct knowledge graphs that effectively link educational resources — such as textbook paragraphs, PDF slideshow sections, and YouTube videos — to specific learning objectives in a classroom setting. By doing so, the project aims to develop a standalone application that enables students to easily identify and access relevant learning materials with a single click. This approach is designed to facilitate a more integrated and resource-rich learning experience.

### 2. **Basic Theory**

#### a. **Understanding Knowledge Graphs:**
- Knowledge graphs represent a collection of interlinked descriptions of entities — objects, events, or concepts. In the context of education, these entities could be learning materials or objectives.
- These graphs are structured in a way that both the relationships (edges) between different pieces of information (nodes) and the information itself are explicitly defined.

#### b. **NetworkX for Building Knowledge Graphs:**
- NetworkX is a Python library used for creating, manipulating, and studying the structure, dynamics, and functions of complex networks. It is well-suited for constructing knowledge graphs due to its flexibility and ease of use in handling graph structures.

#### c. **Integrating Educational Resources:**
- **Textbook and Slideshows:** Linking sections of textbooks and slideshows to learning objectives involves parsing these resources and tagging them with relevant metadata that aligns with the curriculum’s goals.
- **YouTube API and Video Parsing:**
  - **YouTube API:** Used for accessing video content related to the course material.
  - **Pytube:** A Python library for downloading YouTube videos.
  - **Whisper.cpp for Transcription:** A tool for converting spoken language in videos to text, which can then be integrated into the knowledge graph.

### 3. **Implementation**

#### a. **Building the Knowledge Graph with NetworkX:**
- **Data Collection:** Gather all educational resources, including textbook content, slides, and relevant YouTube video URLs.
- **Data Parsing and Tagging:** Use text analysis techniques to extract and tag relevant sections of the textbooks and slides with learning objectives. 
- **Graph Construction:** Use NetworkX to create nodes for each learning resource and objective. Define edges based on the relationships between these entities, such as which resources pertain to which learning objectives.

#### b. **Video Integration:**
- **Downloading Videos:** Use Pytube to download relevant YouTube videos.
- **Transcribing Videos:** Apply Whisper.cpp or a similar tool to transcribe the audio content of the videos into text.
- **Incorporating Video Content:** Tag the transcribed text with relevant learning objectives and integrate them into the knowledge graph as additional nodes.

#### c. **Developing the Student Dashboard:**
- **Interactive Dashboard:** Create a user-friendly interface where students can interact with the knowledge graph. This could be a web or desktop application.
- **Resource Navigation:** Implement features that allow students to easily navigate through the graph, find resources related to specific learning objectives, and access these resources directly through the application.
- **Feedback and Adaptation:** Incorporate mechanisms for students to provide feedback on resource relevance and usefulness, allowing for continuous improvement of the knowledge graph connections.


## (3) Methods for Creating Edges Between Textbook Paragraphs, Learning Objectives, Video Transcripts, and More

### 1. **Purpose**

The aim here is to develop robust methods for establishing connections (edges) between various educational resources (like textbook paragraphs and video transcripts) and learning objectives. Additionally, exploring the interconnections between different learning objectives themselves is crucial. This process is essential for building a comprehensive and interconnected knowledge graph that accurately reflects the educational content and its relevance to specific learning objectives.

### 2. **Basic Theory and Techniques**

#### a. **Cosine Similarity:**
- **Theory:** Cosine similarity measures the cosine of the angle between two non-zero vectors in a multi-dimensional space. In the context of text analysis, it is used to determine how similar two documents are linguistically.
- **Application:** Compute cosine similarity between the vectorized form of textbook paragraphs, video transcripts, and the textual description of learning objectives. High cosine similarity scores indicate a strong relationship.

#### b. **Text Classification with LLMs:**
- Despite their unreliability, small parameter LLMs can still be useful for classifying text content in relation to learning objectives. 
- **Implementation:** Fine-tune a small LLM on a dataset where the input is educational content and the output is the relevant learning objective. Use the model to predict the most relevant learning objective for new content.

#### c. **Additional Methods:**

##### i. **TF-IDF (Term Frequency-Inverse Document Frequency):**
- **Theory:** TF-IDF is a numerical statistic that reflects how important a word is to a document in a collection. It helps in understanding the relevance of words in documents.
- **Application:** Calculate TF-IDF scores for words in educational content and compare them with the words in learning objectives. High TF-IDF scores in both indicate a stronger connection.

##### ii. **Topic Modeling (e.g., LDA - Latent Dirichlet Allocation):**
- **Theory:** Topic modeling identifies topics in a set of documents. LDA assumes that documents are mixtures of topics and topics are mixtures of words.
- **Application:** Use LDA to identify the main topics in educational materials and match them with the topics associated with learning objectives.
- **Resources:** The curious individual can read a brief history about LDA [here](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation). The technically curious individual can read the original paper which discusses the application of LDA to machine learning [here](https://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf).

##### iii. **Semantic Analysis with NLP Tools (e.g., SpaCy, NLTK):**
- **Theory:** Semantic analysis involves understanding the meaning and interpretation of words and sentences.
- **Application:** Use NLP tools for deep linguistic analysis to understand the context and meaning of educational content and match it with learning objectives.

##### iv. **Entity Recognition and Linking:**
- **Theory:** Recognizing named entities (like specific scientific concepts or historical events) in text and linking them to learning objectives.
- **Application:** Use named entity recognition (NER) to tag entities in educational content and link them to related learning objectives.

### 3. **Implementation**

#### a. **Data Preparation:**
- Gather and preprocess all educational content and learning objectives. This involves text normalization (like lowercasing, removing punctuation), and possibly segmenting content into manageable units.

#### b. **Feature Extraction:**
- Apply the chosen techniques (cosine similarity, TF-IDF, etc.) to extract features from the educational content that can be used to establish connections.

#### c. **Graph Construction:**
- Use NetworkX or a similar tool to create a graph where nodes represent educational content and learning objectives.
- Add edges based on the similarity scores or classification results obtained from the above methods.

#### d. **Inter-Objective Connections:**
- To explore connections between different learning objectives, analyze the content linked to each objective and identify common or related themes using the aforementioned methods.

#### e. **Evaluation and Refinement:**
- Continuously evaluate the accuracy and relevance of the connections in the knowledge graph.
- Refine the graph construction methods based on feedback and iterative testing.

## (4) Incorporating RAG with the Knowledge Graph and Its Potential Benefits

### 1. **Purpose**

The goal of integrating a Retrieval-Augmented Generation (RAG) model with the knowledge graph is to enhance the capability of the automated teaching assistant in generating more accurate and contextually relevant educational content, such as multiple-choice questions, free-response questions, and responses to student inquiries. This integration aims to leverage the vast information stored in the knowledge graph to inform and improve the generation capabilities of the RAG model.

### 2. **Basic Theory and Techniques**

#### a. **Understanding RAG:**
- **Theory:** RAG combines the powers of two major components: a retrieval system and a generator (usually a language model). The retrieval system first fetches relevant documents or information snippets based on the input query. The generator then uses this retrieved information to produce a coherent and contextually relevant output.
- **Application in Education:** In the context of an automated teaching assistant, RAG can be used to generate educational content that is not only linguistically accurate but also contextually aligned with the curriculum and learning objectives.

#### b. **Integrating with Knowledge Graph:**
- The knowledge graph, which includes relationships between educational resources and learning objectives, can serve as the retrieval source for the RAG model. When a query (like a student question) is input into the system, the RAG model can use the graph to retrieve the most relevant educational content before generating a response.

#### c. **Fine-Tuning for Specific Tasks:**
- Fine-tuning a RAG model on specific educational tasks can significantly enhance its performance. This involves training the model on datasets that are representative of the types of questions and content it will encounter in the educational setting.
- **Tasks like Generating Multiple Choice Questions:** Train the RAG model on a dataset comprising of educational material and corresponding multiple-choice questions.
- **Free Response Questions and Student Queries:** Similarly, fine-tune the RAG model on datasets that include free-response questions and a wide variety of student questions and answers.

### 3. **Implementation**

#### a. **Setting Up RAG with the Knowledge Graph:**
- **Integration:** Develop a system where the RAG model can query the knowledge graph. This involves creating APIs or interfaces that allow the model to access and retrieve information from the graph.
- **Retrieval Mechanism:** Ensure that the retrieval component of the RAG model is effectively tuned to extract the most relevant nodes (educational content) from the knowledge graph based on the input query.

#### b. **Fine-Tuning Process:**
- **Dataset Preparation:** Collect and prepare datasets that are representative of the educational context in which the RAG model will operate. This includes a variety of question types and subject matter content.
- **Training:** Use these datasets to fine-tune the model, ensuring it learns to generate responses that are not only accurate but also pedagogically relevant.

#### c. **Potential Benefits:**
- **Improved Accuracy and Relevance:** By leveraging the knowledge graph, the RAG model can generate responses that are more aligned with the educational content and objectives.
- **Customized Learning Experience:** Fine-tuning the model on specific educational tasks allows for the generation of content that is tailored to the needs of the classroom and individual students.
- **Efficiency in Content Creation:** Automating the generation of quiz questions and responses to student inquiries can save educators significant time and effort.

#### d. **Evaluation and Refinement:**
- Continuously monitor and evaluate the performance of the RAG model in generating educational content.
- Refine the integration with the knowledge graph and the fine-tuning process based on feedback and observed results.

