# oreilly_api
[interview-exercise-cloud](https://github.com/oreillymedia/interview-exercise-cloud)

`docker/`

* Contains [`Dockerfile`](docker/Dockerfile), [`requirements.txt`](docker/requirements.txt) and the Python Flask app ([`api.py`](docker/api/api.py)) used to generate the docker image [`jrussell/api:latest`](https://hub.docker.com/r/jrussell/api)

`kubernetes/`

* Contains [`api.yaml`](kubernetes/api.yaml) manifest for deploying the cluster

# Deploy to kubernetes
`kubectl apply -f kubernetes/api.yaml`
- Creates 2 pods - one for API and one for DB
- API will be available on `localhost:30088`

# API
**All responses are `application/json`**

`localhost:30088`
- `/`
    - Get all works
- `/works/<work_id>`
    - Get work by `work_id`
- `/isbn/<isbn>`
    - Get work by `isbn`
- `/titles/<title>`
    * Get works matching `title` _(Case-insensitive)_
- `/authors/<author>`
    * Get works matching `author` _(Case-insensitive)_