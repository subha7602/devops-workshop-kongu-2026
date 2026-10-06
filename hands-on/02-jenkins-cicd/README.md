# Lab 2 — Git Push → Jenkins → Local Kubernetes

Goal: see the full loop in action — you change code, push to Git, Jenkins
picks it up, builds a new Docker image, and rolls it out to the same local
Kind cluster from Lab 1. Refresh the browser and see your change live.

```
 git push  --->  Jenkins job  --->  docker build  --->  kind load  --->  kubectl apply/rollout  --->  change visible at localhost
```

## Prerequisites

- Lab 1 completed (Kind cluster `devops-workshop` running with `sample-webapp`)
- Jenkins running locally (see below)

## 1. Run Jenkins locally

Easiest path — run Jenkins itself in Docker, with access to your host's
Docker and kubectl so it can build images and talk to the Kind cluster:

```bash
docker run -d --name jenkins \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v $(which docker):/usr/bin/docker \
  -v $(which kubectl):/usr/bin/kubectl \
  -v $HOME/.kube:/root/.kube \
  jenkins/jenkins:lts
```

Open [http://localhost:8080](http://localhost:8080) and follow the setup
wizard (unlock with the password printed by
`docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`,
install suggested plugins, create an admin user).

## 2. Create the pipeline job

1. **New Item** → name it `sample-webapp-pipeline` → **Pipeline** → OK.
2. Under **Pipeline**, set **Definition** to "Pipeline script from SCM".
3. **SCM**: Git → paste this repo's URL (or local path) → branch `main`.
4. **Script Path**: `hands-on/02-jenkins-cicd/Jenkinsfile`.
5. Save.

## 3. Trigger a build

Click **Build Now**. Watch the stages run in **Stage View**:

`Checkout → Build Docker image → Load image into Kind → Deploy to Kubernetes → Verify`

## 4. See the change reflected locally

```bash
kubectl port-forward svc/sample-webapp 8080:80
# visit http://localhost:8080
```

## 5. Make a change and watch the loop again

1. Edit `hands-on/01-sample-webapp/app.py` — e.g. change the `<h1>` text.
2. Commit and push:
   ```bash
   git add hands-on/01-sample-webapp/app.py
   git commit -m "Update homepage text"
   git push
   ```
3. In Jenkins, click **Build Now** again (or set up a **Poll SCM** trigger,
   e.g. `* * * * *`, so Jenkins picks up the push automatically).
4. Once the pipeline finishes, refresh `http://localhost:8080` — your change
   is live, deployed entirely through the pipeline.

## How it works

- **Jenkinsfile** — a declarative pipeline with five stages: checkout, build
  the Docker image, load it into the Kind cluster, deploy/update it with
  `kubectl`, and verify the rollout.
- Each build gets a unique tag (`build-${BUILD_NUMBER}`), so
  `kubectl rollout status` has something new to roll out every run — this is
  what makes the change visible each time.
- This mirrors a real CI/CD setup: Git is the source of truth, Jenkins is the
  automation server, and Kubernetes is the deployment target — just scaled
  down to run entirely on one laptop.

## Cleanup (after the workshop)

```bash
docker stop jenkins && docker rm jenkins
docker volume rm jenkins_home
kind delete cluster --name devops-workshop
```
