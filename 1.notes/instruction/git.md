# Git
## **Git:**
```
ghp_
aDBo
0ZGAcE8O9
zJaWeGPwB
TvZXxQzb0
jNjPw
```

##  **Git Repo:**
```
https://github.com/EI-Stack/fast-igp-api.git
https://github.com/chenyuchenx/fast-api.git
```

## Git commit message
### Commit Message 最好兼俱 Why 及 What
- 應該獨立 Commit 每個不同意義的異動，這樣 commit 訊息才會跟異動的程式碼有關聯。
- 每次 Commit 都是針對異動的檔案做說明：Why & What。
- 這樣的 Commit Message 能讓日後的維護人員更快進入狀況
- 每次 Commit 都加上 issue 編號，方便追蹤相關的程式異動原因。
### Commit Message 標準樣式
#### Header: <type>(<scope>): <subject>
- type: 代表 commit 的類別：feat, fix, docs, style, refactor, test, chore，必要欄位。
- feat: 新增/修改功能 (feature)。
- fix: 修補 bug (bug fix)。
- docs: 文件 (documentation)。
- style: 格式 (不影響程式碼運行的變動 white-space, formatting, missing semi colons, etc)。
- refactor: 重構 (既不是新增功能，也不是修補 bug 的程式碼變動)。
- perf: 改善效能 (A code change that improves performance)。
- test: 增加測試 (when adding missing tests)。
- chore: 建構程序或輔助工具的變動 (maintain)。
- revert: 撤銷回覆先前的 commit 例如：revert: type(scope): subject (回覆版本：xxxx)。
- scope 代表 commit 影響的範圍，例如資料庫、控制層、模板層等等，視專案不同而不同，為可選欄位。
- ubject 代表此 commit 的簡短描述，不要超過 50 個字元，結尾不要加句號，為必要欄位。

## Homebrew
**The Missing Package Manager for macOS (or Linux)**
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh
```
```
brew install git
```

## Git bash 常用指令
``` bash
git init
# 建立新的本地端 Repository。

git clone [Repository URL]
# 複製遠端的 Repository 檔案到本地端。

git status
# 檢查本地端檔案異動狀態。

git add [檔案或資料夾]
# 將指定的檔案（或資料夾）加入版本控制。用 git add . 可加入全部。

git rm --cached<name>
# 取消選取的檔案

git commit -m "提交說明內容"
# 提交（commit）目前的異動並透過 -m 參數設定摘要說明文字。

git stash
# 獲取目前工作目錄的 dirty state，並保存到一個未完成變更的 stack，以方便隨時回復至當初的 state。

git log
# 查看先前的 commit 記錄。

git push
# 將本地端 Repository 的 commit 發佈到遠端。

git push origin [BRANCH_NAME]
# 發佈至遠端指定的分支（Branch）

git branch
# 查看分支。

git branch [BRANCH_NAME]
# 建立分支。

git checkout [BRANCH_NAME]
# 取出指定的分支。

git checkout -b [BRANCH_NAME]
# 建立並跳到該分支。

git branch -D [BRANCH_NAME]
# 強制刪除指定分支（須先切換至其他分支再做刪除）。

git reset --hard [HASH]
# 強制恢復到指定的 commit（透過 Hash 值）。

git checkout [HASH]
# 切換到指定的 commit（與 git checkout [BRANCH_NAME] 相同)。

git branch -m <OLD_BRANCH_NAME> <NEW_BRANCH_NAME>
# 修改分支名稱。

```