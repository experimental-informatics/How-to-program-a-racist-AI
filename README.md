Notebooks from the Seminar:

# How to program a racist AI < SoSe22 








Georg Trogemann, Christian Heck, Ting Chun Liu

Compact Seminar

Compact seminar 30.05. – 03.06.2022 

Filzengraben 8 – 10, 0.2 [ ] ground zero, Academy of Media Arts Cologne

[Experimental Informatics](https://en.khm.de/exMedia_experimentelle_informatik/)

Academy of Media Arts Cologne

Email: g.trogemann@khm.de, c.heck@khm.de, t.liu@khm.de

### Description

Five years ago, the Google Research Team together with some Google Brain authors published the Transformer Architectures approach under the headline „Attention Is All You Need“. And since then, these Large Language Models (LLM) have also attracted attention. For the past 2 years, they have been at the center of social debates about discriminatory tendencies in AI language models. Even if racism is not explicitly or intentionally inscribed in these machine learning methods, they generate expressions in use that are difficult to predict, ranging from subtle everyday discrimination to agitation on the web, and thus also contribute to acts of racist violence on the streets.

Introduction to Programming Artificially Intelligent Racists is based on the Python programming language. „How to program a racist AI“ is a continuation of the seminar „Human Machine Readable – Introduction to Programming“ from the winter semester. However, participation in the WS is not a prerequisite. The seminar is open to anyone with previous programming experience (in any language). We will take a closer look at three areas of programming: 1. the Transformer model architecture, 2. the training data, and 3. the pre-processing of the respective data sets. The goal of the seminar is that at the end each student understands the basics of various biases in AI language models and is able to code their own communication guerrilla hate speech bot.

## Course

### Hands on Python
<!--
[Python: Variables](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_variables.ipynb)

[Python: Loops & Lists](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_loops_lists.ipynb)

[Python: Booleans, If - Else, While-loop](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_booleans_conditionals.ipynb)

[Python: Strings, Files, Try & Except](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_strings_files_try.ipynb)

[Python: Functions](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_functions.ipynb)

[Python: Modules](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_modules_pypi.ipynb)

[Python: Tuples, Dictionaries, Set](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_tuples_dictionaries_set.ipynb)

[Python: Class / OOP](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/python_class.ipynb)
-->

### Hands on Tokenizers

### Hands on Datasets

### Hands on Transformers
<!--
#### Hands on Datasets

[dataset-list](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/dataset-list.md) < some resources of datasets & archives

[scrape-load_textcorpora](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/scrape-load_textcorpora.ipynb) < some basic examples and code-snippets to srape, load and walk through datasets

[scraper_wikipedia](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/scraper_wikipedia.ipynb) < extract text of specific wikipedia articles

[clean_datasets](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/clean-token-read.ipynb)

[clean_multiple_files](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/clean_multiple_files.ipynb) < define a function to clean text and apply it to multiple files

[extract_with_pdfplumber](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/extract_with_pdfplumber.ipynb) < extract text from a pdf and remove unwanted parts/ characters


#### Coding books with Python

[First book](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_1.ipynb)

[Programmed books 2](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_2.ipynb)

[Programmed books 3](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_3.ipynb)

[Programmed books 4](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/books_4.ipynb)

---

## Week 2 (7.2. - 11.2.)

### Hands on Text as Data

[0-order text generation](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/0-order_text_generation.ipynb) < random word generation, wiederholung von Char, String and List 

[Data cleaning and Parsing](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Data_cleaning_and_Parsing.ipynb) < python method for parsing text as data

[1-order text generation and Probability](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/1-order_text_generation.ipynb) < probability calculation

### Hands on Markov Chain

[Markov Chain - Background and knowledge](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Markov_Chain_0_Background_and_knowledge.ipynb) < basic knowledge of Markov chain

[Markov Chain - Basic (Second Order Text Generation](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Markov_Chain_1_Basic_Second_Order.ipynb) < Basic usage of Markov chain with second order text generation.

[Markov Chain - N-order Text Generation](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Markov_Chain_2_N-order_Text_Generation.ipynb) < N-Order text generation.

[Markov Chain - OOP](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Markov_Chain_3_Class.ipynb) < Markov Chain based on object oriented programming.

[Markov Chain - Markovify-library](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Markov_Chain_Markovify_Library.ipynb) < Markov Chain based on github repo https://github.com/jsvine/markovify

[Additional - Markov Chain with Image](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/02_Markov-Chain/Markov_Chain_Image.ipynb) Image Generation based on Markov Chain

### Hands on Artificial Neural Networks (ANN)

[ANN-in-Keras.ipynb](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/03_ANN/Keras-ANN.ipynb) < Dense Neural Network with Keras

\+ working with [Copilot](https://copilot.github.com/)

### Hands on Recurrent Neural Networks (RNN) / Long Short Term Memory (LSTM) Networks

[Text generation with LSTM](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/03_RNN/LSTM-Textgenerator.ipynb) < Text generation with RNN/LSTM

### Hands on GPT-?

[HuggingFace Pipeline](https://github.com/experimental-informatics/how-to-make-human-machine-readable/tree/master/04_GPT/huggingface-pipeline) < the HuggingFace way to use state-of-the-art NLP-models for inference

[aitextgen](https://github.com/experimental-informatics/how-to-make-human-machine-readable/tree/master/04_GPT/aitextgen) < Python tool for text-based AI training and generation using GPT-2
-->
---

### General Info 
#### Hands on Jupyter Notebooks

- [Introduction](https://github.com/experimental-informatics/how-to-make-human-machine-readable/blob/master/00_General-introductions/Introduction.ipynb)

- *You can run, execute and work on the Notebooks in typing following button:* [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/experimental-informatics/How-to-program-a-racist-AI/HEAD)

#### Cheat Sheets

| Title                       | URL                                                          |
| --------------------------- | ------------------------------------------------------------ |
| Python Beginner Cheat Sheet | https://github.com/ehmatthes/pcc/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf |
| Markdown Syntax             | https://help.github.com/articles/basic-writing-and-formatting-syntax/ |
| Jupyter Notebook            | https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/ |
| Conda                       | https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf |

---

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/experimental-informatics/How-to-program-a-racist-AI/HEAD)
