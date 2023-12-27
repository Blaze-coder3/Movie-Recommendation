from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Load the merged data
df = pd.read_csv(r'C:\Users\syedk\Downloads\Bharat-Intern\Movie Recommendation\merged_data.csv')

# TF-IDF Vectorization for movie overview
tfidf = TfidfVectorizer(stop_words='english')
df['overview'] = df['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['overview'])

# Compute the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        
        if title not in df['original_title'].values:
            return render_template('index.html', error="Movie not found! Please try again.")
        
        idx = df[df['original_title'] == title].index[0]
        
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [i[0] for i in sim_scores]
        
        return render_template('index.html', title=title, recommendations=df['original_title'].iloc[movie_indices].values)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
