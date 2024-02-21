# uv-playground

playground to test the uv package installer and resolver!

## Tests

Test how the installer and resolver works with a requirements.txt.


### Install with pip

Use the [Install with pip Action](https://github.com/alice-biometrics/uv-playground/actions/workflows/pip.yml) to test it. 

```console
pip install -r requirements.txt
```

### Install with uv

Use the [Install with uv Action](https://github.com/alice-biometrics/uv-playground/actions/workflows/uv.yml) to test it.

```console
uv pip install -r requirements.txt
```

## Time comparison

| Action           | Install time |
|------------------|--------------|
| Install with pip | 148 seconds  |
| Install with uv  | 37 seconds   |

Install with uv is **4 times faster** with tested requirements.txt

