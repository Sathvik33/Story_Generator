---
# Personalized Story Generator ✍️
---
### Project Overview
This is a web application that generates unique, creative short stories based on user-provided inputs. The project is built from scratch to demonstrate the power of modern **Large Language Models (LLMs)** and how they can be integrated into interactive applications.

It uses an advanced, instruction-finetuned model to turn simple user prompts into coherent narratives. 
---
### Features
* **Customizable Storytelling:** Users can influence the story by specifying a **Genre**, **Theme**, **Main Character**, and **Location**.
* **Intelligent Text Generation:** The core is built on the **FLAN-T5** language model, known for its strong performance on a variety of text-based tasks.
* **Simple User Interface:** A clean, intuitive interface powered by Streamlit makes it easy for anyone to generate a story with a single click.
* **Long-form Generation:** The model is specifically configured to generate longer, more detailed stories (10-50 lines) by adjusting key parameters.
* **User-Friendly Experience:** Includes a custom loading message to improve the user experience during the model's generation process.
---
### How It's Built
This project was built from scratch using three main components:

* **Streamlit** is the web framework used to create the user interface. It allows for rapid development of data applications in pure Python.
* **Hugging Face Transformers** is the library that provides access to the pre-trained `google/flan-t5-large` model. It handles the complex process of downloading, loading, and running the model.
* **`google/flan-t5-large`** is the specific **language model** used for the text generation. It was chosen for its fine-tuned ability to follow instructions, which is crucial for generating stories that adhere to the user's input.

The application works by taking user inputs from the Streamlit UI, formatting them into a specific instruction-based **prompt** (e.g., "Generate a story with the following genre..."), and then passing that prompt to the FLAN-T5 model. The model processes the prompt and returns the generated story as a text string, which is then displayed back to the user.
---
### Getting Started
Follow these steps to set up and run the Story Generator on your local machine.

#### Prerequisites
* Python 3.8 or higher.
* `pip` package manager.

#### Installation
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    (Replace `your-username/your-repo-name` with your actual repository details).
2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
#### Usage
1.  **Run the Streamlit application** from your terminal:
    ```bash
    streamlit run app.py
    ```
2.  Your web browser should automatically open to the application's URL (usually `http://localhost:8501`).
3.  Use the sidebar to input your desired story details and click the **"Generate Story"** button to see the output.
---
### Known Issues
* **Initial Load Time:** The first time you run the application, it will download the `flan-t5-large` model, which is a large file (approx. 3 GB). This may take several minutes depending on your internet connection. Subsequent runs will be much faster as the model is cached.
* **Story Length Variability:** While the model is configured to generate longer stories, it may sometimes produce shorter outputs if it determines the narrative is complete.
* **Citations:** The model may occasionally include irrelevant citation links at the end of a story. These are automatically cleaned from the final output.
---
### Contact
If you have any questions or feedback, feel free to reach out.

* **Your Name** - [Your Email/LinkedIn/GitHub Profile]
---
