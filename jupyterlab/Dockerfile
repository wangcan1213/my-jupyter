FROM jupyter/base-notebook

USER root

RUN apt-get update && apt-get install -y graphviz

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY ./workdir/simhei.ttf /usr/share/fonts/

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
	
RUN mkdir -p /home/jovyan/work \
    && chmod -R 777 /home/jovyan/work

USER jovyan