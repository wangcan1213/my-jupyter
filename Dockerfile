FROM jupyterhub/jupyterhub:latest

RUN pip install --no-cache \
    oauthenticator \
    dockerspawner \
    jupyterhub-nativeauthenticator

RUN pip install --no-cache \
    numpy pandas matplotlib scikit-learn graphviz  \
	tensorflow torch torchvision torchaudio \
    -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com

RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN echo "jovyan ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/notebook

COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
