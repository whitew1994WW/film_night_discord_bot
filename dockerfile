FROM python:3.6

ADD . /
RUN pip install -r requirements.txt
CMD ["python", "-m", "python -m unittest discover tests"]
CMD [ "python", "./your_bot.py" ]