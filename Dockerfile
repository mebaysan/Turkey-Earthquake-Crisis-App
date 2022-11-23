FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/

COPY ./Makefile /app/

COPY ./.dockerignore /app/

RUN pip install -r requirements.txt

COPY ./app/ /app/

EXPOSE 8501

CMD [ "streamlit", "run", "main.py" ]