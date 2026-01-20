# MongoDB

In this lecture we'll get into the introcutions of MongoDB a NoSQL database, or more precisely a document database. It is useful for handling semi-structured data. However MongoDB also has SQL and also a schema validation if needing to be more strict in the schema and handling more structured data.

<a href="https://youtu.be/1y8o9UOvcNg" target="_blank">
  <img src="https://github.com/kokchun/assets/blob/main/data_modeling/mongodb.png?raw=true" alt="mongodb" width="600">
</a>

> [!Note]
> - CORRECTION TO THE VIDEO: due to a latest MONGODB version, there should be two additional environment variables for `mongo-express` container under `docker-compose.yml` to set the credentials for logging into the UI:
>```cmd
>ME_CONFIG_BASICAUTH_USERNAME: ${MONGO_USER}
>ME_CONFIG_BASICAUTH_PASSWORD: ${MONGO_PASSWORD}


## Local setup using docker compose

Copy the docker-compose.yaml file from this lecture and run `docker compose up -d` to spin up mongodb and mongo-express containers. To see the UI, go into the [http://localhost:8081/](http://localhost:8081/). mongo-express here is a UI for mongodb database.

> [!NOTE]
> this setup is for local mongodb setup using docker. There is also a cloud version which offers a free version but for more storage and features there are several paid versions available. Also there is community version that can be installed if not wanting to use docker.

To access mongodb container do `docker exec -it mongodb bash`. Then you have

## Other videos 📹

- [MongoDB crash course - Traversy Media (2022)](https://www.youtube.com/watch?v=2QQGWYe7IDU&list=PL4RCxklHWZ9shwyfN0KT1KiOX6OOkNJaq&index=9)
- [mongodb + mongo express docker compose never been this easy in less than 10 mins - medium guy (2024)](https://www.youtube.com/watch?v=rPi9yPtlHYw)

## Read more 👓

- [Mongodb homepage](https://www.mongodb.com/)
- [pymongo docs](https://pymongo.readthedocs.io/en/stable/)
