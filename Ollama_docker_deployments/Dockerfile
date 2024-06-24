FROM ubuntu:latest

WORKDIR /app

RUN apt update && apt upgrade -y

RUN apt install curl -y

RUN curl -fsSL https://ollama.com/install.sh -O

RUN chmod +x install.sh

COPY ./pull_model.sh /app/run-ollama.sh

RUN ./install.sh

EXPOSE 11434

RUN chmod +x run-ollama.sh && ./run-ollama.sh

RUN export OLLAMA_NUM_PARALLEL=4

RUN export OLLAMA_MAX_LOADED_MODELS=4

ENTRYPOINT ["/bin/bash"]

CMD ["ollama", "serve"]