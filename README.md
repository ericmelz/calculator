# Calculator

A simple calculator for project demo purposes.

## Get the project
Find a suitable dir (such as `~/Data/code`) and:
```bash
cd ~/Data/code
rm -rf calculator
git clone git@github.com:ericmelz/calculator.git
cd calculator
```

## Local laptop native setup
### Install uv if it's not already on your system

```bash
pip install uv
```

### Create and activate a virtual environment
```bash
uv venv
```

### Install dependencies, including development dependencies
```bash
uv pip install -e ".[dev]"
```

### Run tests
```bash
uv run pytest
```

### Run the app
```bash
uv run streamlit run src/app.py
^c
CALCULATOR_CONF_FILE=var/conf/calculator/.env.prod uv run streamlit run src/app.py
^c
```

## Pycharm setup
In Pycharm Open a new project and navigate to the
directory where you cloned the calculator repo.

Configure the Project Interpreter to use UV:
![Project Interpreter](doc-images/project%20interpreter.png)


## Local Docker setup
### Build and run the docker image
```bash
./run.sh
```

### Hit the app
visit <http://localhost:8501>

## Local k3d setup
### Prerequisites
- Docker installed
- k3d installed (`curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash`)

### Record the configuration directory
```bash
VAR_DIR=$(pwd)/var
```
### Create a new k3d cluster
```bash
k3d cluster create calculator --api-port 6443 -p "8899:80@loadbalancer" --volume "$VAR_DIR:/mnt/var@server:0"
```

### Create a persistent volume and persistent volume claim
```bash
kubectl apply -f k8s-pv
kubectl get pv,pvc
```

Ensure the `STATUS` for the pv and pvc is `Bound`.

### Test writing from k3d:
```bash
kubectl apply -f k8s-test
cat $VAR_DIR/conf/calculator/hello.txt
kubectl exec tester-hostpath -it -- /bin/sh 
cd /conf
ls -la
exit
rm $VAR_DIR/conf/calculator/hello.txt
kubectl delete pod tester-hostpath
```

### Build the Docker image and import it into the cluster
```bash
docker build -t calculator:latest .
k3d image import calculator:latest -c calculator
```
### Install the configuration encryption key
```bash
export GPG_PASSPHRASE=s3cr3t!
kubectl create secret generic gpg-passphrase --from-literal=GPG_PASSPHRASE=$GPG_PASSPHRASE
```

### Deploy to k3d
```bash
kubectl apply -f k8s/
```

### Verify deployment
```bash
kubectl get deployments
kubectl get pods
kubectl get ingress
```

### Access the service
visit http://localhost:8899/calculator/

### Destroy cluster
```bash
k3d cluster delete calculator
```

## Configuration Note
The kubernetes environment assumes that configuration exists as 
gpg-encrypted .env files.  Here are some sample commands for encrypting
and decrypting files.  Do not store unencrypted credentials on your
file system.
```bash
export GPG_PASSPHRASE=$(openssl rand -base64 32)
cat conf/.env.prod|gpg --symmetric --cipher-alg AES256 --batch --passphrase "$GPG_PASSPHRASE" -o conf/.env.prod.encrypted
gpg --batch --yes --passphrase "$GPG_PASSPHRASE" -o conf/.env.prod.decrypted -d conf/.env.prod.encrypted                          
```

## Deployment
TBD