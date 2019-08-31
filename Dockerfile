# docker build -t paoloserver:latest . 
# docker run -t -p 5000:5000 paoloserver:latest (host:container btw)

# We wil use Alpine Linux because it's smol and designed for containers
FROM alpine:3.9.4

# Add a bunch of nice stuff; apologies to image size
# Upd: Blerghh alpine doesn't like psycopg2-binary/any wheel
# see https://github.com/psycopg/psycopg2/issues/684
# and initd.org/psycopg/docs/install.html#install-from-source
# So must add gcc, python3-dev, ...what is postgresql-dev... musl... what
# upd: jk there's py3-psycopg2 idk I'll use it
RUN apk update && apk add --no-cache bash vim python3 py3-psycopg2

# Apparently this is good practice. Still no good grasp of why tbh.
RUN adduser -D paolo
WORKDIR /home/paolo

# Stuff...
RUN pip3 install flask sqlalchemy
ENV FLASK_APP=paolo.py
ADD paolo.py .
ADD templates/hello.html templates/hello.html

# Shouldn't need this if you run with -p 5000:5000
# EXPOSE 5000

# CMD exists to provide DEFAULTS for an EXECUTING container.
# These defaults can include an executable, or they can omit it,
# in which case you must specify an ENTRYPOINT as well.
CMD flask run --host=0.0.0.0
