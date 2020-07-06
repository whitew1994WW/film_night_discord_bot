FROM python:3.6

ADD . /
RUN pip install -r requirements.txt
ARG bot_token
ENV bot_token=${bot_token}
RUN ["python", "-m", "unittest", "discover", "./tests"]
ENTRYPOINT "python" "./your_bot.py" "${bot_token}"