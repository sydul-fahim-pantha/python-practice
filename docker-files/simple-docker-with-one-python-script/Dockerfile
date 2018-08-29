FROM ubuntu:latest
LABEL base.name="Ubuntu with python3"
MAINTAINER sydul-fahim-pantha
RUN apt-get update && apt-get install -y python3
ENV APPROOT="/app"
WORKDIR $APPROOT
COPY ["./app.py", "${APPROOT}"]
ENTRYPOINT ["python3", "app.py"]

