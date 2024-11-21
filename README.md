# Job Application Bot for Seek (Australia & New Zealand)

This application is a bot designed to apply for jobs on the **Seek platform** in Australia and New Zealand. It automates job applications and is divided into different modules for ease of use. The Chrome configuration used in this application is adapted from a LinkedIn bot made by AIHawk that also automates job applications.

## Features

- **Class Separation**  
  - **`class_1.py`**: Contains the core classes and functions for the bot.  
  - **`user_config.py`**: Customize this file to set your desired job and location. Example:
    ```python
    work = "Data Analyst"
    location_user = "Australia"
    ```
  - **`cv_txt.py`**: Paste your CV in triple quotes within this file. Example:
    ```python
    cv_text = """
    Your CV text goes here...
    """
    ```

- **Dynamic Question & Answer Handling**  
  Questions and answers for applications are managed using a `try` and `except` structure. You’ll need to manually review and add them as needed to improve the bot’s versatility and expand its ability to apply for jobs across various fields.

- **OpenAI Integration**  
  Add your **OpenAI API key** in the `api_keys.py` file in the following format:
    ```python
    api_key = 'your_api_key_here'
    ```

- **Session Handling**  
  When you start the application using `main.py`, you will need to log in to your Seek account for the first run. Afterward, your session details will be cached, allowing you to skip the login step in subsequent runs unless there’s an issue.

## How to Use

1. **Clone the repository**  
   Clone the project to your local machine using the following command:
   ```bash
   git clone https://github.com/PatrichBravo/seeek-job.git

2. **Install dependencies**  
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt

3. **Configure your details**  
   - Open `user_config.py` and update it with your desired job and location:
     ```python
     work = "Data Analyst"
     location_user = "Australia"
     ```
   - Paste your CV in the `cv_txt.py` file using triple quotes:
     ```python
     cv_text = """
     Your CV text goes here...
     """
     ```
   - Add your OpenAI API key to the `api_keys.py` file:
     ```python
     api_key = 'your_api_key_here'
     ```

4. **Run the bot**  
   Start the application by running:
   ```bash
   python main.py


5. **Log in**  
   On the first run, you will need to log in to your Seek account. Once logged in, press **Enter** to proceed. Your session details will be cached for subsequent runs.

## Contribution

If you'd like to contribute to the project, feel free to reach out or create a pull request. Whether it's adding new features, improving the application, or enhancing the question-and-answer system, all contributions are welcome!

## Disclaimer

This project is created to help job seekers, including myself, streamline the job application process. Use this bot responsibly, and ensure it aligns with Seek's terms of service.

---

## File Structure

Here’s an overview of the key files in the repository:

- **`class_1.py`**: Contains classes and functions for the bot.
- **`user_config.py`**: Customize this with job details and location.
- **`cv_txt.py`**: Paste your CV here.
- **`api_keys.py`**: Add your OpenAI API key here.
- **`main.py`**: Main entry point of the application.
- **`requirements.txt`**: List of dependencies for the project.

## Example Configuration

**user_config.py**:

```python
work = "Software Engineer"
location_user = "New Zealand"
```

**cv_txt.py**:

```python
cv_text = """
[Your CV content goes here]
"""
```


**api_keys.py**:

```python
api_key = 'your_openai_api_key_here'
```

## Run the Application
Use the following command to start the bot:

```bash
python main.py
```
On the first run, log in to your Seek account when prompted. After logging in, press Enter to proceed. Your session data will be saved for future runs.

## Feedback and Support
If you have suggestions or need help, feel free to open an issue or contact me directly. Contributions to improve the bot are welcome!






