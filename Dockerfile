from clickbg/miiocli

ADD requirements.txt .
ADD robodaemon.py .
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 robodaemon.py
