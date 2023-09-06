FROM python:3.10.12 as base

WORKDIR /app

# system requirements
RUN apt-get update && apt-get install build-essential libhdf5-serial-dev graphviz graphviz-dev python3-gi python3-gi-cairo gir1.2-gtk-4.0 python3-pyaudio libpython3-dev \
    libdbus-1-dev libgeos++-dev libgeos-c1v5 libgeos-dev libgeos-doc libgirepository1.0-dev portaudio19-dev gdal-bin libgdal-dev cmake -y 

COPY requirements.txt /tmp/requirements.txt
COPY requirements.sandbox.txt /tmp/requirements.sandbox.txt

RUN --mount=type=cache,target=/root/.cache \ 
    pip install -r /tmp/requirements.txt

RUN --mount=type=cache,target=/root/.cache \
    pip install -r /tmp/requirements.sandbox.txt

# basemap

RUN pip install "cython < 3"

RUN pip install --no-build-isolation basemap==1.3.2 basemap-data==1.3.2

COPY . /app

FROM base as development

EXPOSE 3000
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]

FROM base as default
EXPOSE 3000

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "3000"]