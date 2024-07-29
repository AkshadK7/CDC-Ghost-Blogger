from fastapi import FastAPI
from pydantic import BaseModel
from redis import Redis
from redisearch import Client, TextField, NumericField, Query
import json
from datetime import datetime
import random
import os

# Get Redis configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))

app = FastAPI()

# Redis connection
redis = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# Defining the index name
index_name = 'blog_index'

redisearch_client = Client(index_name, conn=redis)

try:
    redisearch_client.info()
except:
    # Index does not exist. We need to create it!
    redisearch_client.create_index([
        NumericField('id'),
        TextField('title', weight=5.0),
        TextField('content'),
        TextField('author'),
        NumericField('timestamp')
    ])

# Model for blog post
class BlogPost(BaseModel):
    title: str
    content: str
    author: str

# Add Post
@app.post("/add_post")
def add_post(post: BlogPost):
    timestamp = int(datetime.now().timestamp())
    id = int(random.randint(100, 10000))
    post_dict = post.dict()
    post_dict["timestamp"] = timestamp
    post_dict["id"] = id

    redis.hset("posts", timestamp, json.dumps(post_dict))

    redisearch_client.add_document(timestamp, id=id, title=post.title, content=post.content, author=post.author, timestamp=timestamp)
    return {"message": "Post added successfully"}

# Read Post
@app.get("/read_post/{title}")
def read_post(title: str):
    search_results = redisearch_client.search(Query(f"@title:{title}"))
    if len(search_results.docs) == 0:
        return {"message": "Post not found"}
    post_id = int(search_results.docs[0].id)
    post_json = redis.hget("posts", post_id)
    if not post_json:
        return {"message": "Post not found"}
    post_dict = json.loads(post_json)
    return post_dict

# Read All Posts
@app.get("/read_all_posts")
def read_all_posts():
    posts_json = redis.hvals("posts")
    posts = [json.loads(post_json) for post_json in posts_json]
    return posts

# Update Post
@app.put("/update_post/{title}")
def update_post(title: str, post: BlogPost):
    search_results = redisearch_client.search(Query(f"@title:{title}"))
    if len(search_results.docs) == 0:
        return {"message": "Post not found"}
    post_id = int(search_results.docs[0].id)
    post_dict = post.dict()
    post_dict["timestamp"] = int(datetime.now().timestamp())
    redis.hset("posts", post_id, json.dumps(post_dict))
    redisearch_client.add_document(post_id, title=post.title, content=post.content, author=post.author, timestamp=post.timestamp)
    return {"message": "Post updated successfully"}

# Delete Post
@app.delete("/delete_post/{title}")
def delete_post(title: str):
    search_results = redisearch_client.search(Query(f"@title:{title}"))
    if len(search_results.docs) == 0:
        return {"message": "Post not found"}
    post_id = int(search_results.docs[0].id)
    redis.hdel("posts", post_id)
    redisearch_client.delete_document(post_id)
    return {"message": "Post deleted successfully"}

# Search Post
@app.get("/search_post")
def search_post(query: str):
    search_results = redisearch_client.search(Query(query))
    posts = []
    for result in search_results.docs:
        post_id = int(result.id)
        post_json = redis.hget("posts", post_id)
        if post_json:
            post_dict = json.loads(post_json)
            posts.append(post_dict)
    return posts
