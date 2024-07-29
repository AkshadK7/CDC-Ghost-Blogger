## How to Run the Application


### Create a new external network

docker network create redis-ghost-blogger_ghost-network



### Build the Docker Containers

docker compose up --build



        ### Open a new terminal and type :

        `` docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest ``

        [Documentation](https://redis.io/docs/getting-started/install-stack/docker/#connect-with-redis-cli)


        ### Open a new terminal and type :

        `` pip install -r requirements.txt ``


        ### Open a new split terminal and type :

        Initiate Backend :
        `` uvicorn backend:app --reload ``

        Initiate Frontend :
        `` streamlit run frontend.py ``

        ### Local Ports Information :

        Frontend : http://localhost:8000/
        Backend : (host='localhost', port=6379, db=0)


### Test Redis DB 
docker ps 
docker exec -it <container-id> redis-cli


Copyright &copy; 2024 Akshad Kolhatkar. All rights reserved.