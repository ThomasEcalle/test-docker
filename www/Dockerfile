FROM python:2.7
LABEL maintainer="Thomas Ecalle"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]