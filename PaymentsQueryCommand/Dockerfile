FROM python:3.6
ENV FLASK_RUN_PORT=8003
COPY . /payments-query-command
WORKDIR /payments-query-command
RUN pip install -r requirements.txt
EXPOSE 8003
CMD ["python","app.py"]