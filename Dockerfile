FROM python:3.9
LABEL MAINTAINER="Mojtaba Pooresmaeili| child_foundation"

ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /childfoundation
WORKDIR /childfoundation
COPY . /childfoundation

# Installing requirements
ADD requirements/requirements.txt /childfoundation
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "childfoundation", "--bind", ":8000", "childfoundation.wsgi:application"]