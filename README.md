# email-sms-spam-classifier
This project is a machine learning-based spam classifier that detects whether an email or SMS is Spam or Not Spam using Natural Language Processing (NLP) and Multinomial Naïve Bayes.
Features
Text Preprocessing – Removes stopwords, punctuation, and applies stemming
TF-IDF Vectorization – Converts text into numerical features
Multinomial Naïve Bayes Classifier – Achieves high accuracy in spam detection
Streamlit UI – Interactive web app for real-time classification
Installation & Usage
Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/spam-classifier.git
cd spam-classifier
Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:
bash
Copy
Edit
streamlit run spam_app.py
Enter a message and check if it’s Spam or Not Spam!
Technologies Used
🔹 Python, NLTK, Scikit-learn, Pandas, NumPy
🔹 Machine Learning (Multinomial Naïve Bayes)
🔹 Streamlit for UI
