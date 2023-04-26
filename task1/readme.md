1. Install Docker, kubectl and Istio
2. run ./deploy.sh
3. Get app1 IP from `kubectl get svc app1-service'
4. `curl http://<EXTERNAL_IP>/api`
3. [todo] to reset cluster run ./clean.sh