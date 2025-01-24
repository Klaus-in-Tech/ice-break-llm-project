# Ice Breaker Project

This project is designed to scrape LinkedIn profiles and generate ice breaker summaries using the LangChain and Ollama APIs.

## Features

- Scrape LinkedIn profiles for detailed information.
- Generate summaries and interesting facts about individuals.
- Utilize LangChain and Ollama for natural language processing.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Klaus-in-Tech/ice-break-llm-project.git
    cd ice_breaker
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
     # On Windows use `venv\Scripts\activate`
    ```


3. Create a `.env` file in the root directory and add your API keys:
    ```env
    PROXYCURL_API_KEY=<your_proxycurl_api_key>
    LANGCHAIN_API_KEY=<your_langchain_api_key>
    ```

## Usage

To run the project, use the following command:
```sh
python ice_breaker.py
```

## Example

The script will scrape the LinkedIn profile of "Kakooza Allan Klaus" and generate a summary. You can change the name in the `ice_breaker_with` function call in `ice_breaker.py`.

## Files

- `ice_breaker.py`: Main script to run the ice breaker generation.
- `linkedin.py`: Contains the function to scrape LinkedIn profiles.
- `twitter.py`: (Commented out) Contains the function to scrape Twitter profiles.

## License

This project is licensed under the MIT License.