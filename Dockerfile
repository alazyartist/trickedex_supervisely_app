FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y build-essential && \
    conda update -n base -c defaults conda && \
    conda create -n my_env python=3.9 && \
    echo "source activate my_env" > ~/.bashrc && \
    conda clean -ya

SHELL ["/bin/bash", "-c"]

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]

