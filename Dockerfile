FROM python:3.6-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY requirements.txt setup.sh ./
COPY source_sage_challenge ./source_sage_challenge

# Install API dependencies
RUN pipenv install

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/app/setup.sh"]