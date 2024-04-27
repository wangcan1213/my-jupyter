FROM jupyter/datascience-notebook

RUN rmdir work

USER root

RUN apt-get update && apt-get install -y graphviz

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY ./includes/simhei.ttf /usr/share/fonts/

RUN fc-cache -fv


RUN pip install --no-cache \
    numpy pandas matplotlib scikit-learn graphviz  \
	tensorflow torch torchvision torchaudio opencv-python Pillow\
    -i http://mirrors.tencentyun.com/pypi/simple --trusted-host mirrors.tencentyun.com
    
RUN apt-get update \
    && apt-get install -y git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /etc/sudoers.d \
    && echo "jovyan ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/notebook

USER jovyan
	
RUN mkdir ./jupyter && sudo chmod 777 ./jupyter
