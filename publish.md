# 打包上传步骤

### 1. 修改版本等信息

### 2. 打包


```
python3 -m pip install --upgrade build
python3 -m build

```

### 3. 发布上传

```
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
```

参考 https://packaging.python.org/en/latest/tutorials/packaging-projects/
