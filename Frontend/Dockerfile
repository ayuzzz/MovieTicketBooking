FROM python:3.6
COPY . /frontend
WORKDIR /frontend
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]