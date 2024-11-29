FROM jenkins/jenkins:lts

USER root

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common && \
    mkdir -p /etc/apt/keyrings

# Добавление ключа и репозитория Docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bullseye stable" > /etc/apt/sources.list.d/docker.list

# Установка Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Переключение на пользователя Jenkins
USER jenkins

# Установка плагинов Jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"

