FROM python:2.7.13
MAINTAINER Your Name "saumya.bhasin23@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && \
    pip install PyGithub
ENTRYPOINT ["python","app.py"]
CMD [$1]
