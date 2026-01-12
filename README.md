# 🎬 Movie Recommender System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A sophisticated content-based movie recommendation system that helps you discover your next favorite film based on your viewing preferences.

[Features](#features) • [Demo](#demo) • [Installation](#installation) • [Usage](#usage) • [Tech Stack](#tech-stack)

</div>

---

## 📋 Overview

This Movie Recommender System leverages machine learning algorithms to provide personalized movie recommendations. By analyzing movie similarities based on various features, the system suggests five movies that closely match your selected film's characteristics.

## ✨ Features

- **🎯 Intelligent Recommendations**: Get 5 highly relevant movie suggestions based on content similarity
- **🖼️ Visual Interface**: Browse recommendations with movie posters fetched from TMDB API
- **⚡ Fast Performance**: Pre-computed similarity matrix ensures instant recommendations
- **🎨 User-Friendly UI**: Built with Streamlit for an intuitive and responsive experience
- **📊 Large Movie Database**: Access to thousands of movies for diverse recommendations

## 🎥 Demo

The application presents a clean interface where users can:

1. Select a movie they recently watched from the dropdown
2. Click the "Recommend" button
3. Instantly view 5 similar movies with their posters

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Movie Recommender"
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure data files are present**
   
   Make sure the following pickle files are in the project directory:
   - `movies.pkl` - Contains movie dataset
   - `similarity.pkl` - Pre-computed similarity matrix

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the application**
   
   Open your browser and navigate to `http://localhost:8501`

## 💻 Usage

1. Launch the application using the command above
2. Select a movie from the dropdown menu that you've recently watched
3. Click the "Recommend" button
4. Browse through the 5 recommended movies displayed with their posters
5. Explore new recommendations by selecting different movies

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web framework for the UI |
| **Pandas** | Data manipulation and analysis |
| **Scikit-learn** | Machine learning algorithms (similarity computation) |
| **Pickle** | Model and data serialization |
| **TMDB API** | Fetching movie posters and metadata |
| **Requests** | HTTP library for API calls |

## 📁 Project Structure

```
Movie Recommender/
│
├── app.py              # Main application file
├── movies.pkl          # Serialized movie dataset
├── similarity.pkl      # Pre-computed similarity matrix
├── requirements.txt    # Python dependencies
├── Procfile           # Deployment configuration
├── setup.sh           # Setup script for deployment
└── README.md          # Project documentation
```

## 🔧 How It Works

### Content-Based Filtering

The recommendation system uses **content-based filtering** approach:

1. **Feature Extraction**: Movies are represented by their features (genre, cast, director, keywords, etc.)
2. **Similarity Computation**: Cosine similarity is calculated between all movies
3. **Recommendation Generation**: When a user selects a movie, the system finds the 5 most similar movies based on pre-computed similarity scores
4. **Visual Presentation**: Movie posters are fetched from TMDB API for enhanced user experience

### Algorithm Flow

```
User Selection → Find Movie Index → Retrieve Similarity Scores 
→ Sort by Similarity → Select Top 5 → Fetch Posters → Display Results
```

## 🌐 Deployment

This application is deployment-ready with included configuration files:

- **Procfile**: For Heroku deployment
- **setup.sh**: Environment setup script

### Deploy to Heroku

```bash
heroku login
heroku create your-app-name
git push heroku main
```

## 🔑 API Configuration

The application uses TMDB (The Movie Database) API for fetching movie posters. The API key is currently hardcoded in the application. For production use:

1. Register at [TMDB](https://www.themoviedb.org/settings/api)
2. Get your API key
3. Replace the API key in `app.py` or use environment variables

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 Future Enhancements

- [ ] Add user ratings and collaborative filtering
- [ ] Implement advanced filtering (by genre, year, rating)
- [ ] Add movie trailers and detailed information
- [ ] Create user accounts and watchlists
- [ ] Implement hybrid recommendation approach
- [ ] Add movie search functionality
- [ ] Mobile-responsive design improvements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the movie database API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- The open-source community for inspiration and tools

## 📧 Contact

For questions, suggestions, or collaboration opportunities, feel free to reach out!

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ and Python

</div>