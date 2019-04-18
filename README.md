I followed (https://packaging.python.org/tutorials/packaging-projects/) for packaging this project. This uploaded the distro to the PYPI testing repo.

So to get it, you can just type:
```
python3 -m venv .venv
source .venv/bin/activate
pip install -i https://test.pypi.org/simple/ python-sample

```

curl https://s3-us-west-2.amazonaws.com/personalize-cli-json-models/personalize.json -o personalize.json
curl https://s3-us-west-2.amazonaws.com/personalize-cli-json-models/personalize-runtime.json -o personalize-runtime.json
aws configure add-model --service-model file://`pwd`/personalize.json --service-name personalize
aws configure add-model --service-model file://`pwd`/personalize-runtime.json --service-name personalize-runtime

Things to remember are:
* On OSX, install CLI tools with pip (python3 -m pip) globally. Using --user means the tools aren't on the path.

### Links
*  https://packaging.python.org/tutorials/packaging-projects/
*  https://github.com/storborg/python-packaging/blob/master/command-line-scripts.rst