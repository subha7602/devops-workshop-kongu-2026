# Lab 1 — Docker + Kind (Kubernetes in Docker)

Goal: build a small Flask app into a Docker image, spin up a local Kubernetes
cluster with Kind, and deploy the image into it. This is the same cluster
Lab 2's Jenkins pipeline deploys to.

## Prerequisites

- Docker Desktop running
- `kubectl` installed
- `kind` installed ([kind.sigs.k8s.io](https://kind.sigs.k8s.io/docs/user/quick-start/#installation))

## 1. Build the image

```bash
cd hands-on/01-sample-webapp
docker build -t sample-webapp:local .
docker run --rm -p 5000:5000 sample-webapp:local
# in another terminal: curl localhost:5000
```

Stop the container (Ctrl+C) once you've confirmed it works.

## 2. Create a local cluster

```bash
kind create cluster --name devops-workshop
kubectl cluster-info --context kind-devops-workshop
```

## 3. Load the image into the cluster

Kind clusters can't pull images from your local Docker daemon by default, so
the image has to be loaded in explicitly:

```bash
kind load docker-image sample-webapp:local --name devops-workshop
```

## 4. Deploy

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

kubectl get pods
kubectl get deployments
kubectl get svc
```

## 5. Access the app

```bash
kubectl port-forward svc/sample-webapp 8080:80
# visit http://localhost:8080 in your browser
```

## 6. Break it on purpose (for Lab 2)

Try one of these and observe what `kubectl get pods` shows:

```bash
kubectl set image deployment/sample-webapp sample-webapp=sample-webapp:doesnotexist
kubectl get pods
kubectl describe pod <pod-name>
```

Undo it:

```bash
kubectl set image deployment/sample-webapp sample-webapp=sample-webapp:local
```

Keep this cluster running — Lab 2's Jenkins pipeline deploys to it directly.

## Cleanup (after the workshop)

```bash
kind delete cluster --name devops-workshop
```
