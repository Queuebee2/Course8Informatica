from Course8Informatica import create_app

# Web Server Gateway Interface

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
