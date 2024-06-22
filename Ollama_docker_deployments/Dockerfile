FROM ubuntu:latest

WORKDIR /app

RUN apt update && apt upgrade -y

RUN apt install curl -y


RUN curl -fsSL https://ollama.com/install.sh -O

RUN chmod +x install.sh

RUN ./install.sh

RUN export OLLAMA_NUM_PARALLEL=4

RUN export OLLAMA_MAX_LOADED_MODELS=4

# RUN ollama pull phi3:3.8b-mini-4k-instruct-q4_0

EXPOSE 11434

# ENTRYPOINT ["/bin/bash"]

CMD ["ollama", "serve"]