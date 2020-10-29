# docker-flask-anagram
Simple Containerized Flask App for Retrieving Anagrams

## Clone the Repository

```bash
> git clone https://github.com/jacobeturpin/docker-flask-anagram.git
> cd docker-flask-anagram
```

# Build and Run the Container

```bash
> docker build -t docker-flask-anagram .
> docker run -d -p 5000:5000 docker-flask-anagram
```

# Test the Service
```bash
> curl http://localhost:5000/anagram/spare
  ["apers","apres","asper","pares","parse","pears","prase","presa","rapes","reaps","repas","spaer","spare","spear"]
```