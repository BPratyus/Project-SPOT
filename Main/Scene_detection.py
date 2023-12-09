
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
# import sklearn
# print(sklearn.__version__)
vectorizer=joblib.load('vectorizer.pkl')
# Load the pickled joblib object
model = joblib.load('indoor_scene_recognition_model.pkl')

# user_input = "chair bird cat"
def detect_scene(object_labels):

    # Preprocess and vectorize the input
    user_input_tfidf = vectorizer.transform(object_labels)
    # Use the pickled joblib object
    prediction = model.predict(user_input_tfidf)

    return prediction[0]
