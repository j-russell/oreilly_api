FROM python:3.7
LABEL Josh Russell "josh.russell8@gmail.com"

WORKDIR /api

COPY ./ ./

RUN pip3 install -r requirements.txt

EXPOSE 88

ENTRYPOINT [ "python3" ]
CMD [ "./api/api.py" ]