# Email/SMS Spam Classifier

## Overview
This project is a **machine learning-based spam classifier** that can identify whether a given email or SMS message is spam or not. It is built using **Python, Streamlit, and Scikit-learn** and is deployed on **Render** for easy access.

## Features
- **Text Preprocessing:** Tokenization, stopword removal, stemming, and vectorization using TF-IDF.
- **Machine Learning Model:** Uses **Multinomial Naive Bayes (MNB)** for classification.
- **High Accuracy:** Achieves **97% accuracy** with **100% precision** for spam detection.
- **Interactive UI:** Developed with **Streamlit** for a user-friendly experience.
- **Live Deployment:** Hosted on **Render** for public access.

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning:** Scikit-learn, NLTK
- **Deployment:** Render

## How It Works
1. User enters an email/SMS message in the input field.
2. The text undergoes preprocessing: lowercasing, tokenization, stopword removal, stemming.
3. The cleaned text is transformed into a numerical format using **TF-IDF vectorization**.
4. The trained **Multinomial Naive Bayes** model predicts whether the message is spam or not.
5. The result is displayed on the UI.

## Installation & Setup
To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-classifier.git
   cd spam-classifier
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run spam_app.py
   ```

## Deployment
The project is deployed on Render. To deploy your own:
1. Push the code to GitHub.
2. Connect the GitHub repo to **Render**.
3. Set the start command:
   ```bash
   streamlit run spam_app.py --server.port 10000 --server.address 0.0.0.0
   ```
4. Deploy!
5. Website :- https://email-sms-spam-ham-classifier.onrender.com/

## Future Enhancements
- Add **deep learning** models for better performance.
- Implement **real-time email filtering**.
- Integrate with **Twilio API** for SMS filtering.

## Author
Developed by Darshan K Jain 🚀

## License
MIT License

