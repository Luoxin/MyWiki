#  ssh相关

## Windows

### 获取ssh
- 若不支持ssh，这执行
  - 在`PowerShell` 中输入` Add-WindowsCapability -Online -Name OpenSSH-Client`安装ssh
- 执行`ssh-keygen -t rsa` 命令
  - -t  类型type，加密类型；-b 秘钥位数

### 生成Putty秘钥
- 下载`puttygen`,下载地址`https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html`
- 