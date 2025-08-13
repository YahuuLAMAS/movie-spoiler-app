# Movie Spoiler Detector

A web application that detects spoilers in movie comments and hides them behind a white overlay so users can reveal them only if they want.

## Features
- Flask backend
- Simple spoiler detection (keyword-based for now, can be upgraded to ML)
- Frontend overlay for spoiler hiding/revealing

## Project Structure
movie-spoiler-detector/
├── app.py
├── spoiler_model.py
├── movie_spoilers.csv
├── requirements.txt
├── static/
│ └── index.html
└── models/ (optional - trained ML model)

## Installation & Usage
1. Clone this repository:
    ```
    git clone https://github.com/YahuuLAMAS/movie-spoiler-detector.git
    cd movie-spoiler-detector
    ```
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the application:
    ```
    python app.py
    ```
4. Open in browser:
    ```
    http://127.0.0.1:5000/
    ```

## Future Improvements
- Replace keyword-based detection with a trained NLP model
- Add user authentication
- Support multiple movies with different spoiler datasets
