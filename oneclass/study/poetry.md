安裝
- curl -sSL https://install.python-poetry.org | python3 -
初始化
- poetry init
建立虛擬環境
- poetry env use python3.12
修改設定
- poetry config --list
- poetry config virtualenvs.in-project true
刪除虛擬環境
- poetry env remove python3.12
開啟和關閉虛擬環境
- poetry shell
- exit
套件P2P
- poetry lock
套件全更新
- poetry update
顯示依賴關係
- poetry show
- poetry show --tree
刪除套件
- poetry remove
輸出Ｒ檔
- poetry export -f requirements.txt -o requirements.txt --without-hashes
下載就專案的環境
- poetry install

