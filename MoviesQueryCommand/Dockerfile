FROM python:3.6
ENV FLASK_RUN_PORT=8001
COPY . /movies-query-command
WORKDIR /movies-query-command
RUN pip install -r requirements.txt
EXPOSE 8001
CMD ["python","app.py"]