FROM python:3.12.2
ENV PYTHONBUFFERED 1
ADD . /app 
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD python app.py                                                              
FROM python:3.12.2
ENV PYTHONBUFFERED 1
ADD . /app
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install streamlit
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit","run","jo_ml.py"]