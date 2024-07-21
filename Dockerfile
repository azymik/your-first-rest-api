FROM ubuntu:24.04

# ARG
ARG devpass

ENV TERM=xterm

RUN apt update && \
		apt install -y \
		curl \
		sudo \
		git \
		wget \
		vim \
		zsh \
		eza \
		bat \
		tre-command \
        python3.12 \
        python3-pip \
        python3.12-venv && \
		apt clean

RUN curl -SsL https://packages.httpie.io/deb/KEY.gpg | \
	gpg --dearmor -o /usr/share/keyrings/httpie.gpg
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/httpie.gpg] https://packages.httpie.io/deb ./" | \
	tee /etc/apt/sources.list.d/httpie.list > /dev/null
RUN apt update && \
	apt install -y httpie

RUN adduser --quiet --disabled-password --shell /bin/zsh --home /home/devuser --gecos "User" devuser
RUN touch /home/devuser/.zshrc
RUN echo "devuser:${devpass}" | chpasswd
RUN usermod -aG sudo devuser

USER devuser

RUN echo "y" | sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
WORKDIR /home/devuser
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
RUN git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
RUN sed -i "s/(git)/(git zsh-autosuggestions zsh-syntax-highlighting)/" .zshrc
RUN sed -i "s/robbyrussell/jonathan/" .zshrc
RUN echo "alias e='eza'\nalias b='batcat'" >> .zshrc
RUN echo "source ~/.venv/bin/activate" >> .zshrc
RUN git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
RUN yes | ~/.fzf/install

RUN git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
RUN sh ~/.vim_runtime/install_awesome_vimrc.sh
RUN echo "set mouse=a\nset number" >> ~/.vim_runtime/my_configs.vim
RUN python3.12 -m venv .venv
RUN . ~/.venv/bin/activate && pip install flask==3.0.3 flask-smorest==0.44.0 python-dotenv==1.0.1 sqlalchemy==2.0.31 \
	flask-sqlalchemy==3.1.1 flask-jwt-extended==4.6.0 passlib==1.7.4 flask-migrate==4.0.7 gunicorn==22.0.0 && \
	deactivate

# Can be removed if use 'gunicorn'
EXPOSE 5000
WORKDIR /app

CMD [ "zsh" ]
