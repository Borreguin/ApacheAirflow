# APACHE AIRFLOW DOCKER

This docker needs more than 4 GB RAM.

This project follows some tutorials:
- [Deploy Airflow in Docker](https://www.youtube.com/watch?v=aTaytcxy2Ck&ab_channel=DatawithMarc)
- [Create a DAG](https://www.youtube.com/watch?v=IH1-0hwFZRQ&ab_channel=DatawithMarc)
- [Connect with Postgres DB](https://www.youtube.com/watch?v=S1eapG6gjLU&ab_channel=coder2j)

Here a summary of instructions:

1. Create folders:  mkdir ./dags ./plugins ./logs 
2. Create .env file to give permissions: echo -e "AIRFLOW_UID=$(id -u) \nAIRFLOW_GID=0" > .env
3. Run the docker container: docker-compose up airflow-init
4. Once the airflow user was created then run: docker-compose up