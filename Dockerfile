# docker build -t paoloserver:latest . 
# docker run -t -p 5000:5000 paoloserver:latest (host:container btw)

# We wil use Alpine Linux because it's smol and designed for containers
FROM alpine:3.9.4

# Add a bunch of nice stuff; apologies to image size
RUN apk update && apk add --no-cache bash vim python3

# Apparently this is good practice. Still no good grasp of why tbh.
RUN adduser -D paolo
WORKDIR /home/paolo

# Stuff...
RUN pip3 install flask
ENV FLASK_APP=paolo.py
ADD paolo.py .

# Shouldn't need this if you run with -p 5000:5000
# EXPOSE 5000

# CMD exists to provide DEFAULTS for an EXECUTING container.
# These defaults can include an executable, or they can omit it,
# in which case you must specify an ENTRYPOINT as well.
CMD flask run --host=0.0.0.0
