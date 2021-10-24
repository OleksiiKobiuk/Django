# файл для опису образу контейнера Докера з Linux

FROM python:3.10-alpine
#створювач образу
MAINTAINER SomeDev
ENV PYTHONUNBUFFERED 1
# ENV - середовище, PYTHONUNBUFFERED ставимо в положення 1

RUN apk add --no-cache --virtual ..build-deps gcc musl-dev mariadb-dev

#for pillow (для роботи з фото)
RUN apk add jpeg-dev zlib-dev libjpeg

# створюємо в контейнері нову директорію для бекенду
RUN mkdir /app
WORKDIR /app
#папка app буде робочою папкою

# створюємо юзера операційної системи
RUN adduser -D user
# вказуємо, що юзером опер системи і буде створений юзер
USER user

# вказуємо запускну папку, тобто, в яку будуть встановлюватися pip пакети, наприклад Python
ENV PATH="/home/user/.local/bin:${PATH}"

# вказуємо версію pip 21.01, оскільки станом на 23.07.2021 наступні версії погано працювали з Докером
RUN python -m pip install pip==21.0.1 && pip install --user pipenv
# після && вказується наступна команда до виконання

COPY Pipfile* /tmp/
# копіюємо всі pip-файли (і Pipfile, і Pipfile.lock) в тимчасову папку Лінукса tmp

RUN cd /tmp && pipenv lock -r > requirements.txt && pip install --user -r requirements.txt
