#!/bin/bash
# Copyright (c) 2020 astherier
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#
#WSL2+Ubuntu 20.04でGUIアプリが動くように設定し、Ubuntu Desktopをインストールします

# https://astherier.com/blog/2020/07/install-wsl2-on-windows-10-may-2020/
#WSL環境の各パッケージをアップデートします。
sudo apt update -y
sudo apt upgrade -y

# https://astherier.com/blog/2020/08/run-gui-apps-on-wsl2/
#GUIアプリを動かすため、いくつかソフトを入れて設定します。
#Windows側の設定も必要です。詳細はリンクを見てください。
sudo apt install -y libgl1-mesa-dev xorg-dev xbitmaps x11-apps

echo 'export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '\''{print $2}'\''):0.0' >> ~/.profile

cat << 'EOS' | sudo tee /etc/fonts/local.conf
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
    <dir>/mnt/c/Windows/Fonts</dir>
</fontconfig>
EOS
#起動確認：
# $ xeyes

#https://astherier.com/blog/2020/08/install-ubuntu-desktop-on-wsl2/
#Ubuntu Desktopのインストール
sudo apt -y install ubuntu-desktop
sudo service x11-common start
sudo service dbus start
#起動確認：
#WSLを再起動し、VcXsrvの設定を変更して
# $ sudo service x11-common start && sudo service dbus start && gnome-shell --x11 -r

echo "
一旦、WSL2を終了してください。
　例）wsl.exe -t Ubuntu-20.04
その後、もう一度WSL2 Ubuntuを起動してからGUIを起動してください。
"