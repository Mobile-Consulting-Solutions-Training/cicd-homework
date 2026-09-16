from fastapi import FastAPI

app = FastAPI()

VERSION = "2.0.0"


@app.get("/")
def home():
    return {
        "application": "CI/CD Homework",
        "version": VERSION
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
