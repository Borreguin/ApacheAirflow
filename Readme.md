# APACHE AIRFLOW DOCKER

This docker needs more than 4 GB RAM.

1. Create folders:  mkdir ./dags ./plugins ./logs 
2. Create .env file to give permissions: echo -e "AIRFLOW_UID=$(id -u) \nAIRFLOW_GID=0" > .env
3. Run the docker container: docker-compose up airflow-init
4. Once the airflow user was created the run: docker-compose up