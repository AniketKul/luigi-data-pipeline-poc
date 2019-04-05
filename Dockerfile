FROM python:3.7.3

# copy all project files and change perms on dir
COPY . /data_pipeline_with_luigi/example_dir
WORKDIR /data_pipeline_with_luigi/example_dir

# volume to save data
VOLUME ["/data"]

RUN pip install -r requirements.txt
RUN pip install -e .

EXPOSE 8080
ENTRYPOINT ["example_dir"]
