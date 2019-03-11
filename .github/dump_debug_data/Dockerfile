FROM python:3-alpine

RUN pip3 install requests

COPY dump_debug_data.py /dump_debug_data.py

ENTRYPOINT ["python3", "/dump_debug_data.py"]
