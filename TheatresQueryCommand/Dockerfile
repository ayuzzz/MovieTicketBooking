FROM python:3.6
ENV FLASK_RUN_PORT=8002
COPY . /theatres-query-command
WORKDIR /theatres-query-command
RUN pip install -r requirements.txt
EXPOSE 8002
CMD ["python","app.py"]