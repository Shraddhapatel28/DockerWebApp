from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return """
    <html>
    <head>
        <title>About Us</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class="text-center p-5 bg-light">
        <div class="container">
            <h1 class="text-primary">About This Project</h1>
            <p class="lead mt-3">This project demonstrates Containerization of a Web Application using Docker.</p>
            <p>It was created by <strong>Shraddha</strong> and <strong>Gulshan</strong> for DevOps learning purposes.</p>
            <a href="/" class="btn btn-dark mt-3">⬅ Back to Home</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
