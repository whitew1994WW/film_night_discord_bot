FROM python:3.6

ADD . /
RUN pip install -r requirements.txt
ARG bot_token
ENV bot_token=${bot_token}
CMD ["python", "-m", "unittest discover tests"]
CMD "python" "./your_bot.py" "${bot_token}"