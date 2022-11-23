FROM python:3.11

WORKDIR /app

COPY ./requirements.txt /app/

COPY ./Makefile /app/

COPY ./.dockerignore /app/

RUN pip install -r requirements.txt

COPY ./app/ /app/

# change default port
ENV STREAMLIT_SERVER_PORT=8080

# change theme of the app
ENV STREAMLIT_THEME_BASE=light

EXPOSE 8080

CMD [ "streamlit", "run", "main.py" ]