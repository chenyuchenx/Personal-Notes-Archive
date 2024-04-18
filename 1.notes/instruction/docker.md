## 測試
+ cAdvisor    --> 採集Liunx的Cagroups獲取容器的資源使用資訊
+ Prometheus  --> 推送cAdvisor裡metrics的時間序列資料
+ Dashboard   --> 呈現Prometheus的資料

## Port Forwarding
+ 如果是用虛擬機架 應該需要額外設置虛擬機 port forwarding
+ 用 powershelll 執行
```
-> Add-NetNatStaticMapping -ExternalIPAddress 0.0.0.0/0 -ExternalPort 5000 -Protocol TCP -InternalIPAddress 10.153.72.2 -InternalPort 5000 -NatName IFS_Nat
-> Add-NetNatStaticMapping -ExternalIPAddress 0.0.0.0/0 -ExternalPort 5082 -Protocol TCP -InternalIPAddress 10.153.72.2 -InternalPort 5082 -NatName IFS_Nat
```
+ 上面指令可以把本機的9000port 轉到虛擬機的9000port
```
Add-NetNatStaticMapping -ExternalIPAddress 0.0.0.0/0 -ExternalPort 9000 -Protocol TCP -InternalIPAddress 10.153.72.2 -InternalPort 9000 -NatName IFS_Nat
```
### k8s Port Forwarding
```
kubectl -n development port-forward pivot-etcd-7845bb76cb-t8qf6 2379:2379 --address='0.0.0.0'

kubectl port-forward pivot-etcd-c78ccb9f-c2nzb 2379:2379 --address='0.0.0.0'

kubectl get pod -o wide
```

# Docker

### Docker 基本指令

**檢查 Docker 版本：**
```
docker --version
```

**運行 Python 容器：**
```
docker run --rm -it python:3 python
```

**Other：**
```
docker ps
docker stop <container_id>
docker rm <container_id>
docker images
docker rmi <image_id>
docker run -d -p 8000:8000 <image_id>
docker logs <container_id>
docker exec -it <container_id> /bin/bash
docker cp <container_id>:/app/app.py .
docker cp <container_id>:/app/requirements.txt .
```

**Docker-Compose：**
```
docker-compose up
docker-compose down
docker-compose ps
docker-compose rm
```

```
sudo docker cp b64538b4b5ca:/usr \Users\Yetta Chen\Desktop
docker cp b64538b4b5ca:/usr/local/lib/python3.6/dist-packages/osm_im target
docker cp b64538b4b5ca:/app/storage storage
```

```
curl --silent --output docker-compose.yml https://raw.githubusercontent.com/confluentinc/cp-all-in-one/6.1.0-post/cp-all-in-one/docker-compose.yml
```

```
docker run --name mongo4 -d -p 37017:27017 --rm mongo:4.1
docker run -d  --name mongo4  -p 27888:27017 mongo
docker run -d  -p 9999:9999 1db325daddc7
```

```
apt update && apt install telnet && telnet mongo 27017
127.0.0.1:5081
```

```
telnet mongo 27888
telnet ifp_organizer 80
```

### Docker 比喻

Docker 是一個開源平台，用於開發、交付和運行應用程序。以下是一些比喻來幫助理解 Docker 的概念：
- **映像檔（Image）**：就像系統安裝映像檔，它包含了應用程序運行所需的所有文件和配置。
- **容器（Container）**：就像被安裝好的作業系統，它是從映像檔啟動的運行實例，具有自己的文件系統、網絡和進程空間。

### Docker 流程
1. **新增 Dockerfile**：創建一個名為 Dockerfile 的文本文件，用於定義映像檔的結構和內容。
2. **找到適合的基礎映像檔**：通常從 Docker Hub 上找到適合你應用程序的基礎映像檔，例如 Python、Node.js 等。
3. **複製原始碼**：在 Dockerfile 中添加命令來複製你的應用程序原始碼到容器中。
4. **安裝依賴項**：如果你的應用程序有依賴項，則需要在 Dockerfile 中添加相應的安裝命令。
5. **設定初始命令**：在 Dockerfile 中定義容器啟動後要執行的初始命令，例如運行應用程序的指令。

一旦 Dockerfile 定義完成，你可以使用 `docker build` 命令來生成映像檔，然後使用 `docker run` 命令來運行容器。

### node 9.7 dockerfile
```
FROM node:9.17-stretch-slim

COPY ifp-andon /ifp-andon
WORKDIR /ifp-andon
#COPY . .
RUN npm install --no-optional
#RUN npm run build

CMD [ "npm", "run", "start"]
```
