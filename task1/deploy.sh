#!/bin/bash

# Build Docker images
docker build -t raiskii/app1:latest -f Dockerfile.app1 .
docker build -t raiskii/app2:latest -f Dockerfile.app2 .

# Apply Kubernetes manifests
kubectl apply -f app1-deployment.yaml
kubectl apply -f app1-service.yaml
kubectl apply -f app2-deployment.yaml
kubectl apply -f app2-service.yaml
kubectl apply -f istio-egress-gateway.yaml
