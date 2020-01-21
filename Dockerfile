# start from an official image
FROM python:3.6

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/digiskills
WORKDIR /opt/services/digiskills

# install our two dependencies
ADD requirements.txt /opt/services/digiskills/
RUN pip install -r requirements.txt

# copy our project code
COPY . /opt/services/digiskills/

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "src", "--bind", ":8000", "digiskills.wsgi:application"]