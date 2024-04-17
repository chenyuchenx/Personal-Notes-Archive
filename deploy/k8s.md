# K8s
```
kubectl config get-contexts
kubectl config current-context
kubectl config use-context <namespace>
kubectl -n <namespace> get po
kubectl get po
kubectl get secret
kubectl get secret <secret-file-name> -o yaml
kubectl get replicaset
kubectl delete replicaset
kubectl describe po
kubectl describe replicaset
kubectl get all
kubectl logs
kubectl edit deploy <<deployment file>>
kubectl port-forward rtm-ifp-etcd-ff69bb448-ck96j 2379:2379
kubectl rollout restart deploy ifps-predict-api
kubectl scale deploy ifps-predict-train --replicas=1
```

```
kubectl apply -f deployment.yml -n namespace
kubectl apply -f service.yml -n namespace
kubectl apply -f ingress.yml -n namespace
```

```
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

```
choco install kubernetes-helm
helm init --canary-image
helm version
```

```
helm list -n ifpsdemo
helm delete ifps-predict -n ifpsdemo
helm install ifps-predict . -n ifpsdemo
```

# Python
### Venv
```
python3 -m venv .venv
 .\venv\Scripts\activate.ps1
pip install -r requirements.txt
```
    
### Pyinstaller
```
pyinstaller -D main.py
```

# MongoDB
```
db.serverStatus().connections
db.runCommand({currentOp: 1, $all:[{"active" : true}]})
db.currentOp()
```

```
mongo --host 52.187.110.12:27017 --username e9662ce6-f9ba-4283-91ba-ab5d21e382bb --password bb283e12d5baab193824ab9f6ec2669e --authenticationDatabase admin
use 6dba1e66-a658-445a-b4cc-cb9602bb2d3e
mongo --host 192.168.56.237:27017/ifactory -u root  -p 1qaz@WSX3edc --authenticationDatabase SCRAM-SHA-1
```

### 創建新的database 和 創建 user
```
docker exec -it ___________ bash (container id)
> mongo -u root -p mLvt9SobUrReMhonVWYdsgaGPPu4XyAULYwzKIkRMYiZbxPcQxroot@197a630a48ed --authenticationDatabase admin (username, password)
> show dbs
> use _____ (dbs name)
> db.createUser({user:"root",pwd:"1qaz@WSX3edc",roles:[{role:"readWrite",db:"ifactory"}]})
```

# PostgreSQL
```
SELECT tag_id FROM spc.tag_map where tag_name = '$tag_name' and machine_id= '$machine_id'
machine_name SELECT machine_name_en FROM spc.machine where enable = true group by 1 ORDER BY 1
machine_id   SELECT machine_id FROM spc.machine where machine_name_en= '$machine_name'
tag_name     SELECT split_part(tag_name, '-', 1) FROM spc.tag_map where enable = true and machine_id= '$machine_id'  group by 1 ORDER BY 1
column_name  SELECT column_name FROM spc.column WHERE column_name IS NOT NULL group by 1
tag_id       SELECT tag_id FROM spc.tag_map where tag_name = '$tag_name'||'-'||'$column_name'
column_name  SELECT split_part(column_name, '(', 1) FROM spc.column WHERE column_name IS NOT NULL group by 1 ORDER BY 1

tag_name SELECT split_part(tag_name, '_', 1) from spc.tag_map full outer join spc.chart_config using(tag_id) where spc.chart_config.ctrl is not null and spc.tag_map.tag_name is not null and machine_id= '$machine_id'  group by 1 ORDER BY 1;

```

# Hana
```
hdbsql -u SYSTEM -p HXEHana1
hdbsql -i 90 -n 192.168.56.226:39017 -d SYS -u SYSTEM -p HXEHana1
hdbsql -i 90 -d SYS -u SYSTEM -p HXEHana1
```

# Example
```
SELECT *, (Height+Volume+Area) as Total FROM BR_6610
SELECT *, (Height+Volume+Area) as Total FROM `BR_6610.br_6610.csv`

SELECT * , convert_str_to_time(Date, Time) as creatAt FROM BR_6610
SELECT * , valueCount(Height, Volume) as valueCount FROM BR_6610

SELECT * FROM `BR_6610.br_6610.csv`
SELECT Job FROM `BR_6610.br_6610.csv` GROUP BY Job

SELECT Job, ComponentID, Count(*) FROM `BR_6610.br_6610.csv` GROUP BY Job, ComponentID, PinNumber
SELECT Job, ComponentID, PinNumber, Count(*) FROM `BR_6610.br_6610.csv` GROUP BY Job, ComponentID, PinNumber

SELECT *, concat(a.ComponentID,'_Height_',a.PinNumber) as PK FROM `BR_6610` a
SELECT *, concat(a.ComponentID,'_Height_',a.PinNumber) as PK FROM `BR_6610.br_6610.csv` a

SELECT *, concat(a.ComponentID,'_Height_',a.PinNumber) as PK,  concat(a.ComponentID,'_Area_',a.PinNumber) as PK1, concat(a.ComponentID,'_Volume_',a.PinNumber) as PK2 FROM `BR_6610.br_6610.csv` a

SELECT ComponentID, PinNumber, Count(*) FROM `SPC_v2.spc_v2.csv` GROUP BY ComponentID, PinNumber
```