FROM python:3.6
ENV FLASK_RUN_PORT=8004
COPY . /user-query-command
WORKDIR /user-query-command
RUN pip install -r requirements.txt
EXPOSE 8004
CMD ["python","app.py"]