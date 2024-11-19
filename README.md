# Gemini AI-Powered Applications

## Table of Contents
1. [Project Title](#project-title)
2. [Project Description](#project-description)
3. [Key Features](#key-features)
4. [Tech Stack](#tech-stack)
5. [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation Steps](#installation-steps)
6. [Usage](#usage)
    - [Text Generation App](#text-generation-app)
    - [Image Demonstrator App](#image-demonstrator-app)
7. [File Structure](#file-structure)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)
10. [Contributors](#contributors)
11. [Acknowledgments](#acknowledgments)

---

## Project Title
**AI-Powered Q&A and Image Understanding Applications**

---

## Project Description
This repository contains two AI-powered applications built using **Google's Gemini AI models** and **Streamlit**. The applications provide the following functionalities:
1. **Text Generation App**: A question-answering interface to generate meaningful content for user queries.
2. **Image Demonstrator App**: An AI-powered tool to analyze uploaded images and provide detailed descriptions or insights.

Both apps are user-friendly, leveraging the power of Google Gemini models for advanced generative capabilities.

---

## Key Features
### Text Generation App
- Powered by **Gemini Pro** for content generation.
- Simple interface to input questions and receive answers.

### Image Demonstrator App
- Uses **Gemini 1.5 Flash** for image understanding.
- Accepts user-uploaded images and provides insights or descriptions.
- Supports input prompts for image-contextualized answers.

---

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **AI Models**: Google Gemini AI
- **Libraries**:
  - `Pillow` (for image handling)
  - `dotenv` (for managing API keys)

---

## Setup Instructions

### Prerequisites
1. Install Python 3.8 or later.
2. Obtain a **Google API Key** for Gemini AI models.
3. Ensure the following Python libraries are installed:
   - `streamlit`
   - `google-generativeai`
   - `Pillow`
   - `python-dotenv`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/gemini-ai-apps.git
   cd gemini-ai-apps
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

4. Run the applications:
   - **Text Generation App**:
     ```bash
     streamlit run app.py
     ```
   - **Image Demonstrator App**:
     ```bash
     streamlit run vision.py
     ```

---

## Usage

### Text Generation App
1. Run the app:
   ```bash
   streamlit run app.py
   ```
2. Enter a question or prompt in the input box.
3. Click "Ask any question you wish to know."
4. View the generated response in the output section.

### Image Demonstrator App
1. Run the app:
   ```bash
   streamlit run vision.py
   ```
2. Upload an image (JPG, JPEG, or PNG).
3. Optionally, enter a prompt to contextualize the image analysis.
4. Click "Tell me about the image."
5. View the AI-generated insights in the output section.

---

## File Structure
```
├── app.py                # Text Generation App
├── vision.py             # Image Demonstrator App
├── requirements.txt      # Required libraries
├── .env                  # Environment variables (Google API Key)
├── README.md             # Project documentation
```

---

## Future Enhancements
1. **Multilingual Support**: Enable text and image analysis in multiple languages.
2. **Advanced Image Features**: Add object detection and segmentation capabilities.
3. **UI Improvements**: Enhance the interface for a more interactive experience.

---

## Contributors

- **Rishikesh**  
- LinkedIn: www.linkedin.com/in/rishikesh-a12090285
- Email: rishikesh23@kgpian.iitkgp.ac.in

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
