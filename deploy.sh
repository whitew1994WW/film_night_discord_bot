#!/bin/bash
# install git
sudo yum install git -y
sudo yum install ncurses-devel gcc make openssl-devel zlib-devel bzip2 bzip2-devel readline-devel sqlite libxml2-dev libxslt-dev libffi-devel wget y
# Install screen
wget https://ftp.gnu.org/gnu/screen/screen-4.8.0.tar.gz
tar xzf screen-4.8.0.tar.gz
cd screen-4.8.0/
./configure --prefix=/usr                     \
            --infodir=/usr/share/info         \
            --mandir=/usr/share/man           \
            --with-socket-dir=/run/screen     \
            --with-pty-group=5                \
            --with-sys-screenrc=/etc/screenrc &&
sed -i -e "s%/usr/local/etc/screenrc%/etc/screenrc%" {etc,doc}/* &&
make
sudo make install &&
sudo install -m 644 etc/etcscreenrc /etc/screenrc
# install pyenv and associated functions
curl https://pyenv.run | bash
# edit .bashrc for pyenv
echo 'export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

source ~/.bashrc
mkdir ~/src
cd ~/src
git clone https://github.com/whitew1994WW/film_night_discord_bot.git
cd discord-bot-tempalate
pyenv install 3.6.6
pyenv virtualenv 3.6.6 discord_bot
pyenv local discord_bot
pip install -r requirements.txt
