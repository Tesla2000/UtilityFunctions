## Description

Utility functions for python without any specific purpose but once that are not a part of any specific library that I don't want to recreate

## Running

You can run script with docker or python

### Python
```shell
python main.py --config_file utility_functions/config_sample.toml
```

### Cmd
```shell
poetry install
poetry run utility_functions
```

### Docker
```shell
docker build -t UtilityFunctions .
docker run -it UtilityFunctions /bin/sh
python main.py
```
