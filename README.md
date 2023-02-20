# oreilly_api
interview-exercise-cloud

`docker/`

* Contains Dockerfile, requirements.txt and the Python Flask app used to generate the docker image `jrussell/api:latest`

`kubernetes/`

* Contains `api.yaml` manifest for deploying the cluster

# Deploy to kubernetes
`kubectl apply -f kubernetes/api.yaml`
- Creates 2 pods - one for api and one for db
- Api will be available on `localhost:30088`

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
    * Get works matching `title` (Case-insensitive)
- `/authors/<author>`
    * Get works matching `author` (Case-insensitive)