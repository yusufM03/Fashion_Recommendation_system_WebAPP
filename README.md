# Flask E-Commerce with Recommendation System

A web-based e-commerce application built with Flask, featuring a recommendation system for fashion products.

## Demo
[![Video](https://youtu.be/RX8n1z0c74I?si=K5CCQENQlpGMdCXi)](https://youtu.be/RX8n1z0c74I?si=K5CCQENQlpGMdCXi)

## Overview

This Flask-based web application provides users with a platform to browse and purchase fashion products online. The application incorporates a recommendation system that suggests fashion items based on user preferences .

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yusufM03/Fashion_Recommendation_system_WebAPP/
   ```

2. Install dependencies:
   ```bash
   cd your-repository
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```bash
   python aps.py
   ```

2. Open your web browser and navigate to `http://localhost:5000` to access the e-commerce website.

## Features


- Browse for fashion products.
- Add items to the shopping cart and calculate the total
- Integration of a recommendation system to suggest fashion products available based on user input product.


## Technologies Used

- Flask: Micro web framework for building web applications in Python.
- HTML/CSS/JavaScript: Frontend development technologies for creating the user interface and interactivity.
- TensorFlow: Machine learning library used for implementing the recommendation system.(used vgg16 as feature extraction)


## File Structure

```
├── aps.py                  # Main Flask application file
├── templates/              # HTML templates for rendering web pages
│   ├── index.html          # Homepage template
│   ├── product.html        # Product details template
│   ├── cart.html           # Shopping cart template
│   ├── Recommendation.html       # Checkout template
│  
│     
├── static/                 # Static assets (CSS, JavaScript, images)
│   ├── css/                # CSS files
│   ├── js/                 # JavaScript files
│   └── img/                # Image files
├── recommendation.py       # Feature extraction and testing the similarity
└── utils.py                # Utility functions
```

## License

This project is licensed under the [MIT License](LICENSE).



---
