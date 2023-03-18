# For coding assignment purpose.

## Simple CRUD APIs
#### No middlewares, security, logging, validations(except email) handled.

### Requirements
- Docker and docker-compose `apt install docker.io docker-compose`
- Make sure 8888 and 3306 ports are not in use.

### Run 
1. Env & run containers: `./setup.sh` 
2. Migration: `docker exec -it api alembic upgrade head`

Ping to validate setup is done correctly: 
```curl
curl -X 'GET'  'http://0.0.0.0:8888/' -H 'accept: application/json'
```

### URLs
- Documentation: http://0.0.0.0:8888/documentation
- Re-Documentation: http://0.0.0.0:8888/re-documentation
- Openapi.json: http://0.0.0.0:8888/openapi.json

### Demo
Containers<br><img src="demo/containers.png" width="400"><br>
Docs<br><img src="demo/doc.png" width="250"><br>
Structure<br><img src="demo/structure.png" width="250"><br>
#### Postman APIs:
1. Get all<br><img src="demo/get_all.png" width="250">
2. Get one<br><img src="demo/get_one.png" width="250">
3. Create new<br><img src="demo/create_new.png" width="250">
4. Update one<br><img src="demo/update_one.png" width="250">
5. Delete one<br><img src="demo/delete_one.png" width="250">

